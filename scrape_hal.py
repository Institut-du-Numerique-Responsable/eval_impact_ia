#!/usr/bin/env python3
"""
Recense dans HAL (archives-ouvertes.fr) les publications utiles pour construire
un calculateur d'impact environnemental de l'IA : méthodo de mesure d'énergie,
facteurs d'émission, ACV du matériel, empreinte eau des datacenters, etc.

API publique HAL (Solr) : https://api.archives-ouvertes.fr/search/
Pas de clé nécessaire, pas de scraping HTML.

Pour chaque publication retenue :
    hal_id, titre, auteurs, annee, type, revue/conf, doi, url_hal, url_pdf,
    mots_cles, resume (tronqué), score, axes, ia, requetes

Usage :
    python scrape_hal.py                        # -> output/hal_publications.*
    python scrape_hal.py --ia-only --min-score 3
    python scrape_hal.py --from-year 2018 --rows 100
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

API = "https://api.archives-ouvertes.fr/search/"
HEADERS = {"User-Agent": "eval-CO2-IA-inventory/1.0 (+recherche empreinte IA)"}

FIELDS = ",".join([
    "halId_s", "title_s", "subTitle_s", "authFullName_s", "producedDateY_i",
    "docType_s", "journalTitle_s", "conferenceTitle_s", "doiId_s", "uri_s",
    "fileMain_s", "keyword_s", "abstract_s", "language_s",
])

# Requêtes Solr : croisement (impact environnemental) x (IA / numérique).
QUERIES = [
    '(carbon OR CO2 OR "greenhouse gas" OR carbone) AND ("machine learning" OR "deep learning" OR "artificial intelligence" OR LLM)',
    '("energy consumption" OR "consommation énergétique") AND ("deep learning" OR "neural network" OR LLM OR inference)',
    '("empreinte carbone" OR "impact environnemental") AND ("intelligence artificielle" OR "apprentissage automatique")',
    '("water footprint" OR "water consumption" OR "empreinte eau") AND (datacenter OR "data center" OR AI OR cloud)',
    '("life cycle assessment" OR "analyse de cycle de vie" OR ACV) AND (datacenter OR "data center" OR ICT OR numérique OR GPU OR server)',
    '("green AI" OR "sustainable AI" OR "frugal AI" OR "IA frugale" OR "sobriété numérique")',
    '("energy measurement" OR "power measurement" OR RAPL OR powermeter OR "software power model") AND (CPU OR GPU OR server OR container)',
    '("carbon footprint" OR "carbon intensity") AND (cloud OR datacenter OR HPC OR "high performance computing")',
    '("environmental impact" OR "environmental footprint") AND (ICT OR "information technology" OR software OR numérique)',
    '("emission factor" OR "facteur d\'émission") AND (electricity OR électricité) AND (numérique OR ICT OR datacenter OR computing)',
    '(training OR inference) AND (GPU OR TPU) AND (energy OR watt OR kWh)',
    '("écoconception" OR "éco-conception") AND (logiciel OR numérique OR service OR web)',
    '(LCA OR "life cycle") AND (semiconductor OR "integrated circuit" OR wafer OR "embodied carbon")',
    '("PUE" OR "power usage effectiveness") AND datacenter',
]

AXES = {
    "carbone": ["carbon", "carbone", "co2", "co₂", "ges", "greenhouse", "gwp",
                "emission", "émission", "decarbon", "climate"],
    "energie": ["energy", "énergie", "energie", "energétique", "energetique",
                "kwh", "watt", "power", "electricit", "électricit", "rapl",
                "consumption", "consommation"],
    "eau": ["water", "eau", "hydric", "hydrique", "water footprint"],
    "acv": ["life cycle", "lca", "acv", "cycle de vie", "embodied", "cradle",
            "ecoinvent", "footprint", "empreinte", "environmental impact",
            "impact environnemental"],
    "methodo": ["method", "méthode", "measurement", "mesure", "model", "modèle",
                "estimation", "benchmark", "framework", "tool", "outil",
                "protocol", "protocole", "indicator", "indicateur"],
}

IA_TERMS = [
    "machine learning", "deep learning", "apprentissage automatique",
    "artificial intelligence", "intelligence artificielle", "llm",
    "large language model", "neural network", "réseau de neurones",
    "inference", "inférence", "training", "entraînement", "transformer",
    "genai", "generative ai", "ia générative", " ai ", "gpu", "nlp",
]

NUM_TERMS = [
    "datacenter", "data center", "cloud", "software", "logiciel", "hpc",
    "computing", "server", "serveur", "ict", "numérique", "numerique",
    "digital", "web", "semiconductor", "cpu", "hardware", "network",
]

NOISE = [
    "soil organic carbon", "carbone du sol", "forest carbon", "ocean carbon",
    "carbon nanotube", "carbon fiber", "carbon fibre", "radiocarbon",
    "carbon capture", "photosynth", "biochar", "peatland", "carbon cycle",
    "dissolved organic carbon", "carbon steel", "graphene",
]


@dataclass
class Publi:
    hal_id: str
    titre: str
    auteurs: str
    annee: str
    type_doc: str
    support: str
    doi: str
    url_hal: str
    url_pdf: str
    mots_cles: str
    resume: str
    score: int
    axes: str
    ia: bool
    requetes: str


def _clean(txt: str) -> str:
    txt = re.sub(r"<[^>]+>", " ", txt or "")
    return re.sub(r"\s+", " ", txt).strip()


def _hay(d: dict) -> str:
    return " ".join([
        " ".join(d.get("title_s") or []),
        " ".join(d.get("keyword_s") or []),
        " ".join(d.get("abstract_s") or [])[:1500],
        d.get("journalTitle_s") or "",
        d.get("conferenceTitle_s") or "",
    ]).lower()


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


def chercher(query: str, rows: int, from_year: int, delay: float) -> list[dict]:
    q = f"({query})"
    params = (f"q={quote(q)}&fl={FIELDS}&rows={rows}&wt=json"
              f"&sort=producedDateY_i%20desc")
    if from_year:
        params += f"&fq=producedDateY_i:[{from_year}%20TO%20*]"
    try:
        r = requests.get(f"{API}?{params}", headers=HEADERS, timeout=60)
    except requests.RequestException as exc:
        print(f"  ! {query[:50]}… : {exc}", file=sys.stderr)
        return []
    finally:
        time.sleep(delay)
    if r.status_code != 200:
        print(f"  ! {query[:50]}… : HTTP {r.status_code}", file=sys.stderr)
        return []
    return r.json().get("response", {}).get("docs", [])


def collecter(queries, rows, from_year, delay, min_score, ia_only) -> list[Publi]:
    trouves: dict[str, Publi] = {}
    for q in queries:
        docs = chercher(q, rows, from_year, delay)
        print(f"# {len(docs):>4} résultats — {q[:70]}…", file=sys.stderr)
        for d in docs:
            score, axes, ia = evaluer(d)
            if score < min_score or (ia_only and not ia):
                continue
            hid = d.get("halId_s") or d.get("uri_s", "")
            if hid in trouves:
                reqs = set(trouves[hid].requetes.split(" | ")) | {q[:40]}
                trouves[hid].requetes = " | ".join(sorted(reqs))
                continue
            trouves[hid] = Publi(
                hal_id=hid,
                titre=_clean(" ".join(d.get("title_s") or [])),
                auteurs="; ".join((d.get("authFullName_s") or [])[:8]),
                annee=str(d.get("producedDateY_i") or ""),
                type_doc=d.get("docType_s") or "",
                support=d.get("journalTitle_s") or d.get("conferenceTitle_s") or "",
                doi=d.get("doiId_s") or "",
                url_hal=d.get("uri_s") or "",
                url_pdf=d.get("fileMain_s") or "",
                mots_cles=", ".join((d.get("keyword_s") or [])[:12]),
                resume=_clean(" ".join(d.get("abstract_s") or []))[:600],
                score=score,
                axes=", ".join(sorted(axes)),
                ia=ia,
                requetes=q[:40],
            )
    return sorted(trouves.values(),
                  key=lambda p: (-p.score, -(int(p.annee) if p.annee.isdigit() else 0)))


def ecrire(publis: list[Publi], outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(Publi)]

    with (outdir / "hal_publications.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for p in publis:
            w.writerow(asdict(p))

    (outdir / "hal_publications.json").write_text(
        json.dumps([asdict(p) for p in publis], ensure_ascii=False, indent=2),
        encoding="utf-8")

    lignes = ["| Publication | Année | Type | Axes | IA | Accès |", "|---|---|---|---|---|---|"]
    for p in publis:
        titre = p.titre[:120].replace("|", "/")
        acces = f"[HAL]({p.url_hal})" + (f" · [PDF]({p.url_pdf})" if p.url_pdf else "")
        lignes.append(f"| {titre} | {p.annee} | {p.type_doc} | {p.axes} | "
                      f"{'oui' if p.ia else '—'} | {acces} |")
    (outdir / "hal_publications.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")

    print(f"{len(publis)} publications -> {outdir}/hal_publications.{{csv,json,md}}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queries", nargs="+", default=QUERIES)
    ap.add_argument("--rows", type=int, default=60, help="résultats par requête")
    ap.add_argument("--from-year", type=int, default=2015)
    ap.add_argument("--delay", type=float, default=0.5)
    ap.add_argument("--min-score", type=int, default=3)
    ap.add_argument("--ia-only", action="store_true")
    ap.add_argument("--outdir", type=Path, default=Path("output"))
    args = ap.parse_args()

    publis = collecter(args.queries, args.rows, args.from_year, args.delay,
                       args.min_score, args.ia_only)
    ecrire(publis, args.outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
