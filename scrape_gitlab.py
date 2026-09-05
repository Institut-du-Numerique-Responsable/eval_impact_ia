#!/usr/bin/env python3
"""
Recense sur GitLab (gitlab.com + forges auto-hébergées) les projets qui
permettent d'estimer le coût environnemental de l'IA / du numérique :
carbone (CO2e), énergie (kWh), eau, ou plus largement ACV du numérique.

Même logique que ~/projects/lucie-scraper, mais on interroge l'API REST
publique de GitLab (`/api/v4/projects?search=...`) plutôt que de scraper du
HTML : pas de clé nécessaire pour les projets publics.

Pour chaque projet retenu :
    - instance, chemin, url, description
    - etoiles, forks, derniere_activite, archive
    - topics
    - score       (pertinence calculée sur nom + description + topics)
    - axes        (carbone / energie / eau / acv / mesure)
    - ia          (True si le projet cible explicitement IA/LLM/GPU/ML)
    - requetes    (mots-clés qui l'ont fait remonter)

Usage :
    python scrape_gitlab.py                      # tout, -> output/*.csv|json
    python scrape_gitlab.py --instances gitlab.com framagit.org
    python scrape_gitlab.py --min-score 3        # filtre plus strict
    python scrape_gitlab.py --ia-only            # uniquement projets IA
    python scrape_gitlab.py --delay 0.5 --outdir ./resultats
    GITLAB_TOKEN=xxx python scrape_gitlab.py     # + projets privés visibles
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from dataclasses import dataclass, asdict, fields
from pathlib import Path
from urllib.parse import quote

import requests

HEADERS = {"User-Agent": "eval-CO2-IA-inventory/1.0 (+recherche outils empreinte IA)"}

# Forges GitLab interrogées. L'API /projects est ouverte en anonyme sur toutes.
INSTANCES = [
    "gitlab.com",
    "framagit.org",
    "gitlab.inria.fr",
    "gitlab.in2p3.fr",
    "forge.apps.education.fr",
    "gitlab.ow2.org",
    "gitlab.univ-lille.fr",
    "gitlab.irit.fr",
    "gitlab.imt-atlantique.fr",
    "gitlab.huma-num.fr",
    "gricad-gitlab.univ-grenoble-alpes.fr",
    "plmlab.math.cnrs.fr",
]

# Requêtes envoyées à l'API (FR + EN). GitLab cherche dans nom, chemin et description.
QUERIES = [
    "carbon footprint", "empreinte carbone", "carbon emissions", "co2 emissions",
    "carbon aware", "carbon intensity", "carbon tracker", "codecarbon",
    "energy consumption", "consommation energetique", "energy measurement",
    "power consumption", "energy meter", "rapl", "scaphandre", "powerapi", "kepler",
    "gpu energy", "llm energy", "inference energy", "model energy", "training energy",
    "green ai", "sustainable ai", "frugal ai", "ia frugale", "impact ia",
    "green it", "greenit", "numerique responsable", "sobriete numerique",
    "ecoconception", "eco-conception", "ecoindex", "ecologits", "boavizta",
    "life cycle assessment", "acv numerique", "environmental impact",
    "impact environnemental", "empreinte environnementale", "empreinte numerique",
    "water footprint", "empreinte eau", "datacenter water", "pue datacenter",
    "green algorithms", "mlco2", "ges numerique", "bilan carbone", "ecodiag",
]

# --- Scoring -----------------------------------------------------------------
# Un projet est retenu s'il touche au moins un "axe impact".
AXES = {
    "carbone": ["carbon", "carbone", "co2", "co₂", "ges", "gwp", "greenhouse",
                "emission", "émission", "bilan carbone", "decarbon"],
    "energie": ["energy", "energie", "énergie", "energétique", "energetique",
                "kwh", "watt", "power consumption", "powermeter", "rapl",
                "consumption", "consommation", "electricit", "electricity"],
    "eau": ["water", "eau ", " eau", "hydric", "hydrique", "water footprint"],
    "acv": ["life cycle", "lca", "acv", "cradle", "manufacturing impact",
            "embodied", "footprint", "empreinte", "environmental impact",
            "impact environnemental", "ecoinvent", "boavizta"],
    "mesure": ["measure", "mesure", "monitor", "metering", "profil", "benchmark",
               "tracker", "tracking", "exporter", "telemetry", "sensor"],
}

# Termes qui rattachent le projet au périmètre IA / calcul.
IA_TERMS = [
    " ai ", "ai-", "-ai", "ia ", " ia", "llm", "gpt", "machine learning",
    "deep learning", "neural network", "inference", "inférence", "gpu",
    "transformer", "nlp", "mlops", "genai", "intelligence artificielle",
    "artificial intelligence", "pytorch", "tensorflow", "hugging face",
]

# Termes qui rattachent au périmètre numérique (utile en repli).
NUM_TERMS = [
    "software", "logiciel", "web", "site", "ci/cd", "ci ", "cloud", "server",
    "serveur", "cpu", "gpu", "code", "app", "api", "numerique", "numérique",
    "digital", "it ", " it", "hardware", "device", "terminal",
    "datacenter", "data center", "kubernetes", "compute", "hpc", "runner",
    "pipeline", "container", "docker", "vm ", "model", "modèle",
]

# Bruit fréquent : physique des particules, chimie, biologie, réseaux électriques…
NOISE = [
    "nanotube", "radiocarbon", "14c", "gibbs", "adsorption", "docking",
    "spiking", "monte carlo event", "high-energy physics", "particle",
    "photosynthetic", "greenhouse ontology", "greenhouse gas emissions of soil",
    "blue/green", "blue-green", "greenwich", "greentooth", "greenaddress",
    "green screen", "greenpepper", "lineage 2", "genshin", "chromium based",
    "carbonos", "wordpress development environment", "free energy", "oscillator",
    "geomagnetic", "tsunami", "coral", "hydrologic", "battery charge",
    "photovoltaic", "wind turbine", "smart meter", "dsmr", "growatt",
]


@dataclass
class Projet:
    instance: str
    chemin: str
    url: str
    nom: str
    description: str
    etoiles: int
    forks: int
    derniere_activite: str
    archive: bool
    topics: str
    score: int
    axes: str
    ia: bool
    requetes: str


def _hay(p: dict) -> str:
    return " ".join([
        p.get("name") or "",
        p.get("path_with_namespace") or "",
        p.get("description") or "",
        " ".join(p.get("topics") or []),
    ]).lower()


def evaluer(p: dict) -> tuple[int, list[str], bool]:
    """Retourne (score, axes touchés, cible_ia)."""
    h = _hay(p)
    if any(n in h for n in NOISE):
        return 0, [], False

    axes = [axe for axe, mots in AXES.items() if any(m in h for m in mots)]
    impact = [a for a in axes if a != "mesure"]
    if not impact:
        return 0, [], False

    ia = any(t in h for t in IA_TERMS)
    num = any(t in h for t in NUM_TERMS)

    score = len(impact)                    # 1 pt par axe d'impact
    score += 1 if "mesure" in axes else 0  # outil de mesure/estimation
    score += 2 if ia else (1 if num else 0)
    if not (ia or num):                    # impact hors périmètre numérique
        score -= 1
    return score, axes, ia


def chercher(instance: str, query: str, delay: float, token: str | None) -> list[dict]:
    url = (f"https://{instance}/api/v4/projects"
           f"?search={quote(query)}&per_page=100&order_by=star_count&sort=desc"
           f"&simple=false")
    headers = dict(HEADERS)
    if token:
        headers["PRIVATE-TOKEN"] = token
    try:
        r = requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as exc:
        print(f"  ! {instance} [{query}] : {exc}", file=sys.stderr)
        return []
    finally:
        time.sleep(delay)
    if r.status_code != 200:
        print(f"  ! {instance} [{query}] : HTTP {r.status_code}", file=sys.stderr)
        return []
    try:
        data = r.json()
    except ValueError:
        return []
    return data if isinstance(data, list) else []


def collecter(instances, queries, delay, token, min_score, ia_only) -> list[Projet]:
    trouves: dict[str, Projet] = {}
    for inst in instances:
        print(f"# {inst}", file=sys.stderr)
        for q in queries:
            for p in chercher(inst, q, delay, token):
                score, axes, ia = evaluer(p)
                if score < min_score or (ia_only and not ia):
                    continue
                cle = f"{inst}/{p['path_with_namespace']}"
                if cle in trouves:
                    reqs = set(trouves[cle].requetes.split(" | ")) | {q}
                    trouves[cle].requetes = " | ".join(sorted(reqs))
                    continue
                trouves[cle] = Projet(
                    instance=inst,
                    chemin=p["path_with_namespace"],
                    url=p["web_url"],
                    nom=p["name"],
                    description=(p.get("description") or "").replace("\n", " ").strip(),
                    etoiles=p.get("star_count", 0),
                    forks=p.get("forks_count", 0),
                    derniere_activite=(p.get("last_activity_at") or "")[:10],
                    archive=bool(p.get("archived")),
                    topics=", ".join(p.get("topics") or []),
                    score=score,
                    axes=", ".join(sorted(axes)),
                    ia=ia,
                    requetes=q,
                )
        print(f"  -> {len(trouves)} projets retenus cumulés", file=sys.stderr)
    return sorted(trouves.values(),
                  key=lambda x: (-x.score, -x.etoiles, x.derniere_activite))


def ecrire(projets: list[Projet], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(Projet)]

    csv_path = outdir / "gitlab_projets.csv"
    with csv_path.open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for p in projets:
            w.writerow(asdict(p))

    json_path = outdir / "gitlab_projets.json"
    json_path.write_text(
        json.dumps([asdict(p) for p in projets], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md_path = outdir / "gitlab_projets.md"
    lignes = ["| Projet | Instance | Axes | IA | ⭐ | Activité | Description |",
              "|---|---|---|---|---:|---|---|"]
    for p in projets:
        desc = p.description[:140].replace("|", "/")
        lignes.append(f"| [{p.chemin}]({p.url}) | {p.instance} | {p.axes} | "
                      f"{'oui' if p.ia else '—'} | {p.etoiles} | "
                      f"{p.derniere_activite} | {desc} |")
    md_path.write_text("\n".join(lignes) + "\n", encoding="utf-8")

    print(f"{len(projets)} projets -> {csv_path}, {json_path}, {md_path}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--instances", nargs="+", default=INSTANCES)
    ap.add_argument("--queries", nargs="+", default=QUERIES)
    ap.add_argument("--delay", type=float, default=0.3,
                    help="délai entre requêtes API (défaut 0.3s)")
    ap.add_argument("--min-score", type=int, default=2)
    ap.add_argument("--ia-only", action="store_true")
    ap.add_argument("--outdir", type=Path, default=Path("output"))
    args = ap.parse_args()

    projets = collecter(args.instances, args.queries, args.delay,
                        os.environ.get("GITLAB_TOKEN"),
                        args.min_score, args.ia_only)
    ecrire(projets, args.outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
