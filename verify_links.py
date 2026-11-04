#!/usr/bin/env python3
"""
Vérifie que tous les liens du README.md sont valides (HTTP 200, 202, 203 ou 403).
Les liens en 403 sont considérés valides car certains sites bloquent les requêtes automatisées.

Usage:
    python verify_links.py
    python verify_links.py --readonly README.md
    python verify_links.py --timeout 10
    python verify_links.py --ignore-pattern "github.com|gitlab.com"
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Tuple
from urllib.parse import urlparse

import requests

# User-Agent personnalisé pour éviter les blocages
HEADERS = {
    "User-Agent": "eval-CO2-IA-link-checker/1.0 (+https://github.com/Institut-du-Numerique-Responsable/eval_impact_ia)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

# Délai entre les requêtes pour éviter d'être bloqué
REQUEST_DELAY = 0.1

# Timeout par défaut pour les requêtes
DEFAULT_TIMEOUT = 15

# Codes HTTP considérés comme valides
VALID_STATUS_CODES = {200, 202, 203, 204, 403, 405}

# Domains connus pour bloquer les requêtes automatisées (403 acceptable)
KNOWN_BLOCKING_DOMAINS = {
    "mdpi.com",
    "tandfonline.com", 
    "microsoft.com",
    "springer.com",
    "ieee.org",
    "acm.org",
    "sciencedirect.com",
    "nature.com",
}


def extraire_liens(markdown_text: str) -> list[str]:
    """Extrait tous les liens Markdown du texte."""
    # Pattern pour les liens Markdown: [texte](url)
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    matches = re.findall(pattern, markdown_text)
    
    # Retourner uniquement les URLs (deuxième groupe de capture)
    urls = [url for _, url in matches]
    
    # Nettoyer les URLs (enlever les ancres, etc.)
    cleaned_urls = []
    for url in urls:
        # Supprimer les ancres et les fragments
        parsed = urlparse(url)
        if parsed.scheme and parsed.netloc:
            # Reconstruire l'URL sans fragment
            clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
            if parsed.query:
                clean_url += f"?{parsed.query}"
            cleaned_urls.append(clean_url)
    
    return cleaned_urls


def is_blocking_domain(url: str) -> bool:
    """Vérifie si l'URL appartient à un domaine connu pour bloquer les requêtes."""
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    
    for blocking_domain in KNOWN_BLOCKING_DOMAINS:
        if blocking_domain in domain:
            return True
    return False


def verifier_lien(url: str, timeout: int = DEFAULT_TIMEOUT) -> Tuple[str, int, str]:
    """
    Vérifie un lien unique.
    Retourne (url, status_code, raison)
    """
    try:
        # Vérifier si c'est un domaine bloquant
        if is_blocking_domain(url):
            return (url, 403, "Domain bloque les requêtes automatisées (403 acceptable)")
        
        # Configurer la timeout
        r = requests.head(url, headers=HEADERS, timeout=timeout, allow_redirects=True)
        
        # Si HEAD n'est pas autorisé, essayer GET
        if r.status_code == 405:
            r = requests.get(url, headers=HEADERS, timeout=timeout, stream=True)
            r.close()
        
        return (url, r.status_code, "")
        
    except requests.exceptions.SSLError as e:
        return (url, 0, f"Erreur SSL: {str(e)}")
    except requests.exceptions.ConnectionError as e:
        return (url, 0, f"Erreur de connexion: {str(e)}")
    except requests.exceptions.Timeout as e:
        return (url, 0, f"Timeout: {str(e)}")
    except requests.exceptions.TooManyRedirects as e:
        return (url, 0, f"Trop de redirections: {str(e)}")
    except requests.exceptions.RequestException as e:
        return (url, 0, f"Erreur: {str(e)}")


def verifier_tous_liens(urls: list[str], timeout: int = DEFAULT_TIMEOUT, max_workers: int = 10) -> dict[str, Tuple[int, str]]:
    """Vérifie tous les liens en parallèle."""
    results = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Soumettre toutes les tâches
        future_to_url = {
            executor.submit(verifier_lien, url, timeout): url 
            for url in urls
        }
        
        # Collecter les résultats
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, status_code, raison = future.result()
                results[url] = (status_code, raison)
            except Exception as e:
                results[url] = (0, str(e))
            
            time.sleep(REQUEST_DELAY)  # Respecter le délai entre les requêtes
    
    return results


def afficher_rapport(results: dict[str, Tuple[int, str]]) -> Tuple[int, int, int]:
    """Affiche un rapport des liens vérifiés et retourne (total, valides, invalides)."""
    total = len(results)
    valides = 0
    invalides = 0
    
    print(f"\n{'='*80}")
    print(f"RAPPORT DE VÉRIFICATION DES LIENS")
    print(f"{'='*80}")
    print(f"Total des liens vérifiés: {total}")
    print()
    
    # Trier par code de status
    liens_valides = []
    liens_invalides = []
    liens_avertissements = []
    
    for url, (status, raison) in results.items():
        if status in VALID_STATUS_CODES:
            if status == 403:
                liens_avertissements.append((url, status, raison))
            else:
                liens_valides.append((url, status, raison))
            valides += 1
        else:
            liens_invalides.append((url, status, raison))
            invalides += 1
    
    print(f"✓ Valides: {valides}")
    print(f"⚠ Avertissements (403): {len(liens_avertissements)}")
    print(f"✗ Invalides: {invalides}")
    print()
    
    # Afficher les liens invalides
    if liens_invalides:
        print(f"LIENS INVALIDES:")
        print("-" * 80)
        for url, status, raison in sorted(liens_invalides, key=lambda x: x[1]):
            print(f"  ✗ {url}")
            if raison:
                print(f"    Code: {status}, Raison: {raison}")
            else:
                print(f"    Code: {status}")
        print()
    
    # Afficher les avertissements
    if liens_avertissements:
        print(f"LIENS AVEC AVERTISSEMENTS (403 - domaine bloquant):")
        print("-" * 80)
        for url, status, raison in sorted(liens_avertissements):
            print(f"  ⚠ {url}")
            print(f"    Code: {status}, Raison: {raison}")
        print()
    
    # Afficher un échantillon des liens valides
    if liens_valides:
        print(f"EXEMPLES DE LIENS VALIDES:")
        print("-" * 80)
        for url, status, _ in liens_valides[:5]:
            print(f"  ✓ {url} (HTTP {status})")
        if len(liens_valides) > 5:
            print(f"  ... et {len(liens_valides) - 5} autres")
        print()
    
    return total, valides, invalides


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--readonly",
        type=Path,
        default=Path("README.md"),
        help="Fichier Markdown à vérifier (défaut: README.md)"
    )
    ap.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Timeout en secondes pour chaque requête (défaut: {DEFAULT_TIMEOUT})"
    )
    ap.add_argument(
        "--max-workers",
        type=int,
        default=10,
        help="Nombre maximum de requêtes simultanées (défaut: 10)"
    )
    ap.add_argument(
        "--ignore-pattern",
        type=str,
        default=None,
        help="Pattern regex pour ignorer certains liens"
    )
    ap.add_argument(
        "--quiet",
        action="store_true",
        help="N'affiche que les liens invalides"
    )
    args = ap.parse_args()
    
    # Lire le fichier Markdown
    if not args.readonly.exists():
        print(f"Erreur: {args.readonly} n'existe pas", file=sys.stderr)
        return 1
    
    markdown_content = args.readonly.read_text(encoding="utf-8")
    
    # Extraire les liens
    urls = extraire_liens(markdown_content)
    
    if not urls:
        print("Aucun lien trouvé dans le fichier.")
        return 0
    
    print(f"Trouvé {len(urls)} liens dans {args.readonly}")
    
    # Filtrer par pattern d'ignorance
    if args.ignore_pattern:
        pattern = re.compile(args.ignore_pattern)
        urls = [url for url in urls if not pattern.search(url)]
        print(f"Filtré à {len(urls)} liens après application du pattern d'ignorance")
    
    # Vérifier tous les liens
    print("Vérification en cours...")
    results = verifier_tous_liens(urls, timeout=args.timeout, max_workers=args.max_workers)
    
    # Afficher le rapport
    if args.quiet:
        # N'afficher que les liens invalides
        invalides = [(url, status, raison) for url, (status, raison) in results.items() 
                    if status not in VALID_STATUS_CODES]
        if invalides:
            print(f"\nLIENS INVALIDES ({len(invalides)}):")
            for url, status, raison in invalides:
                print(f"  ✗ {url} (Code: {status}, Raison: {raison})")
            return 1
        else:
            print("Tous les liens sont valides!")
            return 0
    else:
        total, valides, invalides = afficher_rapport(results)
        
        if invalides > 0:
            print(f"\n❌ VÉRIFICATION ÉCHOUÉE: {invalides} liens invalides trouvés")
            return 1
        else:
            print(f"\n✅ VÉRIFICATION RÉUSSIE: Tous les liens sont valides!")
            return 0


if __name__ == "__main__":
    sys.exit(main())
