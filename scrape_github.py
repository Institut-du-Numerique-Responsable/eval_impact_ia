#!/usr/bin/env python3
"""
Même recensement que scrape_gitlab.py, mais sur GitHub : projets permettant
d'estimer le coût environnemental de l'IA / du numérique (carbone, énergie,
eau, ACV).

API REST GitHub `/search/repositories`. Le token est pris dans cet ordre :
    1. $GITHUB_TOKEN
    2. `gh auth token` (GitHub CLI)
    3. aucun -> 10 requêtes/min seulement, mettre --delay 7

Colonnes de sortie identiques à l'inventaire GitLab, plus `langage` et
`licence`, pour pouvoir concaténer les deux CSV.

Usage :
    python scrape_github.py                    # -> output/github_projets.*
    python scrape_github.py --min-score 3 --ia-only
    python scrape_github.py --pages 2 --delay 2.5
    python scrape_github.py --min-stars 5      # ignorer les dépôts confidentiels
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import time
from dataclasses import dataclass, asdict, fields
from pathlib import Path

import requests

API = "https://api.github.com/search/repositories"

# Mêmes intentions de recherche que sur GitLab, réécrites pour la syntaxe GitHub
# (`in:name,description,topics` évite le bruit du code source).
QUERIES = [
    "carbon footprint AI", "carbon emissions machine learning",
    "llm carbon footprint", "llm energy consumption",
    "ai energy consumption", "gpu energy measurement",
    "inference energy", "training energy consumption",
    "green ai", "sustainable ai", "frugal ai", "green software",
    "carbon aware computing", "carbon intensity api",
    "energy consumption monitoring software", "power consumption rapl",
    "software power meter", "energy profiler",
    "cloud carbon footprint", "datacenter carbon footprint",
    "kubernetes energy consumption", "ci carbon emissions",
    "life cycle assessment hardware", "embodied carbon hardware",
    "environmental impact digital", "empreinte carbone numerique",
    "ecoconception logiciel", "numerique responsable",
    "water footprint datacenter", "pue datacenter",
    "carbon calculator", "co2 emissions estimation",
    "ecoindex", "ecologits", "boavizta", "codecarbon", "scaphandre",
    "green algorithms", "mlco2", "energy efficiency deep learning",
]

AXES = {
    "carbone": ["carbon", "carbone", "co2", "co₂", "ges", "gwp", "greenhouse",
                "emission", "émission", "decarbon"],
    "energie": ["energy", "energie", "énergie", "energetique", "energétique",
                "kwh", "watt", "power", "rapl", "consumption", "consommation",
                "electricit", "électricit"],
    "eau": ["water", " eau", "eau ", "hydric", "hydrique"],
    "acv": ["life cycle", "lca", "acv", "cradle", "embodied", "footprint",
            "empreinte", "environmental impact", "impact environnemental",
            "ecoinvent", "boavizta"],
    "mesure": ["measure", "mesure", "monitor", "metering", "profil", "benchmark",
               "tracker", "tracking", "exporter", "telemetry", "estimat",
               "calculator", "calculateur"],
}

IA_TERMS = [
    " ai ", "ai-", "-ai", "ai)", "(ai", "ia ", " ia", "llm", "gpt",
    "machine learning", "deep learning", "neural network", "inference",
    "inférence", "gpu", "transformer", "nlp", "mlops", "genai",
    "intelligence artificielle", "artificial intelligence", "pytorch",
    "tensorflow", "hugging face", "ml ",
]

NUM_TERMS = [
    "software", "logiciel", "web", "site", "cloud", "server", "serveur",
    "cpu", "code", "app", "api", "numerique", "numérique", "digital",
    "hardware", "device", "datacenter", "data center", "kubernetes",
    "compute", "hpc", "runner", "pipeline", "container", "docker", "ci/cd",
]

NOISE = [
    "nanotube", "radiocarbon", "carbon fiber", "carbon fibre", "graphene",
    "carbon capture", "biochar", "peatland", "soil organic carbon",
    "carbon black", "photosynth", "blue/green", "blue-green", "greenwich",
    "greenhouse gas inventory of agriculture", "minecraft", "carbon design system",
    "carbon language", "carbonyl", "free energy perturbation", "wind turbine",
    "solar panel", "photovoltaic", "smart meter home", "battery management",
]


@dataclass
class Projet:
    plateforme: str
    chemin: str
    url: str
    nom: str
    description: str
    etoiles: int
    forks: int
    derniere_activite: str
    archive: bool
    langage: str
    licence: str
    topics: str
    score: int
    axes: str
    ia: bool
    requetes: str


def token() -> str | None:
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        return tok
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True,
                             text=True, timeout=10)
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        pass
    return None


def _hay(r: dict) -> str:
    return " ".join([
        r.get("name") or "",
        r.get("full_name") or "",
        r.get("description") or "",
        " ".join(r.get("topics") or []),
    ]).lower()


def evaluer(r: dict) -> tuple[int, list[str], bool]:
    h = _hay(r)
    if any(n in h for n in NOISE):
        return 0, [], False
    axes = [a for a, mots in AXES.items() if any(m in h for m in mots)]
    impact = [a for a in axes if a != "mesure"]
    if not impact:
        return 0, [], False
    ia = any(t in h for t in IA_TERMS)
    num = any(t in h for t in NUM_TERMS)
    score = len(impact) + (1 if "mesure" in axes else 0) + (2 if ia else (1 if num else 0))
    if not (ia or num):
        score -= 1
    return score, axes, ia


def chercher(query: str, pages: int, delay: float, tok: str | None,
             min_stars: int) -> list[dict]:
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "eval-CO2-IA-inventory/1.0"}
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    q = f"{query} in:name,description,topics"
    if min_stars:
        q += f" stars:>={min_stars}"
    out: list[dict] = []
    for page in range(1, pages + 1):
        params = {"q": q, "sort": "stars", "order": "desc",
                  "per_page": 100, "page": page}
        try:
            r = requests.get(API, headers=headers, params=params, timeout=30)
        except requests.RequestException as exc:
            print(f"  ! [{query}] {exc}", file=sys.stderr)
            return out
        finally:
            time.sleep(delay)
        if r.status_code == 403 and "rate limit" in r.text.lower():
            reset = int(r.headers.get("x-ratelimit-reset", 0)) - int(time.time())
            attente = max(reset + 2, 15)
            print(f"  … rate limit, pause {attente}s", file=sys.stderr)
            time.sleep(attente)
            continue
        if r.status_code != 200:
            print(f"  ! [{query}] HTTP {r.status_code}", file=sys.stderr)
            return out
        items = r.json().get("items", [])
        out += items
        if len(items) < 100:
            break
    return out


def collecter(queries, pages, delay, tok, min_score, ia_only,
              min_stars) -> list[Projet]:
    trouves: dict[str, Projet] = {}
    for q in queries:
        items = chercher(q, pages, delay, tok, min_stars)
        gardes = 0
        for r in items:
            score, axes, ia = evaluer(r)
            if score < min_score or (ia_only and not ia):
                continue
            cle = r["full_name"]
            if cle in trouves:
                reqs = set(trouves[cle].requetes.split(" | ")) | {q}
                trouves[cle].requetes = " | ".join(sorted(reqs))
                continue
            gardes += 1
            lic = (r.get("license") or {})
            trouves[cle] = Projet(
                plateforme="github.com",
                chemin=cle,
                url=r["html_url"],
                nom=r["name"],
                description=(r.get("description") or "").replace("\n", " ").strip(),
                etoiles=r.get("stargazers_count", 0),
                forks=r.get("forks_count", 0),
                derniere_activite=(r.get("pushed_at") or "")[:10],
                archive=bool(r.get("archived")),
                langage=r.get("language") or "",
                licence=lic.get("spdx_id") or "",
                topics=", ".join(r.get("topics") or []),
                score=score,
                axes=", ".join(sorted(axes)),
                ia=ia,
                requetes=q,
            )
        print(f"# {len(items):>4} résultats, +{gardes:<3} retenus — {q}",
              file=sys.stderr)
    return sorted(trouves.values(),
                  key=lambda p: (-p.score, -p.etoiles, p.derniere_activite))


def ecrire(projets: list[Projet], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(Projet)]

    with (outdir / "github_projets.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for p in projets:
            w.writerow(asdict(p))

    (outdir / "github_projets.json").write_text(
        json.dumps([asdict(p) for p in projets], ensure_ascii=False, indent=2),
        encoding="utf-8")

    lignes = ["| Projet | Axes | IA | ⭐ | Langage | Licence | Activité | Description |",
              "|---|---|---|---:|---|---|---|---|"]
    for p in projets:
        desc = p.description[:140].replace("|", "/")
        lignes.append(f"| [{p.chemin}]({p.url}) | {p.axes} | {'oui' if p.ia else '—'} | "
                      f"{p.etoiles} | {p.langage} | {p.licence} | "
                      f"{p.derniere_activite} | {desc} |")
    (outdir / "github_projets.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")

    print(f"{len(projets)} projets -> {outdir}/github_projets.{{csv,json,md}}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", nargs="+", default=QUERIES)
    ap.add_argument("--pages", type=int, default=1, help="pages de 100 résultats")
    ap.add_argument("--delay", type=float, default=2.5,
                    help="délai entre requêtes (7 si pas de token)")
    ap.add_argument("--min-score", type=int, default=2)
    ap.add_argument("--min-stars", type=int, default=0)
    ap.add_argument("--ia-only", action="store_true")
    ap.add_argument("--outdir", type=Path, default=Path("output"))
    args = ap.parse_args()

    tok = token()
    print(f"token : {'oui' if tok else 'non (10 req/min)'}", file=sys.stderr)
    projets = collecter(args.queries, args.pages, args.delay, tok,
                        args.min_score, args.ia_only, args.min_stars)
    ecrire(projets, args.outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
