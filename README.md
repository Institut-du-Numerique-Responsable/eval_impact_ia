# base de ressources & de documents pour un calculateur d'impact environnemental de l'IA

[![Licence CC0 1.0](https://img.shields.io/badge/licence-CC0_1.0-6a9955?style=flat-square)](LICENSE)
[![79 références](https://img.shields.io/badge/références-79_publications-2c6e9b?style=flat-square)](#a-références-documentaires)
[![87 ressources](https://img.shields.io/badge/ressources-87_ressources-2c6e9b?style=flat-square)](#b-ressources-logicielles)
[![Indicateurs CO2e kWh eau ADPe](https://img.shields.io/badge/indicateurs-gCO₂e_·_kWh_·_eau_·_ADPe-4c8c4a?style=flat-square)](#c-proposition-de-méthodologie)
[![Dernière mise à jour](https://img.shields.io/github/last-commit/Institut-du-Numerique-Responsable/eval_impact_ia?style=flat-square&label=mise%20à%20jour&color=888888)](https://github.com/Institut-du-Numerique-Responsable/eval_impact_ia/commits/main)
[![Institut du Numérique Responsable](https://img.shields.io/badge/Institut%20du%20Numérique%20Responsable-0055a4?style=flat-square&logo=organization&logoColor=white)](https://institutnr.org)
[![Maintenu par INR](https://img.shields.io/badge/maintenu%20par-INR-0055a4?style=flat-square&logo=organization)](https://institutnr.org)

> **TL;DR** : Ce dépôt rassemble **79 publications** (HAL/arXiv/revues) et **87 outils open source** pour calculer l'impact environnemental de l'IA (carbone, énergie, eau, ADPe). Méthodologie ACV complète pour les LLM, avec des outils comme CodeCarbon, EcoLogits, Scaphandre et perf-sentinel.

## À propos du projet

**eval_impact_ia** est une **base de connaissances open source** développée et maintenue par **[l'Institut du Numérique Responsable](https://institutnr.org)** (INR). Ce projet a pour objectif de **centraliser, organiser et diffuser** les ressources nécessaires à la **mesure et réduction de l'impact environnemental de l'IA générative**.

### 🎯 Objectifs du projet

- **Rassembler** : **79 publications scientifiques** (HAL, arXiv, revues à comité de lecture) et **87 outils logiciels open source** (GitHub, GitLab, Hugging Face) sur le calcul de l'impact environnemental de l'IA.
- **Structurer** : Classer les ressources par rôle dans un calculateur (méthode, mesure, estimation, normalisation) pour faciliter leur adoption.
- **Documenter** : Fournir une méthodologie claire, des exemples d'usage, et une transparence totale sur les sources.
- **Collaborer** : Créer un référentiel commun pour la communauté francophone et internationale travaillant sur l'IA durable.

### 🏢 Porté par l'Institut du Numérique Responsable

L'[**INR**](https://institutnr.org) est une organisation française engagée pour un **numérique éco-conçu et sobre**. Son rôle dans ce projet :

- **Garantir la qualité** des ressources référencées (validation des sources, vérification des liens).
- **Maintenir l'actualité** du dépôt (veille régulière, mises à jour mensuelles).
- **Animer la communauté** autour des enjeux d'impact environnemental de l'IA.

📧 **Contact** : [contact@institutnr.org](mailto:contact@institutnr.org) | 🐦 [@INR_Numerique](https://twitter.com/INR_Numerique)

## Pourquoi ce dépôt ?

L'IA générative a un **impact environnemental mal mesuré** : entraînement, inférence, fabrication du matériel, refroidissement des datacenters. Ce projet apporte :

- **La méthode** : une synthèse de calcul pour 4 indicateurs (gCO₂e, kWh, L, gSbe) issue de 79 publications scientifiques.
- **Les outils** : 87 briques de code open source pour mesurer, estimer, normaliser.
- **La transparence** : chaque référence et ressource est sourcée, datée, et classée par rôle dans le calculateur.

---

## 🎯 Cas d'usage

### Pour les chercheurs
- **Trouver des publications** sur l'ACV des LLM → [Section A.1](#a1-acv-complète-dun-modèle)
- **Comparer des méthodologies** → [Section A.2](#a2-énergie-dentraînement-et-dinférence)
- **Étudier l'infrastructure** → [Section A.3](#a3-infrastructure-datacenter-hpc-stockage)
- **Analyser les politiques publiques** → [Section A.4](#a4-cadrage-politiques-publiques-effet-rebond)
- **Citer des sources vérifiées** → [SOURCES.md](SOURCES.md)

### Pour les ingénieurs et développeurs
- **Mesurer l'impact d'un modèle** → [Section B.1](#b1-estimer-limpact-dun-modèle-dia)
- **Mesurer la consommation électrique** → [Section B.2](#b2-mesurer-la-consommation-électrique)
- **Estimer les impacts de fabrication** → [Section B.3](#b3-estimer-les-impacts-de-fabrication-acv-matérielle)
- **Convertir en carbone** → [Section B.4](#b4-convertir-en-carbone-intensité-électrique-et-cloud)
- **Normaliser le calcul** → [Section B.5](#b5-normaliser-le-calcul)
- **Intégrer à la CI/CD** → [Section B.6](#b6-intégrer-à-la-cicd-et-à-lordonnancement)
- **Mesurer côté service numérique** → [Section B.7](#b7-mesurer-côté-service-numérique)
- **Utiliser des communs** → [Section B.8](#b8-communs-guides-et-listes-curées)
- **Explorer les ressources EcoInfo** → [Section B.9](#b9-ressources-ecoinfo-cnrs)

### Pour les décideurs et responsables
- **Comprendre les enjeux** → [Section A.4](#a4-cadrage-politiques-publiques-effet-rebond)
- **Trouver des rapports institutionnels** → [Section D.1](#d1-rapports-de-référence-mis-à-jour-chaque-année)
- **Identifier des laboratoires** → [Section D.2](#d2-laboratoires-qui-publient-régulièrement)
- **Accéder à des réseaux** → [Section D.3](#d3-réseaux-et-portails-à-interroger-directement)
- **Consulter des bases de données** → [Section D.5](#d5-bases-de-données-et-facteurs-démission)

---

Construire un calculateur d'impact environnemental de l'IA demande deux choses :
une méthode et des briques de code. Cette page rassemble les deux, pour quatre
indicateurs : carbone (gCO₂e), énergie (kWh), eau (L), ressources abiotiques
(gSbe).

- [A. Références documentaires](#a-références-documentaires) : 79 publications HAL et arXiv. La méthode, les ordres de grandeur, le cadrage.
- [B. Ressources logicielles](#b-ressources-logicielles) : 87 dépôts GitHub/GitLab/Hugging Face. Les briques réutilisables.
- [C. Proposition de méthodologie](#c-proposition-de-méthodologie) : synthèse de calcul et sept points de vigilance.
- [SOURCES.md](SOURCES.md) : **la liste des sources analysées** — ce qui a été balayé, comment, et ce qui a été écarté.
- [D. Où chercher d'autres sources](#d-où-chercher-dautres-sources) :
  - [D.1 Rapports annuels](#d1-rapports-de-référence-mis-à-jour-chaque-année) ·
  - [D.2 Laboratoires](#d2-laboratoires-qui-publient-régulièrement) ·
  - [D.3 Réseaux](#d3-réseaux-et-portails-à-interroger-directement) ·
  - [D.4 Opérateurs de datacenters](#d4-rapports-des-opérateurs-de-datacenters) ·
  - [D.5 Bases de données](#d5-bases-de-données-et-facteurs-démission) ·
  - [D.6 Événements et formations](#d6-événements-formations-et-médias-spécialisés) ·
  - [D.7 Veille prospective](#d7-veille-et-analyse-prospective) ·
  - [D.8 Sécurité](#d8-sécurité-et-conformité) ·
  - [D.9 Communautaires](#d9-ressources-communautaires-et-encyclopédiques)

---

## A. Références documentaires

Publications rangées par brique du calculateur. HAL pour la recherche
francophone, arXiv pour le reste.

### A.1 ACV complète d'un modèle : méthodes de référence

| Référence | Année | Type | Apport |
|---|---|---|---|
| [Life Cycle Assessment of Pre-training the Lucie 7B Open-Source LLM on the Jean Zay Supercomputer](https://hal.science/hal-05685132v1) | 2026 | Rapport | L'ACV complète d'un pré-entraînement réel de LLM sur supercalculateur. La référence la plus proche de l'objectif. |
| [More than carbon: cradle-to-grave environmental impacts of GenAI training on the Nvidia A100 GPU](https://hal.science/hal-05667182v1) | 2026 | Article | Multicritère, du berceau à la tombe, à l'échelle du GPU. Une des rares LCI chiffrées pour cette gamme de matériel. |
| [L'empreinte environnementale complète d'un usage numérique](https://theses.hal.science/tel-04874694v1) | 2024 | Thèse | Cadre ACV pour un service numérique, du terminal au datacenter. |
| [Analysis of the Relationship Between Carbon Footprint and Mineral Resource Depletion in the LCA of Digital Systems](https://hal.science/hal-05631178v1) | 2026 | Communication | Pourquoi ne pas s'arrêter au carbone : le couple GWP / ADPe. |
| [Automating Inventory for LCA of Computing Systems through Machine Vision](https://hal.science/hal-05661956v1) | 2026 | Communication | Automatiser l'inventaire matériel, verrou classique de l'ACV. |
| [ACV de Mistral Large 2](https://mistral.ai/fr/news/our-contribution-to-a-global-environmental-standard-for-ai/) | 2025 | ACV produit | Le seul éditeur de modèle à publier une ACV complète : 20,4 ktCO₂e, 281 000 m³ d'eau et 660 kg Sb eq pour l'entraînement et 18 mois d'usage, puis 1,14 gCO₂e et 45 mL d'eau pour une réponse de 400 tokens. Conforme aux normes ISO 14040/44 et au GHG Protocol Product Standard, menée avec Carbone 4 et l'ADEME, relue par Resilio et Hubblo. Le format de restitution à viser. |
| [Beyond Efficiency: A Systematic Review of Energy Consumption and Carbon Footprint Across the AI Lifecycle](https://doi.org/10.3390/su18031359) | 2026 | Revue systématique | Synthèse des études quantitatives sur tout le cycle de vie : entraînement, inférence, matériel, infrastructure. Le point de départ pour fixer un périmètre. |
| [Generative AI impact assessment through a life cycle analysis of multiple data center typologies](https://doi.org/10.1016/j.apenergy.2025.127288) | 2026 | Article (Applied Energy) | Compare l'ACV de plusieurs architectures de datacenter et montre le poids du choix de modèle et de la localisation. |
| [Quantifying and Disclosing the Environmental Footprint of AI in Research: Life Cycle-Informed Framework and Open-Access Calculator](https://doi.org/10.2196/90770) | 2026 | Article (JMIR AI) | Cadre de calcul complet : énergie opérationnelle, intensité réseau, PUE, eau, fabrication du matériel. Définit un jeu minimal de données à publier pour qu'un résultat soit vérifiable. |
| [Estimating the Carbon Footprint of BLOOM, a 176B Parameter Language Model](https://arxiv.org/abs/2211.02001) | 2022 | Préprint | Hugging Face décompose l'empreinte d'un LLM ouvert : entraînement, fabrication du matériel, déploiement. Le modèle de décomposition à reprendre. |

### A.2 Énergie d'entraînement et d'inférence : les modèles prédictifs

| Référence | Année | Type | Apport |
|---|---|---|---|
| [WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks](https://hal.science/hal-05681820v1) | 2026 | Communication | Estimation de l'énergie d'inférence **couche par couche**. |
| [A Framework for Analytical Performance and Energy Prediction of DL Training on GPUs](https://minesparis-psl.hal.science/hal-05398496v1) | 2025 | Communication | Modèle analytique prédictif, sans instrumenter la machine. |
| [Assessing the Energy and Carbon Emissions of Neural Speaker Verification Model in Training and Inference](https://hal.science/hal-05643961v1) | 2026 | Communication | Protocole de mesure comparant entraînement et inférence. |
| [Energy-Aware Deep Learning on GPUs through Parameter Sharing and Mixed Precision Training](https://minesparis-psl.hal.science/hal-05393922v1) | 2025 | Communication | Chiffre l'effet des choix d'implémentation (précision, partage de paramètres) sur la consommation. |
| [Energy-Aware Scheduling of Large-Scale Deep Learning Training](https://hal.science/hal-05531422v1) | 2026 | Communication | Ordonnancement énergétique de l'entraînement à grande échelle. |
| [Adaptive Inference for Cost-Efficient Deep Neural Networks](https://hal.science/tel-05504891v2) | 2026 | Thèse | Inférence adaptative : moduler le coût selon la difficulté de l'entrée. |
| [A Testbed Framework for Estimating the Environmental Impact of Agentic AI Workflows in HPC](https://hal.science/hal-05594455v1) | 2026 | Communication | Traite les **workflows agentiques** : plusieurs appels chaînés, coût cumulé. |
| [Heuristique, CSP ou LLM ? Étude comparative du coût énergétique du placement de services](https://hal.science/hal-05713191v1) | 2026 | Communication | Compare le coût énergétique de l'IA à celui d'une alternative algorithmique classique. |
| [Évaluation des impacts environnementaux et sociétaux de l'IA générative](https://inria.hal.science/hal-04346102v2) | 2025 | Rapport | Analyse Inria des impacts environnementaux et sociétaux de l'IA générative. |
| [Contribution à l'évaluation de l'impact environnemental des modèles de langage](https://theses.hal.science/tel-05369950) | 2025 | Thèse | Travail doctoral sur l'évaluation des impacts des modèles de langage. |
| [The Carbon Cost of Intelligence: A Domain-Specific Framework for Measuring AI Energy and Emissions](https://doi.org/10.3390/en19030642) | 2026 | Article (Energies) | Segmente l'empreinte par type de charge de travail, avec des mesures empiriques sur GPT-4. Utile pour raisonner par usage plutôt que par modèle. |
| [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) | 2023 | Rapport technique | Un des rares rapports de modèle à documenter matériel, durée de pré-entraînement et estimation carbone. Le niveau de transparence à exiger. |
| [From Words to Watts: Benchmarking the Energy Costs of Large Language Model Inference](https://arxiv.org/abs/2310.03003) | 2023 | Préprint | Le MIT Lincoln Laboratory mesure l'énergie d'inférence des LLM sur supercalculateur, par taille de modèle et par configuration. |
| [Power Hungry Processing: Watts Driving the Cost of AI Deployment?](https://arxiv.org/abs/2311.16863) | 2023 | Préprint | Hugging Face compare l'énergie d'inférence selon la tâche : la génération d'image coûte des ordres de grandeur de plus que la classification. |
| [Great Power, Great Responsibility: Recommendations for Reducing Energy for Training Language Models](https://arxiv.org/abs/2205.09646) | 2022 | Préprint | Le MIT chiffre les gains du bridage de puissance des GPU et de l'arrêt anticipé d'entraînement. |
| [Sustainable AI: Balancing Innovation and Environmental Impact](https://arxiv.org/abs/2506.10989) | 2025 | Préprint | Analyse des enjeux de durabilité de l'IA générative et des trade-offs entre innovation et impact environnemental. |
| [Carbon Emissions and Large Neural Network Training](https://arxiv.org/abs/2104.10350) | 2021 | Préprint | Google et Berkeley posent les facteurs qui font varier l'empreinte d'un facteur 100 : modèle, matériel, datacenter, mix électrique. |
| [Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models](https://arxiv.org/abs/2007.03051) | 2020 | Préprint | L'Université de Copenhague décrit la méthode de prédiction implémentée dans `carbontracker` (partie B.1). |
| [Quantifying the Carbon Emissions of Machine Learning](https://arxiv.org/abs/1910.09700) | 2019 | Préprint | L'article fondateur du calculateur ML CO2 Impact (partie B.1). La formule minimale, à connaître avant de la complexifier. |
| [Energy and Policy Considerations for Deep Learning in NLP](https://arxiv.org/abs/1906.02243) | 2019 | Préprint | Le texte qui a ouvert le sujet, en chiffrant l'entraînement des modèles de langue et la recherche d'hyperparamètres. |

### A.3 Infrastructure : datacenter, HPC, stockage

| Référence | Année | Type | Apport |
|---|---|---|---|
| [The Environmental Impacts Of High-Performance Computing: A Systematic Mapping Study](https://hal.science/hal-05601113v2) | 2026 | Revue | Cartographie de la littérature. Commencez par là. |
| [Analyse de l'empreinte carbone du HPC](https://hal.science/hal-05248774v1) | 2025 | Communication | Empreinte carbone d'un centre de calcul, en français. |
| [Life Cycle Assessment of Edge Data Centers](https://hal-lirmm.ccsd.cnrs.fr/lirmm-05015619v2) | 2025 | Article | ACV en présence de renouvelables et de serveurs reconditionnés. |
| [Micro-Datacenters Model for Carbon Footprint Assessment and Energy Optimization](https://hal.science/hal-05252340v1) | 2025 | Poster | Modèle de calcul pour micro-datacenters. |
| [Modélisation et évaluation d'un concept de mini data center à faible impact environnemental](https://hal.science/tel-05520680v1) | 2025 | Thèse | Conception et évaluation détaillées. |
| [Carbon Footprint of Storage in Data Centers: the Impact of Using SSDs for Key-Value Stores](https://hal.science/hal-05447447v1) | 2025 | Communication | Le stockage, poste que les calculateurs omettent. |
| [Carbon Topography Representation: Improving Impacts of Data Center Lifecycle](https://hal.science/hal-05138320v1) | 2025 | Communication | Représentation spatialisée des impacts sur le cycle de vie. |
| [ETP4HPC SRA 6 White Paper — Energy Efficiency and Sustainability](https://hal.science/hal-05494490v1) | 2026 | Rapport | Feuille de route européenne HPC. |
| [Energy-Aware Computing in the Year 2026](https://minesparis-psl.hal.science/hal-05632692v1) | 2026 | Communication | État de l'art du calcul économe. |
| [The carbon and water footprints of data centers and what this could mean for artificial intelligence](https://doi.org/10.1016/j.patter.2025.101430) | 2026 | Article (Patterns) | Traite carbone et eau ensemble à l'échelle du datacenter, et pointe ce que les opérateurs ne publient pas. |
| [Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models](https://arxiv.org/abs/2304.03271) | 2023 | Préprint | Le Ren Research Group (UC Riverside) sépare l'eau consommée sur site pour le refroidissement de celle consommée hors site pour produire l'électricité. La principale source sur l'axe eau. |

### A.4 Cadrage, politiques publiques, effet rebond

| Référence | Année | Type | Apport |
|---|---|---|---|
| [Recommandations pour une action publique en faveur d'une IA générative respectueuse de l'environnement](https://hal.science/hal-04371031v2) | 2023 | Rapport | Cadre la position française sur l'IA générative soutenable. |
| [Promouvoir des modèles d'intelligence artificielle frugale pour et par les politiques publiques](https://hal.science/hal-04510171v1) | 2024 | Rapport | Définit l'IA frugale et ses leviers. |
| [The Environmental Impacts of Machine Learning Training Keep Rising — Evidencing Rebound Effect](https://hal.science/hal-04839926v5) | 2025 | Article | Montre empiriquement que les gains d'efficacité sont absorbés par la hausse des usages. |
| [When rebound effect is not a side effect](https://hal.science/hal-05566029v1) | 2026 | Article | Analyse sociotechnique de l'effet rebond du numérique. |
| [How Hyper-Datafication Impacts the Sustainability Costs in Frontier AI](https://inria.hal.science/hal-05651665v1) | 2026 | Communication (FAccT) | Coûts de soutenabilité liés à l'explosion des données. |
| [Environmental Cost of Artificial Intelligence: Carbon, Water and Land Footprints](https://unu.edu/inweh/collection/environmental-cost-of-AIs-Enrgy-Use-Carbon-water-and-land-footprints) | 2026 | Rapport (UNU-INWEH) | L'Université des Nations unies quantifie trois empreintes, dont le sol, et documente les limites des données publiques. [PDF](https://collections.unu.edu/eserv/UNU:10647/UNU-INWEH-Report-The_Env_Cost_of_AI-2026.pdf) |
| [Scenario-based forecasting of the global energy demand and carbon footprint of artificial intelligence](https://pmc.ncbi.nlm.nih.gov/articles/PMC12978478/) | 2026 | Article (PLOS ONE) | Cadre de simulation jusqu'en 2050, séparant fabrication des composants, transport et électricité. |
| [A Systematic Review of Green and Sustainable AI: Taxonomy, Metrics, Challenges, and Open Research Directions](https://doi.org/10.3390/su18084115) | 2026 | Revue systématique | Taxonomie des pratiques et des métriques. Sert de grille de lecture pour classer un indicateur. |
| [AI carbon footprint: The non-negligible hidden emission source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12657291/) | 2025 | Article (Eco-Environment & Health) | Recense les sources d'émissions oubliées : refroidissement, fabrication des GPU, chaîne d'approvisionnement. |
| [L'IA générative, du changement climatique](https://carbone4.com/fr/articles/ia-generative-du-changement-climatique) | 2026 | Analyse (Carbone 4) | Agrège les chiffres disponibles côté français et documente ce que les éditeurs de modèles ne publient pas. |
| [AI Index Report, chapitre énergie et environnement](https://hai.stanford.edu/ai-index/2026-ai-index-report) | 2026 | Rapport annuel | Stanford HAI publie le seul suivi chiffré comparable d'une année sur l'autre : émissions d'entraînement par modèle, capacité électrique des datacenters, eau d'inférence. |
| [Green AI](https://arxiv.org/abs/1907.10597) | 2019 | Préprint | Oppose la course à la performance à tout prix et propose l'efficacité comme critère d'évaluation des travaux de recherche. |

### A.5 Restitution, pédagogie, perception

| Référence | Année | Type | Apport |
|---|---|---|---|
| [EcoDashAI: A Visual Analytics Dashboard for Multi-Criteria Evaluation of Language Models Frugality](https://hal.science/hal-05629071v1) | 2026 | Communication | Comment **afficher** un résultat multicritère sans le réduire à un chiffre unique. |
| [Estimer l'empreinte carbone via LLM : vers une architecture frugale et adaptative](https://hal.science/hal-05694015v1) | 2026 | Communication | Utiliser un LLM dans le calculateur lui-même, à coût maîtrisé. |
| [The Invisible Cost of AI-Empowered Education](https://hal.science/hal-05630227v1) | 2025 | Communication | Perception de l'empreinte par les utilisateurs. |
| [Cross-Cultural Differences in Perceptions of the Environmental Impact of Generative AI](https://hal.science/hal-05630387v1) | 2026 | Communication | Variations culturelles de cette perception. |
| [TD programmation — empreinte environnementale du numérique](https://hal.science/hal-05017574v1) | 2025 | Support de cours | Exercices prêts à l'emploi. |
| [Les ressources pour enseigner le numérique responsable en IUT](https://hal.science/hal-05632185v1) | 2026 | Chapitre | Panorama des ressources pédagogiques. |
| [L'IA générative est-elle soutenable ? Le vrai coût écologique d'un prompt](https://theconversation.com/lia-generative-est-elle-soutenable-le-vrai-cout-ecologique-dun-prompt-269432) | 2025 | Article | Analyse grand public des coûts environnementaux des prompts. |
| [Enquête : derrière l'IA, les travailleurs précaires des pays du Sud](https://theconversation.com/enquete-derriere-lia-les-travailleurs-precaires-des-pays-du-sud-201503) | 2025 | Article | Enquête sur les coûts sociaux cachés de l'IA. |

---

## B. Ressources logicielles

Dépôts de code rangés par **rôle dans le calculateur**, GitHub et GitLab
confondus.

### B.1 Estimer l'impact d'un modèle d'IA

| Ressource | Plateforme | Apport |
|---|---|---|
| [mlco2/codecarbon](https://github.com/mlco2/codecarbon) | GitHub | Émissions d'un calcul Python, entraînement comme inférence : kWh mesurés (RAPL/NVML) × intensité carbone régionale. Décorateur, sortie CSV, dashboard. La brique que tout le monde utilise. |
| [mlco2/ecologits](https://github.com/mlco2/ecologits) | GitHub | **Impact d'un appel API LLM** sans accès à la machine : énergie, GWP, ADPe estimés depuis les tokens et la taille du modèle. Votre seule option quand vous ne mesurez pas. |
| [saintslab/carbontracker](https://github.com/saintslab/carbontracker) | GitHub | Mesure **et prédit** l'énergie et le carbone d'un entraînement, par extrapolation dès les premières epochs. |
| [ml-energy/zeus](https://github.com/ml-energy/zeus) | GitHub | Mesure **et optimise** l'énergie des applications d'IA (arbitrage énergie/temps via DVFS GPU). |
| [Breakend/experiment-impact-tracker](https://github.com/Breakend/experiment-impact-tracker) | GitHub | Traçage d'expériences ML, avec génération d'un paragraphe d'impact pour publication. |
| [mlco2/impact](https://github.com/mlco2/impact) | GitHub | ML CO2 Impact : calculateur web historique (Lacoste et al.), formule simple et pédagogique. |
| [Helmholtz-AI-Energy/perun](https://github.com/Helmholtz-AI-Energy/perun) | GitHub | Énergie d'applications Python, orienté HPC / MPI multi-nœuds. |
| [HewlettPackard/sustain-cluster](https://github.com/HewlettPackard/sustain-cluster) | GitHub | Environnement Gymnasium pour benchmarker l'ordonnancement durable de clusters IA. |
| [huggingface/AIEnergyScore](https://github.com/huggingface/AIEnergyScore) | GitHub | **Notation comparable** de l'efficacité énergétique des modèles : méthodologie de benchmark standardisée. |
| [genai-impact/ecologits-calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator) | Hugging Face Space | Calculateur interactif pour estimer l'empreinte carbone des requêtes LLM (implémentation alternative d'EcoLogits). |
| [robintra/perf-sentinel](https://github.com/robintra/perf-sentinel) | GitHub | Détection d'**anti-patterns I/O** (N+1, requêtes redondantes, lentes) dans les traces OpenTelemetry, avec **scoring carbone par requête** (SCI-aligné). Quality gate CI/CD, dashboard HTML, métriques Prometheus. Polyglotte, léger (<20 Mo), auto-hébergé. |
| [Ren-Research/Making-AI-Less-Thirsty](https://github.com/Ren-Research/Making-AI-Less-Thirsty) | GitHub | **Empreinte eau de l'IA** : refroidissement et eau du mix électrique. La principale source sur cet axe. |
| [ecs-lab/llm-inference-energy-benchmark](https://gitlab.com/ecs-lab/llm-inference-energy-benchmark) | GitLab | **Jeu de mesures** : puissance, traces et débit de 13 LLM (1,3B→9B) sur H100 / TensorRT-LLM. De quoi **calibrer et valider** un modèle analytique (papier *SweetSpot*, ICPE 2026). |
| [inria/magnet/declearn/energy](https://gitlab.inria.fr/magnet/declearn/energy) | GitLab INRIA | Consommation d'un framework d'apprentissage fédéré. |

### B.2 Mesurer la consommation électrique

| Ressource | Plateforme | Apport |
|---|---|---|
| [hubblo-org/scaphandre](https://github.com/hubblo-org/scaphandre) | GitHub | Agent de métrologie énergétique (RAPL, cgroups, VM), exporteur Prometheus. Ce que déploient la plupart des équipes infra. |
| [sustainable-computing-io/kepler](https://github.com/sustainable-computing-io/kepler) | GitHub | Énergie par pod/conteneur/nœud **Kubernetes** (eBPF + modèles), exporteur Prometheus. |
| [green-coding-solutions/green-metrics-tool](https://github.com/green-coding-solutions/green-metrics-tool) | GitHub | Banc de mesure complet : énergie et émissions d'un logiciel, timelines, intégration git, comparaison de versions. |
| [powerapi-ng/powerapi](https://github.com/powerapi-ng/powerapi) | GitHub | Framework de construction de *software-defined power meters*. Voir [smartwatts-formula](https://github.com/powerapi-ng/smartwatts-formula) (modèle auto-adaptatif) et [pyJoules](https://github.com/powerapi-ng/pyJoules) (énergie d'un bloc de code). |
| [joular/powerjoular](https://github.com/joular/powerjoular) | GitHub | Consommation **par processus**, multi-plateformes (RAPL + Nvidia). [joularjx](https://github.com/joular/joularjx) descend au niveau du code source Java. |
| [tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge) | GitHub | Mesure multiplateforme (Linux/macOS/Windows, Intel/AMD/Apple Silicon), là où RAPL ne suffit pas. |
| [kajalv/nvml-power](https://github.com/kajalv/nvml-power) | GitHub | Puissance GPU par polling NVML. La brique GPU minimale. |
| [irit/sepia-pub/expetator](https://gitlab.irit.fr/sepia-pub/expetator) | GitLab IRIT | Campagnes de benchmarks HPC avec leviers DVFS et monitoring bas niveau (compteurs matériels, RAPL) sur Grid'5000. |
| [sosy-lab/cpu-energy-meter](https://gitlab.com/sosy-lab/software/cpu-energy-meter) | GitLab | Énergie CPU Intel via RAPL. Petit, auditable. |
| [inria/majay/energy-consumption-of-gpu-benchmarks](https://gitlab.inria.fr/majay/energy-consumption-of-gpu-benchmarks) | GitLab INRIA | Compare les outils de mesure de consommation GPU et tranche entre eux. |
| [inria/mbelgaid/python-energy](https://gitlab.inria.fr/mbelgaid/python-energy) | GitLab INRIA | Énergie induite par les outils d'optimisation Python (transpileurs, JIT). |
| [inria/delamare/tutoriel-mesure-energie-wid2](https://gitlab.inria.fr/delamare/tutoriel-mesure-energie-wid2) | GitLab INRIA | **Tutoriel** de mesure d'énergie. Point de départ pédagogique. |

### B.3 Estimer les impacts de fabrication (ACV matérielle)

| Ressource | Plateforme | Apport |
|---|---|---|
| [in2p3/impacts-hpc](https://gitlab.in2p3.fr/impacts-hpc/impacts-hpc) | GitLab IN2P3 | Librairie Python qui estime l'impact d'un *job* datacenter en GWP, ADPe et énergie primaire, et rend chaque résultat **explicable, sourcé et assorti de son incertitude**. Le modèle à copier. [Documentation](https://impacthpc-cc8227.pages.in2p3.fr/index.html) · [ontologie](https://gitlab.in2p3.fr/impacts-hpc/ontology-impactshpc) |
| [Boavizta/environmental-footprint-data](https://github.com/Boavizta/environmental-footprint-data) | GitHub | Base ouverte des impacts environnementaux d'équipements, issue des fiches constructeurs. |
| [Boavizta/boaviztapi](https://github.com/Boavizta/boaviztapi) | GitHub | **API des impacts de fabrication** (serveur, CPU, GPU, RAM, SSD) : GWP, ADPe, PE. Couvre l'*embodied* que CodeCarbon ignore. |
| [cloud-carbon-footprint/cloud-carbon-coefficients](https://github.com/cloud-carbon-footprint/cloud-carbon-coefficients) | GitHub | Notebooks qui dérivent les coefficients énergie/carbone du cloud. Ils exposent **la méthode**, pas seulement le résultat. |
| [in2p3/ecoinfo/ecodiag](https://gitlab.in2p3.fr/ecoinfo/ecodiag) | GitLab IN2P3 | Bilan carbone d'un parc IT par approche ACV matériel. Daté, mais le modèle se lit facilement. |

### B.4 Convertir en carbone : intensité électrique et cloud

| Ressource | Plateforme | Apport |
|---|---|---|
| [electricitymaps/electricitymaps-contrib](https://github.com/electricitymaps/electricitymaps-contrib) | GitHub | Parsers open source de l'**intensité carbone du réseau** mondial. Fournit le gCO₂e/kWh horaire et localisé. |
| [cloud-carbon-footprint/cloud-carbon-footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) | GitHub | kWh + tCO₂e à partir des factures AWS/GCP/Azure. [Plugin Backstage](https://github.com/cloud-carbon-footprint/ccf-backstage-plugin) disponible. |
| [Green-Software-Foundation/carbon-aware-sdk](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | GitHub | SDK pour décaler ou placer un calcul selon l'intensité carbone. |
| [Green-Software-Foundation/real-time-cloud](https://github.com/Green-Software-Foundation/real-time-cloud) | GitHub | Standards de données énergie/carbone temps réel pour les fournisseurs cloud. |
| [GoogleCloudPlatform/region-picker](https://github.com/GoogleCloudPlatform/region-picker) | GitHub | Choix d'une région cloud arbitrant carbone, prix et latence. |
| [Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC](https://github.com/Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC) | GitHub | Rapport énergie + carbone de ses jobs Slurm. Pendant HPC de Green Algorithms. |
| [fledee/ecodynelec](https://gitlab.com/fledee/ecodynelec) | GitLab | Impacts de l'électricité européenne en **suivant les flux entre pays**, donc sur le mix réellement consommé. |
| [elioth/dynco2](https://gitlab.com/elioth/dynco2) | GitLab | Forçage radiatif instantané d'une série d'émissions (modèle DynCO2), pour aller au-delà du gCO₂e. |
| [meltano/tap-carbon-intensity](https://gitlab.com/meltano/tap-carbon-intensity) | GitLab | Connecteur vers l'API Carbon Intensity (UK). |
| [inria/mlanvin/compute_carbon_footprint_g5k](https://gitlab.inria.fr/mlanvin/compute_carbon_footprint_g5k) | GitLab INRIA | Carbone d'un job Grid'5000. Le modèle reste simple (puissance ∝ usage CPU, bornée au TDP) et **documente son périmètre et ses exclusions**. |

### B.5 Normaliser le calcul

| Ressource | Plateforme | Apport |
|---|---|---|
| [Green-Software-Foundation/sci](https://github.com/Green-Software-Foundation/sci) | GitHub | **Software Carbon Intensity** : spécification normative, `SCI = (E × I + M) / R`. Cadre de référence pour structurer un calculateur. |
| [Green-Software-Foundation/if](https://github.com/Green-Software-Foundation/if) | GitHub | Impact Framework : pipeline déclaratif (YAML) composé de plugins. L'architecture dont s'inspirer pour l'outil à construire. |
| [Comparia](https://www.comparia.beta.gouv.fr/) | Plateforme gouvernementale | Outil de comparaison des impacts environnementaux des services numériques (en développement). |

### B.6 Intégrer à la CI/CD et à l'ordonnancement

| Ressource | Plateforme | Apport |
|---|---|---|
| [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) | GitHub | Empreinte carbone de **sessions d'agent de code**, le cas d'usage voisin du nôtre. |
| [green-coding-solutions/eco-ci-energy-estimation](https://github.com/green-coding-solutions/eco-ci-energy-estimation) | GitHub | Estimation d'énergie dans GitHub Actions, GitLab CI et Jenkins. |
| [GreenScheduler/cats](https://github.com/GreenScheduler/cats) | GitHub | Climate-Aware Task Scheduler : décale un job vers un créneau bas carbone. |
| [Institut-du-Numerique-Responsable/green-claude](https://github.com/Institut-du-Numerique-Responsable/green-claude) | GitHub | Skill d'éco-conception (RGESN, GR491, Green Software) pour Claude Code. |
| [deepshotinc/gitgreen](https://gitlab.com/deepshotinc/gitgreen) | GitLab | CI/CD *carbon-aware* pour GitLab sur GCP. [Version auto-hébergée](https://gitlab.com/deepshotinc/gitgreen-server). |
| [youneslaaroussi/duoops](https://gitlab.com/youneslaaroussi/duoops) | GitLab | CLI et portail de transparence des pipelines GitLab, volet émissions inclus. |
| [dimasna96/greenstatus](https://gitlab.com/dimasna96/greenstatus) | GitLab | Composant CI/CD : tests d'API + calcul CO₂, rapport publié sur GitLab Pages. |
| [demeringo/scaphandre-runner](https://gitlab.com/demeringo/scaphandre-runner) | GitLab | Exécution de Scaphandre dans GitLab CI. |
| [sustainable-computing-systems/carbond](https://gitlab.com/sustainable-computing-systems/carbond) | GitLab | Démon système pour la *carbon awareness*. |

### B.7 Mesurer côté service numérique

| Ressource | Plateforme | Apport |
|---|---|---|
| [marmelab/greenframe-cli](https://github.com/marmelab/greenframe-cli) | GitHub | Empreinte carbone d'un **scénario utilisateur** sur une application web. Mesure conteneurisée réelle, sans modèle intermédiaire. |
| [green-code-initiative/creedengo-rules-specifications](https://github.com/green-code-initiative/creedengo-rules-specifications) | GitHub | Règles d'écoconception logicielle pour SonarQube (ex-ecoCode). |
| [cnumr/EcoIndex](https://github.com/cnumr/EcoIndex) | GitHub | EcoIndex : score environnemental d'une page web. Voir [EcoIndex_python](https://github.com/cnumr/EcoIndex_python). |
| [green-code-initiative/EcoSonar](https://github.com/green-code-initiative/EcoSonar) | GitHub | Audit d'écoconception intégré à la CI. |
| [wholegrain/carbon-api-2-0](https://gitlab.com/wholegrain/carbon-api-2-0) | GitLab | API Website Carbon. Dépréciée, mais son modèle de calcul se lit facilement. |
| [wholegrain/website-carbon-badges](https://gitlab.com/wholegrain/website-carbon-badges) | GitLab | Badges d'émissions d'une page web. |
| [gibbonjoyeux/bare-tracker-extension](https://gitlab.com/gibbonjoyeux/bare-tracker-extension) | GitLab | Extension navigateur exposant l'impact de la navigation. |

### B.8 Communs, guides et listes curées

| Ressource | Plateforme | Apport |
|---|---|---|
| [aac-ademe/consortium-ia-durable](https://gitlab.com/aac-ademe/consortium-ia-durable) | GitLab | Commun numérique ADEME qui coordonne CodeCarbon et EcoLogits, publie un [guide IA durable](https://challengedata.ens.fr/ia_durable/guide) et anime un espace de formation (branche `toy_projects_fr`). Le point d'entrée côté français. |
| [AI Environmental Footprint Calculator](https://doi.org/10.2196/90770) | JMIR AI | Calculateur en accès libre couvrant énergie, PUE, eau et fabrication, avec la méthode publiée en regard (partie A.1). |
| [samuelrince/awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) | GitHub | Liste curée d'outils et ressources Green AI, pour prolonger la veille. |
| [schaDev/GreenCoding-measuring-tools](https://github.com/schaDev/GreenCoding-measuring-tools) | GitHub | Panorama comparatif des outils de mesure énergie/CO₂ des logiciels. |
| [in2p3/ecoinfo/bonnes-pratiques](https://gitlab.in2p3.fr/ecoinfo/bonnes-pratiques) | GitLab IN2P3 | Guide EcoInfo (CNRS) de bonnes pratiques pour l'informatique de l'ESR. |
| [aac-ademe](https://gitlab.com/aac-ademe) | GitLab | Groupe complet des appels à communs ADEME, dont `datacenter-footprint`. |

### B.9 Ressources EcoInfo (CNRS)

Ressources issues du site [EcoInfo](https://ecoinfo.cnrs.fr/), le réseau français de l'informatique éco-responsable.

| Ressource | Type | Date | Catégories | Apport |
|---|---|---|---|---|
| [Impact environnemental de l'IA](https://ecoinfo.cnrs.fr/2019/10/01/impact-environnemental-de-lia/) | Article | 2019 | IA | Analyse complète des impacts environnementaux de l'IA. |
| [Consommation énergétique de l'utilisation de l'IA](https://ecoinfo.cnrs.fr/2021/06/12/consommation-energetique-de-lutilisation-de-lia/) | Article | 2021 | IA, Energie, Agir | Focus sur la consommation énergétique en phase d'inférence et d'utilisation. |
| [Les impacts sociaux de l'IA](https://ecoinfo.cnrs.fr/2022/03/15/impacts-sociaux-de-lia/) | Article | 2022 | IA, Aspects sociaux | Analyse des enjeux sociaux liés à l'IA. |
| [Évaluer les impacts d'un projet d'IA](https://ecoinfo.cnrs.fr/2022/12/14/evaluer-les-impacts-dun-projet-dia/) | Article | 2022 | IA, Bonnes pratiques | Méthodologie pour évaluer l'impact d'un projet d'IA. |
| [BGES_DC](https://ecoinfo.cnrs.fr/2026/08/28/bges_dc/) | Ressource | 2026 | Datacentres | Bilan Gaz à Effet de Serre des Datacentres. |
| [Le vrai coût énergétique du numérique](https://ecoinfo.cnrs.fr/2022/10/21/le-vrai-cout-energetique-du-numerique/) | Article | 2022 | Datacentres, Energie | Analyse approfondie des coûts énergétiques réels. |
| [Guide des bonnes pratiques du Code de Conduite européen sur les Datacentres](https://ecoinfo.cnrs.fr/2020/05/19/guide-des-bonnes-pratiques-du-code-de-conduite-europeen-sur-les-datacentres/) | Guide | 2020 | Datacentres | Recommandations pour des datacentres éco-responsables. |
| [Mesurer la consommation électrique d'un serveur](https://ecoinfo.cnrs.fr/2019/09/13/mesurer-la-consommation-electrique-dun-serveur/) | Guide | 2019 | Datacentres, Mesures | Méthodes de mesure de la consommation électrique. |
| [Plaquette « Je code : les bonnes pratiques en éco-conception](https://ecoinfo.cnrs.fr/2026/03/05/plaquette-je-code-les-bonnes-pratiques-en-eco-conception-de-service-numerique-a-destination-des-developpeurs-de-logiciels/) | Guide | 2026 | Ecoconception | Bonnes pratiques pour les développeurs. |
| [Formation : Impact environnemental du numérique](https://ecoinfo.cnrs.fr/2020/06/23/formation-2020-impact-environnemental-du-numerique-comprendre-et-agir/) | Formation | 2020 | ACV, Ecoconception | Formation complète sur l'impact environnemental du numérique. |
| [ANF 2023 : Impacts environnementaux du numérique — les 8R](https://ecoinfo.cnrs.fr/2023/05/04/anf-2023-impacts-environnementaux-du-numerique-les-8r/) | Atelier | 2023 | Agir | Méthode des 8R pour réduire l'impact environnemental. |
| [MOOC : Impacts environnementaux du numérique](https://ecoinfo.cnrs.fr/2022/01/11/mooc-impacts-environnementaux-du-numerique/) | MOOC | 2022 | Agir | Formation en ligne sur les impacts environnementaux. |
| [Datacentre éco-responsable à l'université Lille 1](https://ecoinfo.cnrs.fr/2015/12/23/datacentre-eco-responsable-a-luniversite-de-lilles/) | Retour d'expérience | 2015 | Datacentres | Exemple concret de datacentre éco-responsable. |
| [Froggy: supercalculateur refroidi à l'eau tiède](https://ecoinfo.cnrs.fr/2014/09/10/froggy-un-supercalculateur-refroidi-avec-de-leau-tiede-universite-de-grenoble/) | Retour d'expérience | 2014 | Datacentres | Innovation en refroidissement de datacentre. |
| [Panorama des systèmes de refroidissement en Datacentres](https://ecoinfo.cnrs.fr/2009/10/08/panorama-des-principaux-systemes-de-refroidissement-en-datacentres/) | Guide | 2009 | Datacentres | Comparatif des solutions de refroidissement. |
| [Le Free Cooling](https://ecoinfo.cnrs.fr/2009/10/08/le-free-cooling/) | Guide | 2009 | Datacentres | Technique de refroidissement gratuit. |
| [Guide des bonnes pratiques pour améliorer l'efficience énergétique](https://ecoinfo.cnrs.fr/2009/09/15/datacentres-guide-des-bonnes-pratiques-pour-ameliorer-leur-efficience-energetique/) | Guide | 2009 | Datacentres, Energie | Recommandations pour l'optimisation énergétique. |
| [« Carbon neutralities » of ICT companies](https://ecoinfo.cnrs.fr/2022/07/05/carbon-neutralities-of-ict-companies/) | Article | 2022 | Données, Energie | Analyse des claims de neutralité carbone des entreprises IT. |
| [Les « neutralités carbone » des entreprises du numérique](https://ecoinfo.cnrs.fr/2022/03/17/les-neutralites-carbone-des-entreprises-du-numerique/) | Article | 2022 | Données, Energie | Version française de l'analyse ci-dessus. |
| [Références ACV PC](https://ecoinfo.cnrs.fr/2010/04/12/references-acv-pc/) | Base de données | 2010 | ACV | Références pour les ACV des PCs. |
| [Calculer l'empreinte carbone d'1 heure de calcul sur un cœur](https://ecoinfo.cnrs.fr/2020/04/24/calculer-lempreinte-carbone-d1-heure-de-calcul-sur-un-coeur/) | Guide | 2020 | Datacentres, Energie, Mesures | Méthodologie de calcul pratique. |
| [Code de Conduite européen sur les Datacentres](https://ecoinfo.cnrs.fr/2019/05/06/code-de-conduite-europeen-sur-les-datacentres/) | Guide | 2019 | Datacentres | Cadre européen pour les datacentres durables. |
| [Audit de salles informatiques (datacentre)](https://ecoinfo.cnrs.fr/2019/02/12/audit-de-salles-informatiques-datacentre/) | Guide | 2019 | Datacentres | Méthodologie d'audit énergétique. |
| [Eco-conception](https://ecoinfo.cnrs.fr/2019/02/19/eco-conception/) | Guide | 2019 | Ecoconception | Principes fondamentaux de l'éco-conception. |
| [Agir vers la sobriété numérique](https://ecoinfo.cnrs.fr/2021/03/01/agir-vers-la-sobriete-numerique/) | Guide | 2021 | Agir | Stratégies pour réduire l'empreinte numérique. |

---
## C. Proposition de méthodologie

Synthèse de calcul tirée des parties A et B.

```
Impact(usage IA) =
    Énergie_calcul (kWh)           # mesure (RAPL/NVML) ou modèle analytique
  × PUE                            # surcoût datacenter : refroidissement, infra
  × Intensité_carbone (gCO₂e/kWh)  # mix électrique, si possible horaire et local
  + Impacts_fabrication amortis    # GPU/CPU/RAM/stockage, au prorata du temps d'usage
  + Eau (L)                        # refroidissement datacenter + eau du mix électrique
```

Sept points de vigilance, avec les sections qui les documentent :

| # | Vigilance | Voir |
|---|---|---|
| 1 | **Déclarer le périmètre.** Entraînement seul ≠ entraînement + inférence + données + réseau + terminal. | A.1, B.4 |
| 2 | **Aller au-delà du carbone.** ADPe et eau changent les conclusions. | A.1, B.1, B.3 |
| 3 | **Amortir la fabrication.** L'*embodied* domine dès que l'usage est court. | A.1, B.3 |
| 4 | **Donner l'incertitude et les sources**, pas un chiffre unique. | B.3, A.5 |
| 5 | **Intensité carbone locale et horaire**, pas une moyenne mondiale. | B.4 |
| 6 | **Séparer mesure et estimation.** Mesurez quand vous avez la machine, modélisez quand vous n'avez qu'une API. | A.2, B.1, B.2 |
| 7 | **S'aligner sur une spec existante.** Le cadre est déjà écrit. | B.5 |

---

## D. Où chercher d'autres sources

Les parties A et B recensent des documents et du code. Cette partie donne les
endroits d'où ils sortent, pour continuer la veille sans repartir d'un moteur de
recherche.

### D.1 Rapports de référence, mis à jour chaque année

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **Stanford HAI, AI Index Report** | Un chapitre entier consacré à l'énergie et à l'environnement : capacité électrique des datacenters d'IA, émissions d'entraînement par modèle, eau d'inférence, écart d'efficacité entre modèles. Le seul suivi annuel chiffré et comparable. | [AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report) · [dossier énergie et environnement](https://hai.stanford.edu/topics/energy-environment) |
| **Agence internationale de l'énergie** | Projections de consommation électrique des datacenters et de l'IA à l'échelle mondiale. La source à citer pour les ordres de grandeur macro. | [Energy and AI](https://www.iea.org/reports/energy-and-ai) |
| **Arcep et ADEME** | Évaluation de l'empreinte environnementale du numérique en France, méthodologie et données publiques. Le référentiel réglementaire français. | [Dossier Arcep](https://www.arcep.fr/la-regulation/grands-dossiers-thematiques-transverses/lempreinte-environnementale-du-numerique.html) |
| **Hugging Face, AI Energy Score** | Classement d'efficacité énergétique des modèles, protocole de mesure publié. Sert à comparer avant de choisir un modèle. | [Leaderboard](https://huggingface.co/spaces/AIEnergyScore/Leaderboard) |

### D.2 Laboratoires qui publient régulièrement

| Laboratoire | Ce qu'on y trouve | Accès |
|---|---|---|
| **MIT Lincoln Laboratory Supercomputing Center** | Mesure et réduction de l'énergie des LLM sur supercalculateur : bridage de puissance des GPU, arrêt anticipé d'entraînement, instrumentation de datacenter. Voir *From Words to Watts*, qui chiffre l'énergie d'inférence. | [LLSC](https://www.ll.mit.edu/r-d/cyber-security-and-information-sciences/lincoln-laboratory-supercomputing-center) · [From Words to Watts](https://arxiv.org/abs/2310.03003) · [MIT Sustainability](https://sustainability.mit.edu/) |
| **Université de Copenhague, département d'informatique** | L'équipe de Raghavendra Selvan, qui a produit `carbontracker` (partie B.1) et travaille sur la *climate-aware AI*. Publications et jeux de mesures accessibles. | [Page de Selvan](https://raghavian.github.io/) · [Actualité DIKU](https://di.ku.dk/english/news/2023/what-can-we-do-about-the-increasing-carbon-footprint-of-ai/) · [Portail de recherche KU](https://researchprofiles.ku.dk/en/publications/carbontracker-tracking-and-predicting-the-carbon-footprint-of-tra/) |
| **Sorbonne Université, LIP6** | Ordonnancement économe, profilage énergétique logiciel et mobile, consommation des services réseau. Plus de 150 dépôts HAL sur le sujet. | [LIP6](https://www.lip6.fr/) · [Portail HAL Sorbonne](https://hal.sorbonne-universite.fr/) |
| **EPFL et Université de Lausanne** | Empreinte du numérique à l'échelle d'un pays et d'un campus, sobriété numérique. L'étude suisse 2025 associe EPFL, UNIL et l'IMD. | [Recherche et durabilité EPFL](https://www.epfl.ch/about/sustainability/research-innovation/) · [Sobriété numérique](https://actu.epfl.ch/news/la-sobriete-numerique-passe-au-rang-des-priorite-2/) · [IGD, UNIL](https://www.unil.ch/igd/home.html) |
| **Ren Research Group** | L'empreinte eau de l'IA, angle le moins couvert ailleurs. Code et données de *Making AI Less Thirsty*. | [Dépôts](https://github.com/Ren-Research) · [Article](https://arxiv.org/abs/2304.03271) |
| **Inria, IRISA, LIG** | Calcul économe, ordonnancement carbone, métrologie sur Grid'5000. Plus de 500 dépôts HAL pour l'IRISA, 200 pour le LIG. | [Portail HAL Inria](https://inria.hal.science/) |
| **CIS CNRS** | Centre Informatique et Société du CNRS. Travaille sur les enjeux sociétaux du numérique. | [Presentation GDR CIS](https://cis.cnrs.fr/presentation-gdr/) |
| **Sorbonne Université** | Travaux sur l'IA et la durabilité, dont l'impact environnemental. | [Dossier IA et société](https://www.sorbonne-universite.fr/dossiers/intelligence-artificielle/lia-dans-leducation-entre-opportunites-et-defis) |

### D.3 Réseaux et portails à interroger directement

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **EcoInfo, groupement de service CNRS** | Le réseau français de l'informatique responsable dans la recherche : guides, calculateurs, retours de terrain. | [ecoinfo.cnrs.fr](https://ecoinfo.cnrs.fr/) |
| **Labos 1point5** | Empreinte carbone des laboratoires de recherche, dont le calcul lié aux moyens informatiques. Outils et données ouvertes. | [labos1point5.org](https://labos1point5.org/) |
| **HAL** | Le moteur derrière la partie A. Interroger par collection de laboratoire donne des résultats plus propres qu'une recherche libre. | [Recherche HAL](https://hal.science/search/index/?q=%22empreinte+carbone%22+IA) |
| **arXiv** | La littérature anglophone, souvent publiée là avant toute revue. Catégories `cs.LG`, `cs.CY` et `cs.DC`. | [arXiv cs.CY](https://arxiv.org/list/cs.CY/recent) |

### D.4 Rapports des opérateurs de datacenters

Ces rapports suivent le GHG Protocol et passent par un audit, ce qui en fait la
source primaire la plus solide sur les infrastructures. Deux limites à garder en
tête : les chiffres agrègent l'IA et le reste de l'activité, et le périmètre
Scope 3 varie d'un opérateur à l'autre.

| Opérateur | Ce qu'on y trouve | Accès |
|---|---|---|
| **Google** | Émissions Scope 1 à 3, part des datacenters, consommation électrique et d'eau, effet de l'IA sur la trajectoire. | [Rapports](https://sustainability.google/reports/) |
| **Microsoft** | Émissions annuelles, construction de datacenters, achats d'électricité renouvelable, projets de captation. Une fiche de données accompagne le rapport. | [Rapport annuel](https://www.microsoft.com/en-us/corporate-responsibility/sustainability/report) |
| **Amazon** | Émissions du groupe, électricité achetée, part des datacenters AWS. | [Reporting](https://sustainability.aboutamazon.com/reporting) |
| **Meta** | Forte croissance du Scope 3, tirée par la fabrication des serveurs et la construction des datacenters. | [Sustainability](https://sustainability.atmeta.com/) |
| **Apple** | Rapports détaillés, utiles pour la méthode de comptabilisation du matériel. | [Environment](https://www.apple.com/environment/) |
| **NVIDIA** | Le Scope 3 dépasse 99 % du total : achats de biens et services, transport amont, usage des produits. La donnée la plus utile pour amortir la fabrication d'un GPU. | [Sustainability](https://www.nvidia.com/en-us/sustainability/) · [Archives des rapports](https://www.nvidia.com/en-gb/foundation/archives/) |
| **Mistral AI** | Le seul éditeur de modèle à publier une ACV produit complète, détaillée en partie A.1. | [Publication](https://mistral.ai/fr/news/our-contribution-to-a-global-environmental-standard-for-ai/) |
| **Greenpeace, analyse critique** | Ce que le reporting de NVIDIA laisse de côté, notamment les émissions d'usage des GPU hors cibles et la concentration des émissions amont en Asie de l'Est. À lire en regard du rapport officiel. | [Analyse](https://www.greenpeace.org/usa/behind-nvidias-record-profits-a-growing-climate-disaster/) |

### D.5 Bases de données et facteurs d'émission

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **ecoinvent** | La base de référence pour l'ACV, avec les procédés liés aux équipements électroniques, aux datacenters et à l'électricité par région. Licence payante. | [ecoinvent.org](https://ecoinvent.org) |
| **Base Empreinte, ADEME** | Facteurs d'émission et jeux de données ACV publics, côté français. | [base-empreinte.ademe.fr](https://base-empreinte.ademe.fr/) |
| **Boavizta** | Impacts de fabrication des équipements, en accès libre et interrogeable par API (partie B.3). | [Données](https://github.com/Boavizta/environmental-footprint-data) |
| **Electricity Maps** | Intensité carbone du réseau, horaire et par zone (partie B.4). | [Dépôt](https://github.com/electricitymaps/electricitymaps-contrib) |

### D.6 Événements, formations et médias spécialisés

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **IA4Dev 2025** | Conférence francophone sur l'IA durable, avec des retours d'expérience et des ateliers pratiques. | [ia4dev-2025.sciencesconf.org](https://ia4dev-2025.sciencesconf.org/resource/page/id/1) |
| **MOOC Fun-MOOC : IA et Société** | Cours en ligne ouvert sur les enjeux sociétaux et environnementaux de l'IA, accessible à tous. | [fun-mooc.fr/IA-et-société](https://www.fun-mooc.fr/fr/cours/intelligence-artificielle-et-societe/) |
| **MOOC INR : IA responsable** | Formation en ligne sur l'IA responsable, abordant les aspects environnementaux et éthiques. | [institut-numerique-responsable.fr](https://institut-numerique-responsable.fr/) |
| **Canal U : Formation ENVOL** | Formation vidéo sur l'IA en aide au développement, incluant des modules sur l'impact environnemental. | [canal-u.tv/ENVOl](https://www.canal-u.tv/chaines/devlog/formation-envol-l-intelligence-artificielle-en-aide-au-developpement) |
| **RAG'AR'ENN** | Réseau breton pour une IA responsable, ressources et événements locaux. | [ragarenn.eskemm-numerique.fr](https://ragarenn.eskemm-numerique.fr/index.html) |
| **Emmy, plateforme vidéo CNRS** | Chaîne dédiée aux conférences et formation sur l'IA et l'environnement. | [emmy.cnrs.fr](https://emmy.cnrs.fr/) |

### D.7 Veille et analyse prospective

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **CaFeIA** | Blog collaboratif sur l'IA frugale et responsable, analyses techniques et retours terrain. | [cafeia.org](https://cafeia.org/) |
| **NMN.gl** | Blog technique sur l'IA et l'apprentissage, avec des analyses sur l'efficacité énergétique. | [nmn.gl/blog/ai-and-learning](https://nmn.gl/blog/ai-and-learning) |
| **Le Grand Continent** | Think tank européen, analyses géopolitiques et technologiques incluant l'IA et ses impacts. | [legrandcontinent.eu/IA-MIT](https://legrandcontinent.eu/fr/2025/06/19/chatgpt-cerveau-etude-mit/) |
| **The Meta News** | Actualités sur l'IA en Europe, couverture des initiatives de recherche responsable. | [themeta.news/mistral-recherche](https://themeta.news/mistral-gagnant-pour-la-recherche/) |
| **IANA Data** | Réflexion sur l'éthique et la société, incluant l'impact cognitif et environnemental des outils d'IA. | [iana-data.org/éthique-IA](https://www.iana-data.org/ethique-et-societe/843-lutilisation-exageree-doutils-dia-altere-les-capacites-cognitives-humaines.html) |
| **DataCamp : Mistral Vibe 2.0** | Article technique sur les outils d'IA générative et leur empreinte, cas d'usage concrets. | [datacamp.com/fr/blog/mistral-vibe-2-0](https://www.datacamp.com/fr/blog/mistral-vibe-2-0) |

### D.8 Sécurité et conformité

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **ANSSI : Assistants de programmation IA** | Recommandations de sécurité pour les outils d'IA générative, bonnes pratiques et risques. | [cyber.gouv.fr/assistants-IA](https://cyber.gouv.fr/actualites/lanssi-et-le-bsi-publient-leurs-recommandations-de-securite-concernant-les-assistants-de-programmationbasés-sur-lia/) |
| **ANSSI : Systèmes d'IA générative** | Cadre de sécurité pour les systèmes d'IA, incluant l'évaluation des risques environnementaux. | [cyber.gouv.fr/recommandations-IA](https://cyber.gouv.fr/publications/recommandations-de-securite-pour-un-systeme-dia-generative) |
| **CNIL : IA et RGPD** | Recommandations pour une innovation responsable, incluant la dimension environnementale. | [cnil.fr/IA-RGPD](https://www.cnil.fr/fr/ia-et-rgpd-la-cnil-publie-ses-nouvelles-recommandations-pour-accompagner-une-innovation-responsable) |
| **Ministère de l'Économie** | Guide RAG v4 interactif sur l'IA générative, incluant les aspects de durabilité. | [entreprises.gouv.fr/guide-RAG](https://www.entreprises.gouv.fr/files/files/Publications/2024/Guides/20241127-bro-guide-ragv4-interactif.pdf) |

### D.9 Ressources communautaires et encyclopédiques

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **Wikipédia : Vibe Coding** | Page encyclopédique sur le *vibe coding*, contexte historique et impact sur les pratiques de développement. | [fr.wikipedia.org/wiki/Vibe_coding](https://fr.wikipedia.org/wiki/Vibe_coding) |
