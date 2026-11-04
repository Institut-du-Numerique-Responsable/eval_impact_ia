#!/usr/bin/env python3
"""
Scrape le site EcoInfo (ecoinfo.cnrs.fr) pour trouver des ressources sur
l'impact environnemental de l'IA et du numérique.

Utilise l'API REST WordPress : https://ecoinfo.cnrs.fr/wp-json/wp/v2/

Catégories pertinentes (IDs) :
  - 205 : Intelligence Artificielle (IA)
  - 110 : Analyse de cycle de vie (ACV)
  - 79  : Datacentres
  - 12  : Energie
  - 36  : Mesures et indicateurs
  - 204 : Ecoconception
  - 108 : Accessibilité
  - 211 : Agir

Usage :
    python scrape_ecoinfo.py                    # -> output/ecoinfo_ressources.*
    python scrape_ecoinfo.py --categories 205,110,79,12,36,204
    python scrape_ecoinfo.py --min-score 3
    python scrape_ecoinfo.py --clear-cache
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
from dataclasses import dataclass, asdict, fields
from pathlib import Path
from urllib.parse import quote

import requests

from scrape_cache import cached_request, clear_cache, get_cache_stats

API = "https://ecoinfo.cnrs.fr/wp-json/wp/v2"
HEADERS = {"User-Agent": "eval-CO2-IA-inventory/1.0 (+recherche outils empreinte IA)"}

# Désactiver la vérification SSL par défaut (certificat du site pose problème)
VERIFY_SSL = False

# Catégories pertinentes (noms -> IDs)
CATEGORIES = {
    "ia": 205,           # Intelligence Artificielle (IA)
    "acv": 110,          # Analyse de cycle de vie (ACV)
    "datacentres": 79,   # Datacentres
    "energie": 12,       # Energie
    "mesures": 36,       # Mesures et indicateurs
    "ecoconception": 204,# Ecoconception
    "accessibilite": 108,# Accessibilité
    "agir": 211,         # Agir
}

# Catégories par défaut à scrapper
DEFAULT_CATEGORIES = [205, 110, 79, 12, 36, 204, 108, 211]

# Axes d'impact
AXES = {
    "carbone": ["carbon", "carbone", "co2", "co₂", "ges", "gwp", "greenhouse",
                "emission", "émission", "bilan carbone", "decarbon"],
    "energie": ["energy", "energie", "énergie", "energétique", "energetique",
                "kwh", "watt", "power", "electricit", "électricit", "rapl",
                "consumption", "consommation"],
    "eau": ["water", "eau", "hydric", "hydrique", "water footprint"],
    "acv": ["life cycle", "lca", "acv", "cycle de vie", "embodied", "cradle",
            "ecoinvent", "footprint", "empreinte", "environmental impact",
            "impact environnemental"],
    "mesure": ["measure", "mesure", "monitor", "metering", "profil", "benchmark",
               "tracker", "tracking", "exporter", "telemetry", "sensor"],
}

# Termes IA/Numérique
IA_TERMS = [
    " ai ", "ai-", "-ai", "ia ", " ia", "llm", "gpt", "machine learning",
    "deep learning", "neural network", "inference", "inférence", "gpu",
    "transformer", "nlp", "mlops", "genai", "intelligence artificielle",
    "artificial intelligence", "pytorch", "tensorflow", "hugging face",
]

NUM_TERMS = [
    "datacenter", "data center", "cloud", "software", "logiciel", "hpc",
    "computing", "server", "serveur", "ict", "numérique", "numerique",
    "digital", "web", "semiconductor", "cpu", "hardware", "network",
]

NOISE = [
    "nanotube", "radiocarbon", "carbon fiber", "carbon fibre", "graphene",
    "carbon capture", "biochar", "peatland", "soil organic carbon",
]


@dataclass
class Ressource:
    source: str
    ressource_id: str
    type: str
    titre: str
    url: str
    date: str
    categories: str
    categories_ids: str
    resume: str
    score: int
    axes: str
    ia: bool
    requetes: str


def _txt(x: str | None) -> str:
    """Nettoie le texte (supprime les balises HTML et les espaces multiples)."""
    if x is None:
        return ""
    x = re.sub(r"<[^>]+>", " ", x)  # Supprime les balises HTML
    return re.sub(r"\s+", " ", x).strip()


def _hay(d: dict) -> str:
    """Génère une chaîne de texte pour l'évaluation."""
    return f"{_txt(d.get('title', {}).get('rendered', ''))} " \
           f"{_txt(d.get('content', {}).get('rendered', ''))[:2000]}".lower()


def evaluer(d: dict) -> tuple[int, list[str], bool]:
    """Évalue une ressource et retourne (score, axes, est_ia)."""
    h = _hay(d)
    
    # Filtrer le bruit
    if any(n in h for n in NOISE):
        return 0, [], False
    
    # Détecter les axes
    axes = [a for a, mots in AXES.items() if any(m in h for m in mots)]
    impact = [a for a in axes if a != "mesure"]
    if not impact:
        return 0, [], False
    
    # Détecter IA/numérique
    ia = any(t in h for t in IA_TERMS)
    num = any(t in h for t in NUM_TERMS)
    
    # Calculer le score
    score = len(impact) + (1 if "mesure" in axes else 0) + (2 if ia else (1 if num else 0))
    if not (ia or num):
        score -= 1
    
    return score, axes, ia


@cached_request("ecoinfo", ttl=86400)
def _fetch_posts(categories: list[int], per_page: int = 100, page: int = 1) -> list[dict]:
    """Récupère les posts d'EcoInfo pour les catégories spécifiées."""
    cats_str = ",".join(str(c) for c in categories)
    url = f"{API}/posts?categories={cats_str}&per_page={per_page}&page={page}"
    
    try:
        r = requests.get(url, headers=HEADERS, timeout=30, verify=VERIFY_SSL)
        if r.status_code == 200:
            return r.json()
        print(f"  ! HTTP {r.status_code} pour {url}", file=sys.stderr)
        return []
    except requests.RequestException as e:
        print(f"  ! Erreur pour {url}: {e}", file=sys.stderr)
        return []


@cached_request("ecoinfo", ttl=86400)
def _fetch_pages(per_page: int = 100, page: int = 1) -> list[dict]:
    """Récupère les pages d'EcoInfo."""
    url = f"{API}/pages?per_page={per_page}&page={page}"
    
    try:
        r = requests.get(url, headers=HEADERS, timeout=30, verify=VERIFY_SSL)
        if r.status_code == 200:
            return r.json()
        print(f"  ! HTTP {r.status_code} pour {url}", file=sys.stderr)
        return []
    except requests.RequestException as e:
        print(f"  ! Erreur pour {url}: {e}", file=sys.stderr)
        return []


def _get_category_names(category_ids: list[int]) -> list[str]:
    """Convertit les IDs de catégories en noms."""
    # Inverser le dictionnaire CATEGORIES
    id_to_name = {v: k for k, v in CATEGORIES.items()}
    return [id_to_name.get(cid, str(cid)) for cid in category_ids]


def collecter_ressources(categories: list[int], min_score: int = 3, 
                         ia_only: bool = False) -> list[Ressource]:
    """Collecte les ressources (posts + pages) depuis EcoInfo."""
    trouves: dict[str, Ressource] = {}
    
    # Récupérer les pages
    print("# Récupération des pages...", file=sys.stderr)
    page_num = 1
    while True:
        pages = _fetch_pages(per_page=100, page=page_num)
        if not pages:
            break
        
        for page in pages:
            score, axes, ia = evaluer(page)
            if score < min_score or (ia_only and not ia):
                continue
            
            url = page.get("link", "")
            if not url:
                continue
            
            if url in trouves:
                continue
            
            category_names = _get_category_names(page.get("categories", []))
            category_ids = page.get("categories", [])
            
            trouves[url] = Ressource(
                source="ecoinfo.cnrs.fr",
                ressource_id=str(page.get("id", "")),
                type="page",
                titre=_txt(page.get("title", {}).get("rendered", "")),
                url=url,
                date=page.get("date", "")[:10] if page.get("date") else "",
                categories=", ".join(category_names),
                categories_ids=", ".join(str(c) for c in category_ids),
                resume=_txt(page.get("content", {}).get("rendered", ""))[:500],
                score=score,
                axes=", ".join(sorted(axes)),
                ia=ia,
                requetes="",
            )
        
        if len(pages) < 100:
            break
        page_num += 1
        time.sleep(0.5)
    
    # Récupérer les posts par catégorie
    print("# Récupération des posts par catégorie...", file=sys.stderr)
    for cat_id in categories:
        page_num = 1
        while True:
            posts = _fetch_posts(categories=[cat_id], per_page=100, page=page_num)
            if not posts:
                break
            
            for post in posts:
                score, axes, ia = evaluer(post)
                if score < min_score or (ia_only and not ia):
                    continue
                
                url = post.get("link", "")
                if not url:
                    continue
                
                if url in trouves:
                    continue
                
                category_names = _get_category_names(post.get("categories", []))
                category_ids = post.get("categories", [])
                
                trouves[url] = Ressource(
                    source="ecoinfo.cnrs.fr",
                    ressource_id=str(post.get("id", "")),
                    type="post",
                    titre=_txt(post.get("title", {}).get("rendered", "")),
                    url=url,
                    date=post.get("date", "")[:10] if post.get("date") else "",
                    categories=", ".join(category_names),
                    categories_ids=", ".join(str(c) for c in category_ids),
                    resume=_txt(post.get("content", {}).get("rendered", ""))[:500],
                    score=score,
                    axes=", ".join(sorted(axes)),
                    ia=ia,
                    requetes="",
                )
            
            if len(posts) < 100:
                break
            page_num += 1
            time.sleep(0.5)
    
    return sorted(trouves.values(),
                  key=lambda r: (-r.score, -int(r.date.replace("-", "")) if r.date.isdigit() else 0))


def ecrire(ressources: list[Ressource], outdir: Path) -> None:
    """Écrit les ressources dans des fichiers CSV, JSON et Markdown."""
    outdir.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(Ressource)]
    
    # CSV
    with (outdir / "ecoinfo_ressources.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in ressources:
            w.writerow(asdict(r))
    
    # JSON
    (outdir / "ecoinfo_ressources.json").write_text(
        json.dumps([asdict(r) for r in ressources], ensure_ascii=False, indent=2),
        encoding="utf-8")
    
    # Markdown
    lignes = [
        "| Ressource | Type | Date | Catégories | Axes | IA | Accès |",
        "|---|---|---|---|---|---|---|"
    ]
    for r in ressources:
        titre = r.titre[:100].replace("|", "/")
        lignes.append(
            f"| {titre} | {r.type} | {r.date} | {r.categories} | {r.axes} | "
            f"{'oui' if r.ia else '—'} | [{r.source}]({r.url}) |"
        )
    
    (outdir / "ecoinfo_ressources.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    
    print(f"{len(ressources)} ressources -> {outdir}/ecoinfo_ressources.{{csv,json,md}}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--categories", nargs="+", type=int, default=DEFAULT_CATEGORIES,
                    help="IDs des catégories à scrapper (défaut: IA, ACV, Datacentres, Energie, Mesures, Ecoconception)")
    ap.add_argument("--min-score", type=int, default=3,
                    help="Score minimum pour retenir une ressource (défaut: 3)")
    ap.add_argument("--ia-only", action="store_true",
                    help="Ne garder que les ressources spécifiques à l'IA")
    ap.add_argument("--outdir", type=Path, default=Path("output"))
    ap.add_argument("--use-cache", action="store_true", default=True,
                    help="Utiliser le cache (défaut: oui)")
    ap.add_argument("--clear-cache", action="store_true",
                    help="Effacer le cache avant de commencer")
    args = ap.parse_args()
    
    if args.clear_cache:
        count = clear_cache("ecoinfo")
        print(f"Cache effacé: {count} entrées supprimées", file=sys.stderr)
    
    # Désactiver le cache si demandé
    if not args.use_cache:
        _fetch_posts.cache_ttl = 0
        _fetch_pages.cache_ttl = 0
    
    ressources = collecter_ressources(
        categories=args.categories,
        min_score=args.min_score,
        ia_only=args.ia_only
    )
    ecrire(ressources, args.outdir)
    
    if args.use_cache:
        stats = get_cache_stats()
        print(f"Cache EcoInfo: {stats.get('by_source', {}).get('ecoinfo', 0)} requêtes en cache", file=sys.stderr)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
