#!/usr/bin/env python3
"""
Module de cache pour les requêtes API des scrapers.
Stocke les réponses dans des fichiers JSON pour éviter de refaire les mêmes requêtes.

Usage:
    from scrape_cache import get_cached, cache_response
    
    # Vérifier si une réponse est en cache
    cached = get_cached("arxiv", "query_hash")
    if cached:
        return cached
    
    # Stocker une réponse en cache
    cache_response("arxiv", "query_hash", response_text, expires_in=86400)
    
    # Utiliser comme décorateur
    @cached_request("arxiv", timeout=30)
    def ma_fonction_de_scraping():
        ...
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from functools import wraps
from pathlib import Path
from typing import Any, Callable

# Dossier de cache par défaut
DEFAULT_CACHE_DIR = Path(".cache")

# Durée de vie par défaut du cache (en secondes) : 24h
DEFAULT_CACHE_TTL = 86400


def get_cache_dir(cache_dir: Path | str | None = None) -> Path:
    """Retourne le dossier de cache, en le créant si nécessaire."""
    if cache_dir is None:
        cache_dir = DEFAULT_CACHE_DIR
    else:
        cache_dir = Path(cache_dir)
    
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def get_cache_path(source: str, query_hash: str, cache_dir: Path | None = None) -> Path:
    """Retourne le chemin du fichier de cache pour une requête."""
    cache_dir = get_cache_dir(cache_dir)
    # Utiliser la source comme sous-dossier
    source_dir = cache_dir / source
    source_dir.mkdir(parents=True, exist_ok=True)
    return source_dir / f"{query_hash}.json"


def get_cached(source: str, query_hash: str, cache_dir: Path | None = None) -> dict[str, Any] | None:
    """
    Récupère une réponse mise en cache si elle existe et n'a pas expiré.
    
    Args:
        source: Nom de la source (ex: "arxiv", "github", "hal")
        query_hash: Hash unique de la requête
        cache_dir: Dossier de cache (optionnel)
    
    Returns:
        La réponse en cache (dict) ou None si non trouvée/expirée
    """
    cache_path = get_cache_path(source, query_hash, cache_dir)
    
    if not cache_path.exists():
        return None
    
    try:
        with open(cache_path, "r", encoding="utf-8") as f:
            cached = json.load(f)
        
        # Vérifier l'expiration
        if time.time() - cached.get("timestamp", 0) > cached.get("ttl", DEFAULT_CACHE_TTL):
            cache_path.unlink()  # Supprimer le cache expiré
            return None
        
        return cached.get("data")
    except (json.JSONDecodeError, KeyError, OSError):
        return None


def cache_response(source: str, query_hash: str, data: Any, 
                 ttl: int = DEFAULT_CACHE_TTL, cache_dir: Path | None = None) -> None:
    """
    Stocke une réponse en cache.
    
    Args:
        source: Nom de la source
        query_hash: Hash unique de la requête
        data: Données à mettre en cache
        ttl: Durée de vie en secondes
        cache_dir: Dossier de cache (optionnel)
    """
    cache_path = get_cache_path(source, query_hash, cache_dir)
    
    cached = {
        "timestamp": time.time(),
        "ttl": ttl,
        "data": data,
    }
    
    try:
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cached, f, ensure_ascii=False, indent=2)
    except OSError:
        pass  # Ignorer les erreurs d'écriture


def generate_hash(*args: Any, **kwargs: Any) -> str:
    """Génère un hash unique à partir des arguments."""
    # Convertir tous les arguments en string
    key = str(args) + str(sorted(kwargs.items()))
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def cached_request(source: str, ttl: int = DEFAULT_CACHE_TTL, 
                   cache_dir: Path | None = None):
    """
    Décorateur pour mettre en cache les résultats des fonctions de scraping.
    
    Usage:
        @cached_request("arxiv", ttl=3600)
        def chercher(query, maxres, pages, delay):
            ...
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Générer un hash unique pour cette requête
            query_hash = generate_hash(func.__name__, args, kwargs)
            
            # Vérifier le cache
            cached = get_cached(source, query_hash, cache_dir)
            if cached is not None:
                return cached
            
            # Exécuter la fonction
            result = func(*args, **kwargs)
            
            # Stocker en cache
            cache_response(source, query_hash, result, ttl, cache_dir)
            
            return result
        return wrapper
    return decorator


def clear_cache(source: str | None = None, cache_dir: Path | None = None) -> int:
    """
    Efface le cache.
    
    Args:
        source: Nom de la source à effacer (None = tout effacer)
        cache_dir: Dossier de cache
    
    Returns:
        Nombre de fichiers supprimés
    """
    cache_dir = get_cache_dir(cache_dir)
    
    if source is not None:
        # Effacer uniquement le cache d'une source
        source_dir = cache_dir / source
        if source_dir.exists():
            count = 0
            for cache_file in source_dir.glob("*.json"):
                cache_file.unlink()
                count += 1
            return count
        return 0
    else:
        # Effacer tout le cache
        count = 0
        if cache_dir.exists():
            for cache_file in cache_dir.rglob("*.json"):
                cache_file.unlink()
                count += 1
        return count


def get_cache_stats(cache_dir: Path | None = None) -> dict[str, int]:
    """Retourne les statistiques du cache."""
    cache_dir = get_cache_dir(cache_dir)
    stats = {"total": 0, "by_source": {}}
    
    if cache_dir.exists():
        for source_dir in cache_dir.iterdir():
            if source_dir.is_dir():
                count = len(list(source_dir.glob("*.json")))
                stats["by_source"][source_dir.name] = count
                stats["total"] += count
    
    return stats
