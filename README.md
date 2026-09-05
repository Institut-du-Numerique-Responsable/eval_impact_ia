# base de ressources & de documents pour un calculateur d'impact environnemental de l'IA

Vous voulez calculer l'impact environnemental d'un usage d'IA : carbone (gCO₂e),
énergie (kWh), eau (L), ressources abiotiques (gSbe). Cette page rassemble la
littérature qui donne la méthode et le code que vous pouvez réutiliser.

**Sommaire**

- [A. Références documentaires](#a-références-documentaires) : méthodes, ordres de grandeur, cadrage
- [B. Ressources logicielles](#b-ressources-logicielles) : briques de code réutilisables
- [C. Structure de calcul qui en découle](#c-structure-de-calcul-qui-en-découle)

HAL publie la méthodologie et les ordres de grandeur validés. GitHub héberge les briques que tout le monde
utilise : CodeCarbon, EcoLogits, Boavizta, Scaphandre, Kepler. GitLab abrite la
recherche publique française (INRIA, IN2P3/CNRS, IRIT) et la coordination
ADEME.

---

## A. Références documentaires

Publications HAL, rangées par brique du calculateur.

### A.1 ACV complète d'un modèle : méthodes de référence

| Référence | Année | Type | Apport |
|---|---|---|---|
| [Life Cycle Assessment of Pre-training the Lucie 7B Open-Source LLM on the Jean Zay Supercomputer](https://hal.science/hal-05685132v1) | 2026 | Rapport | L'ACV complète d'un pré-entraînement réel de LLM sur supercalculateur. La référence la plus proche de l'objectif. |
| [More than carbon: cradle-to-grave environmental impacts of GenAI training on the Nvidia A100 GPU](https://hal.science/hal-05667182v1) | 2026 | Article | Multicritère, du berceau à la tombe, à l'échelle du GPU. Une des rares LCI chiffrées pour cette gamme de matériel. |
| [L'empreinte environnementale complète d'un usage numérique](https://theses.hal.science/tel-04874694v1) | 2024 | Thèse | Cadre ACV pour un service numérique, du terminal au datacenter. |
| [Analysis of the Relationship Between Carbon Footprint and Mineral Resource Depletion in the LCA of Digital Systems](https://hal.science/hal-05631178v1) | 2026 | Communication | Pourquoi ne pas s'arrêter au carbone : le couple GWP / ADPe. |
| [Automating Inventory for LCA of Computing Systems through Machine Vision](https://hal.science/hal-05661956v1) | 2026 | Communication | Automatiser l'inventaire matériel, verrou classique de l'ACV. |

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

### A.4 Cadrage, politiques publiques, effet rebond

| Référence | Année | Type | Apport |
|---|---|---|---|
| [Recommandations pour une action publique en faveur d'une IA générative respectueuse de l'environnement](https://hal.science/hal-04371031v2) | 2023 | Rapport | Cadre la position française sur l'IA générative soutenable. |
| [Promouvoir des modèles d'intelligence artificielle frugale pour et par les politiques publiques](https://hal.science/hal-04510171v1) | 2024 | Rapport | Définit l'IA frugale et ses leviers. |
| [The Environmental Impacts of Machine Learning Training Keep Rising — Evidencing Rebound Effect](https://hal.science/hal-04839926v5) | 2025 | Article | Montre empiriquement que les gains d'efficacité sont absorbés par la hausse des usages. |
| [When rebound effect is not a side effect](https://hal.science/hal-05566029v1) | 2026 | Article | Analyse sociotechnique de l'effet rebond du numérique. |
| [How Hyper-Datafication Impacts the Sustainability Costs in Frontier AI](https://inria.hal.science/hal-05651665v1) | 2026 | Communication (FAccT) | Coûts de soutenabilité liés à l'explosion des données. |

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
confondus. La colonne étoiles donne un ordre de grandeur d'adoption.

### B.1 Estimer l'impact d'un modèle d'IA

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [mlco2/codecarbon](https://github.com/mlco2/codecarbon) | GitHub | 1910 | Émissions d'un calcul Python, entraînement comme inférence : kWh mesurés (RAPL/NVML) × intensité carbone régionale. Décorateur, sortie CSV, dashboard. La brique que tout le monde utilise. |
| [mlco2/ecologits](https://github.com/mlco2/ecologits) | GitHub | 325 | **Impact d'un appel API LLM** sans accès à la machine : énergie, GWP, ADPe estimés depuis les tokens et la taille du modèle. Votre seule option quand vous ne mesurez pas. |
| [saintslab/carbontracker](https://github.com/saintslab/carbontracker) | GitHub | 483 | Mesure **et prédit** l'énergie et le carbone d'un entraînement, par extrapolation dès les premières epochs. |
| [ml-energy/zeus](https://github.com/ml-energy/zeus) | GitHub | 372 | Mesure **et optimise** l'énergie des applications d'IA (arbitrage énergie/temps via DVFS GPU). |
| [Breakend/experiment-impact-tracker](https://github.com/Breakend/experiment-impact-tracker) | GitHub | 293 | Traçage d'expériences ML, avec génération d'un paragraphe d'impact pour publication. |
| [mlco2/impact](https://github.com/mlco2/impact) | GitHub | 270 | ML CO2 Impact : calculateur web historique (Lacoste et al.), formule simple et pédagogique. |
| [Helmholtz-AI-Energy/perun](https://github.com/Helmholtz-AI-Energy/perun) | GitHub | 94 | Énergie d'applications Python, orienté HPC / MPI multi-nœuds. |
| [HewlettPackard/sustain-cluster](https://github.com/HewlettPackard/sustain-cluster) | GitHub | 74 | Environnement Gymnasium pour benchmarker l'ordonnancement durable de clusters IA. |
| [huggingface/AIEnergyScore](https://github.com/huggingface/AIEnergyScore) | GitHub | 41 | **Notation comparable** de l'efficacité énergétique des modèles : méthodologie de benchmark standardisée. |
| [Ren-Research/Making-AI-Less-Thirsty](https://github.com/Ren-Research/Making-AI-Less-Thirsty) | GitHub | 33 | **Empreinte eau de l'IA** : refroidissement et eau du mix électrique. La principale source sur cet axe. |
| [ecs-lab/llm-inference-energy-benchmark](https://gitlab.com/ecs-lab/llm-inference-energy-benchmark) | GitLab | — | **Jeu de mesures** : puissance, traces et débit de 13 LLM (1,3B→9B) sur H100 / TensorRT-LLM. De quoi **calibrer et valider** un modèle analytique (papier *SweetSpot*, ICPE 2026). |
| [inria/magnet/declearn/energy](https://gitlab.inria.fr/magnet/declearn/energy) | GitLab INRIA | — | Consommation d'un framework d'apprentissage fédéré. |

### B.2 Mesurer la consommation électrique

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [hubblo-org/scaphandre](https://github.com/hubblo-org/scaphandre) | GitHub | 1968 | Agent de métrologie énergétique (RAPL, cgroups, VM), exporteur Prometheus. Ce que déploient la plupart des équipes infra. |
| [sustainable-computing-io/kepler](https://github.com/sustainable-computing-io/kepler) | GitHub | 1563 | Énergie par pod/conteneur/nœud **Kubernetes** (eBPF + modèles), exporteur Prometheus. |
| [green-coding-solutions/green-metrics-tool](https://github.com/green-coding-solutions/green-metrics-tool) | GitHub | 254 | Banc de mesure complet : énergie et émissions d'un logiciel, timelines, intégration git, comparaison de versions. |
| [powerapi-ng/powerapi](https://github.com/powerapi-ng/powerapi) | GitHub | 253 | Framework de construction de *software-defined power meters*. Voir [smartwatts-formula](https://github.com/powerapi-ng/smartwatts-formula) (modèle auto-adaptatif) et [pyJoules](https://github.com/powerapi-ng/pyJoules) (énergie d'un bloc de code). |
| [joular/powerjoular](https://github.com/joular/powerjoular) | GitHub | 117 | Consommation **par processus**, multi-plateformes (RAPL + Nvidia). [joularjx](https://github.com/joular/joularjx) descend au niveau du code source Java. |
| [tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge) | GitHub | 37 | Mesure multiplateforme (Linux/macOS/Windows, Intel/AMD/Apple Silicon), là où RAPL ne suffit pas. |
| [kajalv/nvml-power](https://github.com/kajalv/nvml-power) | GitHub | 26 | Puissance GPU par polling NVML. La brique GPU minimale. |
| [irit/sepia-pub/expetator](https://gitlab.irit.fr/sepia-pub/expetator) | GitLab IRIT | — | Campagnes de benchmarks HPC avec leviers DVFS et monitoring bas niveau (compteurs matériels, RAPL) sur Grid'5000. |
| [sosy-lab/cpu-energy-meter](https://gitlab.com/sosy-lab/software/cpu-energy-meter) | GitLab | — | Énergie CPU Intel via RAPL. Petit, auditable. |
| [inria/majay/energy-consumption-of-gpu-benchmarks](https://gitlab.inria.fr/majay/energy-consumption-of-gpu-benchmarks) | GitLab INRIA | — | Compare les outils de mesure de consommation GPU et tranche entre eux. |
| [inria/mbelgaid/python-energy](https://gitlab.inria.fr/mbelgaid/python-energy) | GitLab INRIA | — | Énergie induite par les outils d'optimisation Python (transpileurs, JIT). |
| [inria/delamare/tutoriel-mesure-energie-wid2](https://gitlab.inria.fr/delamare/tutoriel-mesure-energie-wid2) | GitLab INRIA | — | **Tutoriel** de mesure d'énergie. Point de départ pédagogique. |

### B.3 Estimer les impacts de fabrication (ACV matérielle)

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [in2p3/impacts-hpc](https://gitlab.in2p3.fr/impacts-hpc/impacts-hpc) | GitLab IN2P3 | — | Librairie Python qui estime l'impact d'un *job* datacenter en GWP, ADPe et énergie primaire, et rend chaque résultat **explicable, sourcé et assorti de son incertitude**. Le modèle à copier. [Documentation](https://impacthpc-cc8227.pages.in2p3.fr/index.html) · [ontologie](https://gitlab.in2p3.fr/impacts-hpc/ontology-impactshpc) |
| [Boavizta/environmental-footprint-data](https://github.com/Boavizta/environmental-footprint-data) | GitHub | 130 | Base ouverte des impacts environnementaux d'équipements, issue des fiches constructeurs. |
| [Boavizta/boaviztapi](https://github.com/Boavizta/boaviztapi) | GitHub | 99 | **API des impacts de fabrication** (serveur, CPU, GPU, RAM, SSD) : GWP, ADPe, PE. Couvre l'*embodied* que CodeCarbon ignore. |
| [cloud-carbon-footprint/cloud-carbon-coefficients](https://github.com/cloud-carbon-footprint/cloud-carbon-coefficients) | GitHub | 45 | Notebooks qui dérivent les coefficients énergie/carbone du cloud. Ils exposent **la méthode**, pas seulement le résultat. |
| [in2p3/ecoinfo/ecodiag](https://gitlab.in2p3.fr/ecoinfo/ecodiag) | GitLab IN2P3 | — | Bilan carbone d'un parc IT par approche ACV matériel. Daté, mais le modèle se lit facilement. |

### B.4 Convertir en carbone : intensité électrique et cloud

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [electricitymaps/electricitymaps-contrib](https://github.com/electricitymaps/electricitymaps-contrib) | GitHub | 4032 | Parsers open source de l'**intensité carbone du réseau** mondial. Fournit le gCO₂e/kWh horaire et localisé. |
| [cloud-carbon-footprint/cloud-carbon-footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) | GitHub | 1050 | kWh + tCO₂e à partir des factures AWS/GCP/Azure. [Plugin Backstage](https://github.com/cloud-carbon-footprint/ccf-backstage-plugin) disponible. |
| [Green-Software-Foundation/carbon-aware-sdk](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | GitHub | 592 | SDK pour décaler ou placer un calcul selon l'intensité carbone. |
| [Green-Software-Foundation/real-time-cloud](https://github.com/Green-Software-Foundation/real-time-cloud) | GitHub | 75 | Standards de données énergie/carbone temps réel pour les fournisseurs cloud. |
| [GoogleCloudPlatform/region-picker](https://github.com/GoogleCloudPlatform/region-picker) | GitHub | 69 | Choix d'une région cloud arbitrant carbone, prix et latence. |
| [Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC](https://github.com/Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC) | GitHub | 73 | Rapport énergie + carbone de ses jobs Slurm. Pendant HPC de Green Algorithms. |
| [fledee/ecodynelec](https://gitlab.com/fledee/ecodynelec) | GitLab | — | Impacts de l'électricité européenne en **suivant les flux entre pays**, donc sur le mix réellement consommé. |
| [elioth/dynco2](https://gitlab.com/elioth/dynco2) | GitLab | — | Forçage radiatif instantané d'une série d'émissions (modèle DynCO2), pour aller au-delà du gCO₂e. |
| [meltano/tap-carbon-intensity](https://gitlab.com/meltano/tap-carbon-intensity) | GitLab | — | Connecteur vers l'API Carbon Intensity (UK). |
| [inria/mlanvin/compute_carbon_footprint_g5k](https://gitlab.inria.fr/mlanvin/compute_carbon_footprint_g5k) | GitLab INRIA | — | Carbone d'un job Grid'5000. Le modèle reste simple (puissance ∝ usage CPU, bornée au TDP) et **documente son périmètre et ses exclusions**. |

### B.5 Normaliser le calcul

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [Green-Software-Foundation/sci](https://github.com/Green-Software-Foundation/sci) | GitHub | 296 | **Software Carbon Intensity** : spécification normative, `SCI = (E × I + M) / R`. Cadre de référence pour structurer un calculateur. |
| [Green-Software-Foundation/if](https://github.com/Green-Software-Foundation/if) | GitHub | 183 | Impact Framework : pipeline déclaratif (YAML) composé de plugins. L'architecture dont s'inspirer pour l'outil à construire. |

### B.6 Intégrer à la CI/CD et à l'ordonnancement

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) | GitHub | 186 | Empreinte carbone de **sessions d'agent de code**, le cas d'usage voisin du nôtre. |
| [green-coding-solutions/eco-ci-energy-estimation](https://github.com/green-coding-solutions/eco-ci-energy-estimation) | GitHub | 116 | Estimation d'énergie dans GitHub Actions, GitLab CI et Jenkins. |
| [GreenScheduler/cats](https://github.com/GreenScheduler/cats) | GitHub | 79 | Climate-Aware Task Scheduler : décale un job vers un créneau bas carbone. |
| [Institut-du-Numerique-Responsable/green-claude](https://github.com/Institut-du-Numerique-Responsable/green-claude) | GitHub | 45 | Skill d'éco-conception (RGESN, GR491, Green Software) pour Claude Code. |
| [deepshotinc/gitgreen](https://gitlab.com/deepshotinc/gitgreen) | GitLab | — | CI/CD *carbon-aware* pour GitLab sur GCP. [Version auto-hébergée](https://gitlab.com/deepshotinc/gitgreen-server). |
| [youneslaaroussi/duoops](https://gitlab.com/youneslaaroussi/duoops) | GitLab | — | CLI et portail de transparence des pipelines GitLab, volet émissions inclus. |
| [dimasna96/greenstatus](https://gitlab.com/dimasna96/greenstatus) | GitLab | — | Composant CI/CD : tests d'API + calcul CO₂, rapport publié sur GitLab Pages. |
| [demeringo/scaphandre-runner](https://gitlab.com/demeringo/scaphandre-runner) | GitLab | — | Exécution de Scaphandre dans GitLab CI. |
| [sustainable-computing-systems/carbond](https://gitlab.com/sustainable-computing-systems/carbond) | GitLab | — | Démon système pour la *carbon awareness*. |

### B.7 Mesurer côté service numérique

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [marmelab/greenframe-cli](https://github.com/marmelab/greenframe-cli) | GitHub | 283 | Empreinte carbone d'un **scénario utilisateur** sur une application web. Mesure conteneurisée réelle, sans modèle intermédiaire. |
| [green-code-initiative/creedengo-rules-specifications](https://github.com/green-code-initiative/creedengo-rules-specifications) | GitHub | 216 | Règles d'écoconception logicielle pour SonarQube (ex-ecoCode). |
| [cnumr/EcoIndex](https://github.com/cnumr/EcoIndex) | GitHub | 92 | EcoIndex : score environnemental d'une page web. Voir [EcoIndex_python](https://github.com/cnumr/EcoIndex_python). |
| [green-code-initiative/EcoSonar](https://github.com/green-code-initiative/EcoSonar) | GitHub | 59 | Audit d'écoconception intégré à la CI. |
| [wholegrain/carbon-api-2-0](https://gitlab.com/wholegrain/carbon-api-2-0) | GitLab | 46 | API Website Carbon. Dépréciée, mais son modèle de calcul se lit facilement. |
| [wholegrain/website-carbon-badges](https://gitlab.com/wholegrain/website-carbon-badges) | GitLab | 40 | Badges d'émissions d'une page web. |
| [gibbonjoyeux/bare-tracker-extension](https://gitlab.com/gibbonjoyeux/bare-tracker-extension) | GitLab | — | Extension navigateur exposant l'impact de la navigation. |

### B.8 Communs, guides et listes curées

| Ressource | Plateforme | ⭐ | Apport |
|---|---|---:|---|
| [aac-ademe/consortium-ia-durable](https://gitlab.com/aac-ademe/consortium-ia-durable) | GitLab | — | Commun numérique ADEME qui coordonne CodeCarbon et EcoLogits, publie un [guide IA durable](https://challengedata.ens.fr/ia_durable/guide) et anime un espace de formation (branche `toy_projects_fr`). Le point d'entrée côté français. |
| [samuelrince/awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) | GitHub | 114 | Liste curée d'outils et ressources Green AI, pour prolonger la veille. |
| [schaDev/GreenCoding-measuring-tools](https://github.com/schaDev/GreenCoding-measuring-tools) | GitHub | 47 | Panorama comparatif des outils de mesure énergie/CO₂ des logiciels. |
| [in2p3/ecoinfo/bonnes-pratiques](https://gitlab.in2p3.fr/ecoinfo/bonnes-pratiques) | GitLab IN2P3 | — | Guide EcoInfo (CNRS) de bonnes pratiques pour l'informatique de l'ESR. |
| [aac-ademe](https://gitlab.com/aac-ademe) | GitLab | — | Groupe complet des appels à communs ADEME, dont `datacenter-footprint`. |

---

## C. Structure de calcul qui en découle

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

