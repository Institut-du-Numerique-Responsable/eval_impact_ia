# base de ressources & de documents pour un calculateur d'impact environnemental de l'IA

[![Licence CC0 1.0](https://img.shields.io/badge/licence-CC0_1.0-6a9955?style=flat-square)](LICENSE)
[![44 références](https://img.shields.io/badge/références-44_publications-2c6e9b?style=flat-square)](#a-références-documentaires)
[![62 ressources logicielles](https://img.shields.io/badge/ressources-62_dépôts-2c6e9b?style=flat-square)](#b-ressources-logicielles)
[![Indicateurs CO2e kWh eau ADPe](https://img.shields.io/badge/indicateurs-gCO₂e_·_kWh_·_eau_·_ADPe-4c8c4a?style=flat-square)](#c-proposition-de-méthodologie)
[![Dernière mise à jour](https://img.shields.io/github/last-commit/Institut-du-Numerique-Responsable/eval_impact_ia?style=flat-square&label=mise%20à%20jour&color=888888)](https://github.com/Institut-du-Numerique-Responsable/eval_impact_ia/commits/main)

Construire un calculateur d'impact environnemental de l'IA demande deux choses :
une méthode et des briques de code. Cette page rassemble les deux, pour quatre
indicateurs : carbone (gCO₂e), énergie (kWh), eau (L), ressources abiotiques
(gSbe).

- [A. Références documentaires](#a-références-documentaires) : la méthode, les ordres de grandeur, le cadrage. Publications HAL.
- [B. Ressources logicielles](#b-ressources-logicielles) : les briques réutilisables. Dépôts GitHub et GitLab.
- [C. Proposition de méthodologie](#c-proposition-de-méthodologie) : la synthèse de calcul et les sept points de vigilance.
- [D. Où chercher d'autres sources](#d-où-chercher-dautres-sources) : laboratoires, portails et rapports de référence.

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
| [From Words to Watts: Benchmarking the Energy Costs of Large Language Model Inference](https://arxiv.org/abs/2310.03003) | 2023 | Préprint | Le MIT Lincoln Laboratory mesure l'énergie d'inférence des LLM sur supercalculateur, par taille de modèle et par configuration. |
| [Power Hungry Processing: Watts Driving the Cost of AI Deployment?](https://arxiv.org/abs/2311.16863) | 2023 | Préprint | Hugging Face compare l'énergie d'inférence selon la tâche : la génération d'image coûte des ordres de grandeur de plus que la classification. |
| [Great Power, Great Responsibility: Recommendations for Reducing Energy for Training Language Models](https://arxiv.org/abs/2205.09646) | 2022 | Préprint | Le MIT chiffre les gains du bridage de puissance des GPU et de l'arrêt anticipé d'entraînement. |
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
| [Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models](https://arxiv.org/abs/2304.03271) | 2023 | Préprint | Le Ren Research Group (UC Riverside) sépare l'eau consommée sur site pour le refroidissement de celle consommée hors site pour produire l'électricité. La principale source sur l'axe eau. |

### A.4 Cadrage, politiques publiques, effet rebond

| Référence | Année | Type | Apport |
|---|---|---|---|
| [Recommandations pour une action publique en faveur d'une IA générative respectueuse de l'environnement](https://hal.science/hal-04371031v2) | 2023 | Rapport | Cadre la position française sur l'IA générative soutenable. |
| [Promouvoir des modèles d'intelligence artificielle frugale pour et par les politiques publiques](https://hal.science/hal-04510171v1) | 2024 | Rapport | Définit l'IA frugale et ses leviers. |
| [The Environmental Impacts of Machine Learning Training Keep Rising — Evidencing Rebound Effect](https://hal.science/hal-04839926v5) | 2025 | Article | Montre empiriquement que les gains d'efficacité sont absorbés par la hausse des usages. |
| [When rebound effect is not a side effect](https://hal.science/hal-05566029v1) | 2026 | Article | Analyse sociotechnique de l'effet rebond du numérique. |
| [How Hyper-Datafication Impacts the Sustainability Costs in Frontier AI](https://inria.hal.science/hal-05651665v1) | 2026 | Communication (FAccT) | Coûts de soutenabilité liés à l'explosion des données. |
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
| [samuelrince/awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) | GitHub | Liste curée d'outils et ressources Green AI, pour prolonger la veille. |
| [schaDev/GreenCoding-measuring-tools](https://github.com/schaDev/GreenCoding-measuring-tools) | GitHub | Panorama comparatif des outils de mesure énergie/CO₂ des logiciels. |
| [in2p3/ecoinfo/bonnes-pratiques](https://gitlab.in2p3.fr/ecoinfo/bonnes-pratiques) | GitLab IN2P3 | Guide EcoInfo (CNRS) de bonnes pratiques pour l'informatique de l'ESR. |
| [aac-ademe](https://gitlab.com/aac-ademe) | GitLab | Groupe complet des appels à communs ADEME, dont `datacenter-footprint`. |

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

### D.3 Réseaux et portails à interroger directement

| Source | Ce qu'on y trouve | Accès |
|---|---|---|
| **EcoInfo, groupement de service CNRS** | Le réseau français de l'informatique responsable dans la recherche : guides, calculateurs, retours de terrain. | [ecoinfo.cnrs.fr](https://ecoinfo.cnrs.fr/) |
| **Labos 1point5** | Empreinte carbone des laboratoires de recherche, dont le calcul lié aux moyens informatiques. Outils et données ouvertes. | [labos1point5.org](https://labos1point5.org/) |
| **HAL** | Le moteur derrière la partie A. Interroger par collection de laboratoire donne des résultats plus propres qu'une recherche libre. | [Recherche HAL](https://hal.science/search/index/?q=%22empreinte+carbone%22+IA) |
| **arXiv** | La littérature anglophone, souvent publiée là avant toute revue. Catégories `cs.LG`, `cs.CY` et `cs.DC`. | [arXiv cs.CY](https://arxiv.org/list/cs.CY/recent) |
