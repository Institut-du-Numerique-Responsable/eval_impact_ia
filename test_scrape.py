#!/usr/bin/env python3
"""
Tests unitaires pour les fonctions d'évaluation des scripts de scraping.
Vérifie que le scoring et le filtrage fonctionnent comme attendu.

Usage:
    python test_scrape.py
    python -m pytest test_scrape.py -v
"""

from __future__ import annotations

import unittest
from scrape_arxiv import evaluer as arxiv_evaluer, AXES as ARXIV_AXES, IA_TERMS as ARXIV_IA_TERMS, NOISE as ARXIV_NOISE
from scrape_github import evaluer as github_evaluer, AXES as GITHUB_AXES, IA_TERMS as GITHUB_IA_TERMS, NOISE as GITHUB_NOISE
from scrape_gitlab import evaluer as gitlab_evaluer, AXES as GITLAB_AXES, IA_TERMS as GITLAB_IA_TERMS, NOISE as GITLAB_NOISE
from scrape_hal import evaluer as hal_evaluer, AXES as HAL_AXES, IA_TERMS as HAL_IA_TERMS, NOISE as HAL_NOISE


class TestArxivEvaluer(unittest.TestCase):
    """Tests pour scrape_arxiv.py"""

    def test_paper_fondateur_strubell(self) -> None:
        """Energy and Policy Considerations for Deep Learning in NLP (1906.02243)"""
        doc = {
            "titre": "Energy and Policy Considerations for Deep Learning in NLP",
            "resume": "The energy requirements of NLP models. Policy considerations.",
        }
        score, axes, ia = arxiv_evaluer(doc)
        self.assertGreaterEqual(score, 3, f"Score trop bas pour Strubell: {score}")
        self.assertIn("energie", axes, f"Axe energie manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_paper_fondateur_power_hungry(self) -> None:
        """Power Hungry Processing: Watts Driving the Cost of AI Deployment? (2311.16863/2608.07427)"""
        doc = {
            "titre": "Power Hungry Processing: Watts Driving the Cost of AI Deployment?",
            "resume": "The cost of AI deployment in terms of power and energy consumption.",
        }
        score, axes, ia = arxiv_evaluer(doc)
        self.assertGreaterEqual(score, 3, f"Score trop bas pour Power Hungry: {score}")
        self.assertIn("energie", axes, f"Axe energie manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_paper_fondateur_carbontracker(self) -> None:
        """Carbontracker (2007.03051)"""
        doc = {
            "titre": "Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models",
            "resume": "A tool to track carbon emissions from training deep learning models.",
        }
        score, axes, ia = arxiv_evaluer(doc)
        self.assertGreaterEqual(score, 4, f"Score trop bas pour Carbontracker: {score}")
        self.assertIn("carbone", axes, f"Axe carbone manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_paper_fondateur_great_power(self) -> None:
        """Great Power, Great Responsibility (2205.09646)"""
        doc = {
            "titre": "Great Power, Great Responsibility: Recommendations for Reducing Energy for Training Language Models",
            "resume": "Recommendations for reducing energy consumption in training language models.",
        }
        score, axes, ia = arxiv_evaluer(doc)
        self.assertGreaterEqual(score, 4, f"Score trop bas pour Great Power: {score}")
        self.assertIn("energie", axes, f"Axe energie manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_paper_bruit_exclu(self) -> None:
        """Les papiers hors sujet doivent être exclus"""
        noisy_docs = [
            {"titre": "High Energy Physics Experiment", "resume": "Study of particle collisions."},
            {"titre": "Carbon Nanotube Synthesis", "resume": "Chemical vapor deposition of carbon nanotubes."},
            {"titre": "Free Energy Calculations in Molecular Dynamics", "resume": "Computing free energy."},
        ]
        for doc in noisy_docs:
            with self.subTest(doc=doc):
                score, axes, ia = arxiv_evaluer(doc)
                self.assertEqual(score, 0, f"Noise non filtré: {doc['titre']} -> score={score}")

    def test_paper_acv_complet(self) -> None:
        """ACV complète d'un modèle"""
        doc = {
            "titre": "Life Cycle Assessment of Pre-training the Lucie 7B Open-Source LLM",
            "resume": "Complete LCA of a pre-training on supercomputer, including carbon, water, and ADPe.",
        }
        score, axes, ia = arxiv_evaluer(doc)
        self.assertGreaterEqual(score, 4, f"Score trop bas pour LCA: {score}")
        self.assertIn("acv", axes, f"Axe ACV manquant: {axes}")
        self.assertIn("carbone", axes, f"Axe carbone manquant: {axes}")


class TestGitHubEvaluer(unittest.TestCase):
    """Tests pour scrape_github.py"""

    def test_projet_codecarbon(self) -> None:
        """codecarbon doit être identifié comme projet IA avec axe carbone"""
        repo = {
            "name": "codecarbon",
            "full_name": "mlco2/codecarbon",
            "description": "Track carbon emissions from machine learning training and inference",
            "topics": ["carbon-footprint", "machine-learning", "sustainability"],
        }
        score, axes, ia = github_evaluer(repo)
        self.assertGreaterEqual(score, 4, f"Score trop bas pour codecarbon: {score}")
        self.assertIn("carbone", axes, f"Axe carbone manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_projet_ecologits(self) -> None:
        """ecologits doit être identifié"""
        repo = {
            "name": "ecologits",
            "full_name": "mlco2/ecologits",
            "description": "Estimate carbon footprint of LLM API calls",
            "topics": ["carbon", "llm", "api"],
        }
        score, axes, ia = github_evaluer(repo)
        self.assertGreaterEqual(score, 3, f"Score trop bas pour ecologits: {score}")
        self.assertIn("carbone", axes, f"Axe carbone manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_projet_scaphandre(self) -> None:
        """scaphandre doit être identifié"""
        repo = {
            "name": "scaphandre",
            "full_name": "hubblo-org/scaphandre",
            "description": "Energy consumption metering agent for containers and VMs",
            "topics": ["energy", "monitoring", "kubernetes"],
        }
        score, axes, ia = github_evaluer(repo)
        self.assertGreaterEqual(score, 3, f"Score trop bas pour scaphandre: {score}")
        self.assertIn("energie", axes, f"Axe energie manquant: {axes}")

    def test_projet_bruit_exclu(self) -> None:
        """Les projets hors sujet doivent être exclus"""
        noisy_repos = [
            {"name": "carbon-design-system", "description": "Design system by IBM", "topics": []},
            {"name": "free-energy-calculator", "description": "Thermodynamic free energy calculations", "topics": []},
            {"name": "greenhouse", "description": "IoT greenhouse monitoring", "topics": []},
        ]
        for repo in noisy_repos:
            with self.subTest(repo=repo):
                score, axes, ia = github_evaluer(repo)
                self.assertEqual(score, 0, f"Noise non filtré: {repo['name']} -> score={score}")


class TestGitLabEvaluer(unittest.TestCase):
    """Tests pour scrape_gitlab.py"""

    def test_projet_impacts_hpc(self) -> None:
        """impacts-hpc doit être identifié comme projet ACV"""
        projet = {
            "name": "impacts-hpc",
            "path_with_namespace": "in2p3/impacts-hpc",
            "description": "Estimate environmental impact of HPC jobs (GWP, ADPe, energy)",
            "topics": ["lca", "hpc", "carbon-footprint"],
        }
        score, axes, ia = gitlab_evaluer(projet)
        self.assertGreaterEqual(score, 4, f"Score trop bas pour impacts-hpc: {score}")
        self.assertIn("acv", axes, f"Axe ACV manquant: {axes}")

    def test_projet_numerique_responsable(self) -> None:
        """Les projets de numérique responsable doivent être identifiés"""
        projet = {
            "name": "green-claude",
            "path_with_namespace": "Institut-du-Numerique-Responsable/green-claude",
            "description": "Skill d'éco-conception pour Claude Code",
            "topics": ["eco-conception", "green-it", "climate"],
        }
        score, axes, ia = gitlab_evaluer(projet)
        self.assertGreaterEqual(score, 3, f"Score trop bas: {score}")


class TestHALEvaluer(unittest.TestCase):
    """Tests pour scrape_hal.py"""

    def test_publication_acv_llm(self) -> None:
        """ACV d'un LLM doit être identifiée"""
        doc = {
            "title_s": ["Life Cycle Assessment of Pre-training the Lucie 7B Open-Source LLM"],
            "abstract_s": ["Complete LCA of a pre-training on supercomputer."],
            "keyword_s": ["LCA", "carbon footprint", "LLM", "supercomputer"],
        }
        score, axes, ia = hal_evaluer(doc)
        self.assertGreaterEqual(score, 4, f"Score trop bas: {score}")
        self.assertIn("acv", axes, f"Axe ACV manquant: {axes}")
        self.assertTrue(ia, "Devrait être marqué IA")

    def test_publication_energie_inference(self) -> None:
        """Publication sur l'énergie d'inférence"""
        doc = {
            "title_s": ["From Words to Watts: Benchmarking the Energy Costs of LLM Inference"],
            "abstract_s": ["Measuring energy costs of large language model inference."],
            "keyword_s": ["energy", "inference", "LLM", "benchmark"],
        }
        score, axes, ia = hal_evaluer(doc)
        self.assertGreaterEqual(score, 4, f"Score trop bas: {score}")
        self.assertIn("energie", axes, f"Axe energie manquant: {axes}")


class TestConsistency(unittest.TestCase):
    """Tests de cohérence entre les différents scrapers"""

    def test_axes_communs(self) -> None:
        """Les axes doivent être cohérents entre les scrapers"""
        # Tous les scrapers doivent avoir les axes carbone, energie, eau, acv
        for axes_dict in [ARXIV_AXES, GITHUB_AXES, GITLAB_AXES, HAL_AXES]:
            with self.subTest(axes=axes_dict):
                self.assertIn("carbone", axes_dict)
                self.assertIn("energie", axes_dict)
                self.assertIn("eau", axes_dict)
                self.assertIn("acv", axes_dict)


if __name__ == "__main__":
    unittest.main()
