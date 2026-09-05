#!/usr/bin/env python3
"""
Même recensement que scrape_hal.py, mais sur arXiv : publications utiles pour
construire un calculateur d'impact environnemental de l'IA (carbone, énergie,
eau, ACV).

API Atom d'arXiv (https://export.arxiv.org/api/query). Pas de clé nécessaire.
arXiv demande au moins 3 secondes entre deux requêtes : c'est le défaut de
--delay, ne le baissez pas.

Le bruit principal d'arXiv sur ce sujet vient de la physique et des modèles
à base d'énergie (*energy-based models*, *free energy*, *dark energy*). Deux
garde-fous : restriction aux catégories cs / eess / stat, et liste NOISE.

Usage :
    python scrape_arxiv.py                     # -> output/arxiv_publications.*
    python scrape_arxiv.py --max-results 200 --pages 3
    python scrape_arxiv.py --from-year 2018 --min-score 4
    python scrape_arxiv.py --validate          # vérifie les papiers de contrôle
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
import time
from dataclasses import dataclass, asdict, fields
from pathlib import Path
from urllib.parse import quote

import requests

API = "https://export.arxiv.org/api/query"
HEADERS = {"User-Agent": "eval-CO2-IA-inventory/1.0 (+recherche empreinte IA)"}

# Catégories retenues. Tout le reste (physique, astro, chimie) est écarté.
CATS = ["cs", "eess", "stat"]

QUERIES = [
    'all:"carbon footprint" AND all:"machine learning"',
    'all:"carbon footprint" AND (all:"language model" OR all:LLM)',
    'all:"carbon emissions" AND (all:training OR all:inference)',
    'all:"energy consumption" AND (all:"deep learning" OR all:"neural network")',
    'all:"energy consumption" AND (all:LLM OR all:"language model")',
    'all:"inference energy" OR all:"training energy"',
    'all:"green AI" OR all:"sustainable AI" OR all:"frugal AI"',
    'all:"environmental impact" AND (all:"artificial intelligence" OR all:"machine learning")',
    'all:"life cycle assessment" AND (all:computing OR all:datacenter OR all:hardware OR all:GPU)',
    'all:"embodied carbon" AND (all:hardware OR all:computing OR all:semiconductor)',
    'all:"water footprint" AND (all:AI OR all:datacenter OR all:"data center")',
    'all:"carbon aware" AND (all:computing OR all:scheduling OR all:datacenter)',
    'all:"carbon intensity" AND (all:electricity OR all:datacenter OR all:cloud)',
    'all:"power consumption" AND all:GPU AND (all:measurement OR all:model)',
    'all:"energy efficiency" AND all:"large language model"',
    'all:"datacenter" AND (all:"energy" OR all:"carbon") AND all:"artificial intelligence"',
    'all:"PUE" AND all:datacenter',
    'all:"sustainability" AND all:"foundation model"',
]

AXES = {
    "carbone": ["carbon", "co2", "co₂", "ghg", "greenhouse", "gwp", "emission",
                "decarbon", "climate"],
    "energie": ["energy", "kwh", "watt", "power consumption", "power draw",
                "electricity", "rapl", "nvml", "joule", "consumption"],
    "eau": ["water", "water footprint", "cooling water", "wue"],
    "acv": ["life cycle", "lca", "embodied", "cradle", "ecoinvent", "footprint",
            "environmental impact", "environmental footprint", "adpe",
            "resource depletion"],
    "methodo": ["method", "measurement", "estimat", "model", "benchmark",
                "framework", "tool", "protocol", "indicator", "profil",
                "calculator", "predict"],
}

IA_TERMS = [
    "machine learning", "deep learning", "neural network", "language model",
    "llm", "gpt", "transformer", "inference", "training", "fine-tuning",
    "foundation model", "generative ai", "artificial intelligence", "nlp",
    "gpu", "tpu", "mlops", "diffusion model",
]

NUM_TERMS = [
    "datacenter", "data center", "cloud", "software", "hpc", "computing",
    "server", "ict", "semiconductor", "cpu", "hardware", "kubernetes",
    "scheduling", "network", "edge",
]

# Le piège d'arXiv : « energy » y désigne aussi une fonction de coût ou une
# grandeur physique, sans aucun rapport avec la consommation électrique.
NOISE = [
    "energy-based model", "energy based model", "free energy", "dark energy",
    "energy landscape", "potential energy", "binding energy", "energy function",
    "high energy physics", "energy spectrum", "kinetic energy", "hamiltonian",
    "energy minimization of the loss", "carbon nanotube", "graphene",
    "carbon capture", "soil carbon", "forest carbon", "carbon fiber",
    "energy market", "energy storage", "battery", "photovoltaic",
    "wind power forecasting", "smart grid", "power system stability",
    "energy harvesting", "wireless power",
]

# Papiers de contrôle : un filtrage correct doit tous les faire remonter.
VALIDATION = {
    "2310.03003": "From Words to Watts (MIT Lincoln Lab)",
    "2311.16863": "Power Hungry Processing (Hugging Face)",
    "2205.09646": "Great Power, Great Responsibility (MIT)",
    "2104.10350": "Carbon Emissions and Large Neural Network Training (Google)",
    "2007.03051": "Carbontracker (Copenhague)",
    "1910.09700": "Quantifying the Carbon Emissions of ML",
    "1906.02243": "Energy and Policy Considerations (Strubell)",
    "2304.03271": "Making AI Less Thirsty (Ren Research Group)",
    "2211.02001": "Carbon Footprint of BLOOM",
    "1907.10597": "Green AI",
}


@dataclass
class Publi:
    arxiv_id: str
    titre: str
    auteurs: str
    annee: str
    categories: str
    url: str
    pdf: str
    doi: str
    resume: str
    score: int
    axes: str
    ia: bool
    requetes: str


def _txt(x: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(x or "")).strip()


def _hay(d: dict) -> str:
    return f"{d['titre']} {d['resume']}".lower()


def evaluer(d: dict) -> tuple[int, list[str], bool]:
    h = _hay(d)
    if any(n in h for n in NOISE):
        return 0, [], False
    axes = [a for a, mots in AXES.items() if any(m in h for m in mots)]
    impact = [a for a in axes if a != "methodo"]
    if not impact:
        return 0, [], False
    ia = any(t in h for t in IA_TERMS)
    num = any(t in h for t in NUM_TERMS)
    if not (ia or num):
        return 0, axes, False
    score = len(impact) + (1 if "methodo" in axes else 0) + (2 if ia else 1)
    return score, axes, ia


def parser(xml: str) -> list[dict]:
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        ident = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", e)
        if not ident:
            continue
        aid = ident.group(1)
        doi = re.search(r'<arxiv:doi[^>]*>([^<]+)</arxiv:doi>', e)
        pdf = re.search(r'<link[^>]*title="pdf"[^>]*href="([^"]+)"', e)
        out.append({
            "arxiv_id": aid,
            "titre": _txt(re.search(r"<title>(.*?)</title>", e, re.S).group(1)),
            "auteurs": "; ".join(re.findall(r"<name>(.*?)</name>", e)[:8]),
            "annee": re.search(r"<published>(\d{4})", e).group(1),
            "categories": ", ".join(re.findall(r'category term="([^"]+)"', e)[:6]),
            "url": f"https://arxiv.org/abs/{aid.split('v')[0]}",
            "pdf": pdf.group(1) if pdf else "",
            "doi": doi.group(1) if doi else "",
            "resume": _txt(re.search(r"<summary>(.*?)</summary>", e, re.S).group(1))[:800],
        })
    return out


def chercher(query: str, maxres: int, pages: int, delay: float) -> list[dict]:
    """Trie par pertinence : un tri par date tronquerait les articles fondateurs,
    tous antérieurs à 2022, sous le flot des préprints récents."""
    cats = " OR ".join(f"cat:{c}.*" for c in CATS)
    q = f"({query}) AND ({cats})"
    out: list[dict] = []
    for page in range(pages):
        url = (f"{API}?search_query={quote(q)}&start={page * maxres}"
               f"&max_results={maxres}&sortBy=relevance&sortOrder=descending")
        for essai in range(3):
            try:
                r = requests.get(url, headers=HEADERS, timeout=90)
            except requests.RequestException as exc:
                print(f"  ! {exc}", file=sys.stderr)
                time.sleep(delay)
                continue
            finally:
                time.sleep(delay)
            if r.status_code == 200:
                lot = parser(r.text)
                out += lot
                if len(lot) < maxres:
                    return out
                break
            print(f"  ! HTTP {r.status_code}, nouvel essai", file=sys.stderr)
    return out


def collecter(queries, maxres, pages, from_year, delay, min_score, ia_only) -> list[Publi]:
    trouves: dict[str, Publi] = {}
    for q in queries:
        docs = chercher(q, maxres, pages, delay)
        gardes = 0
        for d in docs:
            if from_year and int(d["annee"]) < from_year:
                continue
            score, axes, ia = evaluer(d)
            if score < min_score or (ia_only and not ia):
                continue
            base = d["arxiv_id"].split("v")[0]
            if base in trouves:
                reqs = set(trouves[base].requetes.split(" | ")) | {q[:45]}
                trouves[base].requetes = " | ".join(sorted(reqs))
                continue
            gardes += 1
            trouves[base] = Publi(score=score, axes=", ".join(sorted(axes)),
                                  ia=ia, requetes=q[:45], **d)
        print(f"# {len(docs):>4} résultats, +{gardes:<3} retenus — {q[:62]}",
              file=sys.stderr)
    return sorted(trouves.values(),
                  key=lambda p: (-p.score, -int(p.annee)))


def valider(publis: list[Publi]) -> None:
    trouves = {p.arxiv_id.split("v")[0] for p in publis}
    print("\nPapiers de contrôle :", file=sys.stderr)
    manquants = 0
    for aid, nom in VALIDATION.items():
        ok = aid in trouves
        manquants += not ok
        print(f"  {'✓' if ok else '✗'} {aid}  {nom}", file=sys.stderr)
    print(f"  {len(VALIDATION) - manquants}/{len(VALIDATION)} retrouvés",
          file=sys.stderr)


def ecrire(publis: list[Publi], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(Publi)]

    with (outdir / "arxiv_publications.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for p in publis:
            w.writerow(asdict(p))

    (outdir / "arxiv_publications.json").write_text(
        json.dumps([asdict(p) for p in publis], ensure_ascii=False, indent=2),
        encoding="utf-8")

    lignes = ["| Publication | Année | Catégories | Axes | IA | Accès |",
              "|---|---|---|---|---|---|"]
    for p in publis:
        titre = p.titre[:120].replace("|", "/")
        lignes.append(f"| {titre} | {p.annee} | {p.categories} | {p.axes} | "
                      f"{'oui' if p.ia else '—'} | [arXiv]({p.url}) |")
    (outdir / "arxiv_publications.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")

    print(f"{len(publis)} publications -> {outdir}/arxiv_publications.{{csv,json,md}}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", nargs="+", default=QUERIES)
    ap.add_argument("--max-results", type=int, default=200, help="résultats par page")
    ap.add_argument("--pages", type=int, default=2, help="pages par requête")
    ap.add_argument("--from-year", type=int, default=2015)
    ap.add_argument("--delay", type=float, default=3.0,
                    help="arXiv exige 3 s minimum entre deux requêtes")
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument("--ia-only", action="store_true")
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--outdir", type=Path, default=Path("output"))
    args = ap.parse_args()

    publis = collecter(args.queries, args.max_results, args.pages,
                       args.from_year, args.delay, args.min_score, args.ia_only)
    ecrire(publis, args.outdir)
    if args.validate:
        valider(publis)
    return 0


if __name__ == "__main__":
    sys.exit(main())
