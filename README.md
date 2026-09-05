# eval_CO2_IA — base de code & de documents pour un calculateur d'impact environnemental de l'IA

Objectif : réunir **le code existant** (GitLab en priorité) et **la littérature**
(HAL) nécessaires pour apprendre à construire un calculateur d'impact
environnemental de l'IA — carbone (gCO₂e), à défaut énergie (kWh), eau (L) et
ressources abiotiques (gSbe).

---

## Où vit quoi

L'écosystème « empreinte de l'IA » se répartit très inégalement :

- **GitHub** — les briques logicielles de fait : CodeCarbon, EcoLogits, Boavizta,
  Scaphandre, Kepler, Zeus, carbontracker. C'est là qu'on prend le code.
- **GitLab** — la **recherche publique française** (INRIA, IN2P3/CNRS, IRIT :
  mesure d'énergie HPC, ACV datacenter), la **coordination ADEME**, des briques
  CI/CD. C'est là qu'on prend les modèles explicables et les jeux de mesures.
- **HAL** — la méthodologie et les ordres de grandeur validés.

---

## A. Code — GitLab

### A.1 — Coordination & communs (le point d'entrée)

| Projet | Ce que c'est |
|---|---|
| [aac-ademe/consortium-ia-durable](https://gitlab.com/aac-ademe/consortium-ia-durable) ⭐ | **Commun numérique ADEME** sur les librairies open-source d'évaluation de l'empreinte du numérique et de l'IA générative. Coordonne CodeCarbon et EcoLogits, publie un [guide IA durable](https://challengedata.ens.fr/ia_durable/guide) et un espace de formation (branche `toy_projects_fr`). **À lire en premier.** |
| [aac-ademe (groupe complet)](https://gitlab.com/aac-ademe) | Autres appels à communs ADEME, dont `datacenter-footprint`. |
| [in2p3/ecoinfo/bonnes-pratiques](https://gitlab.in2p3.fr/ecoinfo/bonnes-pratiques) | Guide EcoInfo (CNRS) de bonnes pratiques environnementales pour l'informatique de l'ESR. |

### A.2 — Estimation d'impact d'un calcul (le cœur du calculateur)

| Projet | Ce que c'est |
|---|---|
| [in2p3/impacts-hpc](https://gitlab.in2p3.fr/impacts-hpc/impacts-hpc) ⭐ | **Librairie Python** estimant l'impact environnemental d'un *job* sur un datacenter : GWP (gCO₂e), ADPe (gSbe), énergie primaire (MJ). Résultats **explicables, sourcés, avec incertitudes**, et tolérants à des données d'entrée de précision variable. Modèle de référence pour ce projet. [Doc](https://impacthpc-cc8227.pages.in2p3.fr/index.html) · [ontologie associée](https://gitlab.in2p3.fr/impacts-hpc/ontology-impactshpc) |
| [inria/mlanvin/compute_carbon_footprint_g5k](https://gitlab.inria.fr/mlanvin/compute_carbon_footprint_g5k) | Estimation carbone d'un job Grid'5000. Modèle simple et lisible : puissance ∝ usage CPU, bornée par le TDP ; documente explicitement ce qu'il **exclut** (fabrication, refroidissement, serveurs d'infra) — bon exemple de périmètre déclaré. |
| [gitlab.com/ecs-lab/llm-inference-energy-benchmark](https://gitlab.com/ecs-lab/llm-inference-energy-benchmark) ⭐ | **Jeu de données de mesures** : puissance, traces temporelles et débit de 13 LLM (1,3B→9B) sur H100 / TensorRT-LLM, selon longueurs de contexte et batch. Support du papier *SweetSpot* (ICPE 2026). Utile pour **calibrer et valider** un modèle analytique d'énergie d'inférence. |
| [inria/majay/energy-consumption-of-gpu-benchmarks](https://gitlab.inria.fr/majay/energy-consumption-of-gpu-benchmarks) | Comparaison des outils logiciels de mesure de conso GPU — quel *power meter* croire. |
| [inria/magnet/declearn/energy](https://gitlab.inria.fr/magnet/declearn/energy) | Conso énergétique d'un framework d'apprentissage fédéré. |
| [in2p3/ecoinfo/ecodiag](https://gitlab.in2p3.fr/ecoinfo/ecodiag) | Calculateur web du bilan carbone d'un parc IT (approche ACV matériel). Ancien mais le modèle est lisible. |
| [gitlab.com/cloud-carbon-footprint (miroirs)](https://gitlab.com/rbn-djx/cloud-carbon-footprint) | Miroir GitLab de Cloud Carbon Footprint : kWh + tCO₂e à partir des factures cloud AWS/GCP/Azure. |

### A.3 — Mesure de la consommation électrique (la donnée d'entrée)

| Projet | Ce que c'est |
|---|---|
| [gitlab.com/joular/powerjoular](https://gitlab.com/joular/powerjoular) | Monitoring de puissance multi-plateformes **par processus** (RAPL, Nvidia). Miroir ; upstream sur GitHub. |
| [sosy-lab/software/cpu-energy-meter](https://gitlab.com/sosy-lab/software/cpu-energy-meter) | Mesure de l'énergie CPU Intel via RAPL. Petit, auditable. |
| [irit/sepia-pub/expetator](https://gitlab.irit.fr/sepia-pub/expetator) | Campagnes de benchmarks HPC avec leviers DVFS et monitoring bas niveau (compteurs matériels, RAPL), sur Grid'5000. |
| [inria/htayeb/kepler](https://gitlab.inria.fr/htayeb/kepler) | Kepler : exporter Prometheus de la conso énergétique par conteneur/pod/nœud Kubernetes. |
| [inria/mbelgaid/python-energy](https://gitlab.inria.fr/mbelgaid/python-energy) | Mesure de l'énergie induite par différents outils d'optimisation Python (transpileurs, JIT). |
| [inria/lsiffre/service-energy-monitor](https://gitlab.inria.fr/lsiffre/service-energy-monitor) | Monitoring énergétique orienté service. |
| [inria/delamare/tutoriel-mesure-energie-wid2](https://gitlab.inria.fr/delamare/tutoriel-mesure-energie-wid2) | **Tutoriel** de mesure d'énergie — bon point de départ pédagogique. |
| [demeringo/scaphandre-runner](https://gitlab.com/demeringo/scaphandre-runner) | Exécution de Scaphandre dans GitLab CI. |

### A.4 — Carbone dans la CI/CD (mesurer l'IA qu'on entraîne… et le reste)

| Projet | Ce que c'est |
|---|---|
| [deepshotinc/gitgreen](https://gitlab.com/deepshotinc/gitgreen) · [gitgreen-server](https://gitlab.com/deepshotinc/gitgreen-server) | CI/CD *carbon-aware* pour GitLab sur GCP ; version auto-hébergée du suivi carbone. |
| [youneslaaroussi/gitgreen](https://gitlab.com/youneslaaroussi/gitgreen) · [duoops](https://gitlab.com/youneslaaroussi/duoops) | Suivi des émissions des pipelines GitLab CI (runners GCP/AWS) ; CLI + portail. |
| [dimasna96/greenstatus](https://gitlab.com/dimasna96/greenstatus) | Composant GitLab CI/CD : tests d'API + calcul des émissions CO₂, rapport publié sur GitLab Pages. |
| [demeringo/typescript-starter](https://gitlab.com/demeringo/typescript-starter) | Démo de mesure de conso énergétique en CI, comparée entre branches. |
| [kamalbuilds/ecoguardian](https://gitlab.com/kamalbuilds/ecoguardian) | Orchestrateur SDLC carbon-aware (intensité carbone temps réel via MCP). |
| [sustainable-computing-systems/carbond](https://gitlab.com/sustainable-computing-systems/carbond) | Démon OS pour la *carbon awareness*. |
| [boonen/greener-software-development](https://gitlab.com/boonen/greener-software-development) | Vitrine de pratiques de dev sobres + mesure de la conso du logiciel. |

### A.5 — Intensité carbone de l'électricité (le facteur de conversion kWh → gCO₂e)

| Projet | Ce que c'est |
|---|---|
| [fledee/ecodynelec](https://gitlab.com/fledee/ecodynelec) | Package Python calculant les impacts environnementaux de l'électricité européenne en **suivant les flux entre pays** (mix réel, pas mix national). |
| [meltano/tap-carbon-intensity](https://gitlab.com/meltano/tap-carbon-intensity) | Connecteur vers l'API Carbon Intensity (UK). |
| [hotmaps/.../electricity_emissions_hourly](https://gitlab.com/hotmaps/electricity/load_electricity/electricity_emissions_hourly) | Émissions CO₂ horaires du secteur électrique. |
| [elioth/dynco2](https://gitlab.com/elioth/dynco2) | Forçage radiatif instantané de séries temporelles d'émissions (modèle DynCO2) — pour aller au-delà du simple gCO₂e. |

### A.6 — Écoconception web / mesure côté usage

| Projet | Ce que c'est |
|---|---|
| [wholegrain/website-carbon-badges](https://gitlab.com/wholegrain/website-carbon-badges) | Badges d'émissions d'une page web. |
| [wholegrain/carbon-api-2-0](https://gitlab.com/wholegrain/carbon-api-2-0) | API Website Carbon (déprécié, modèle de calcul lisible). |
| [gibbonjoyeux/bare-tracker-extension](https://gitlab.com/gibbonjoyeux/bare-tracker-extension) | Extension navigateur exposant l'impact environnemental de la navigation. |
| [i-have-a-green/plugin-ecoindex](https://gitlab.com/i-have-a-green/plugin-ecoindex) | Intégration EcoIndex (WordPress). |

## B. Code — GitHub

### B.1 — Estimation de l'impact d'un modèle d'IA (le cœur du sujet)

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [mlco2/codecarbon](https://github.com/mlco2/codecarbon) | 1910 | **La référence.** Traque les émissions d'un calcul Python (entraînement comme inférence) : kWh mesurés (RAPL/NVML) × intensité carbone régionale. Décorateur/contexte, sortie CSV, dashboard. |
| [mlco2/ecologits](https://github.com/mlco2/ecologits) | 325 | **Impact d'un appel API LLM** (OpenAI, Anthropic, Mistral…) sans accès à la machine : énergie, GWP, ADPe estimés depuis le nombre de tokens et la taille du modèle. Indispensable quand on ne mesure pas. |
| [saintslab/carbontracker](https://github.com/saintslab/carbontracker) | 483 | Mesure **et prédit** l'énergie et l'empreinte carbone d'un entraînement de deep learning (extrapolation dès les premières epochs). |
| [ml-energy/zeus](https://github.com/ml-energy/zeus) | 372 | Mesure **et optimise** l'énergie des applications d'IA (arbitrage énergie/temps via DVFS GPU). |
| [mlco2/impact](https://github.com/mlco2/impact) | 270 | ML CO2 Impact : calculateur web historique (Lacoste et al.), formule simple et pédagogique. |
| [Breakend/experiment-impact-tracker](https://github.com/Breakend/experiment-impact-tracker) | 293 | Traçage de l'impact d'expériences ML, avec génération automatique d'un paragraphe d'impact pour un papier. |
| [Helmholtz-AI-Energy/perun](https://github.com/Helmholtz-AI-Energy/perun) | 94 | Mesure d'énergie d'applications Python, orientée HPC / MPI multi-nœuds. |
| [huggingface/AIEnergyScore](https://github.com/huggingface/AIEnergyScore) | 41 | **Notation comparable** de l'efficacité énergétique des modèles d'IA — méthodologie de benchmark standardisée. |
| [Ren-Research/Making-AI-Less-Thirsty](https://github.com/Ren-Research/Making-AI-Less-Thirsty) | 33 | **Empreinte eau de l'IA** — la référence sur l'axe eau (eau de refroidissement + eau du mix électrique). Rare et central ici. |
| [HewlettPackard/sustain-cluster](https://github.com/HewlettPackard/sustain-cluster) | 74 | Environnement Gymnasium pour benchmarker l'ordonnancement multi-objectif durable de clusters IA. |
| [samuelrince/awesome-green-ai](https://github.com/samuelrince/awesome-green-ai) | 114 | **Liste curée** d'outils et ressources Green AI — bon complément de veille à ce README. |

### B.2 — Métrologie énergie (la donnée d'entrée)

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [hubblo-org/scaphandre](https://github.com/hubblo-org/scaphandre) | 1968 | Agent de métrologie énergétique (RAPL, cgroups, VM), exporteur Prometheus. Standard de fait côté infra. |
| [sustainable-computing-io/kepler](https://github.com/sustainable-computing-io/kepler) | 1563 | Énergie par pod/conteneur/nœud **Kubernetes**, exporteur Prometheus (eBPF + modèles). |
| [powerapi-ng/powerapi](https://github.com/powerapi-ng/powerapi) | 253 | Framework Python de construction de *software-defined power meters*. Voir aussi [smartwatts-formula](https://github.com/powerapi-ng/smartwatts-formula) (modèle auto-adaptatif) et [pyJoules](https://github.com/powerapi-ng/pyJoules) (énergie d'un bloc de code). |
| [joular/powerjoular](https://github.com/joular/powerjoular) | 117 | Conso **par processus**, multi-plateformes (RAPL + Nvidia). [joularjx](https://github.com/joular/joularjx) fait la même chose au niveau du code source Java. |
| [tdurieux/EnergiBridge](https://github.com/tdurieux/EnergiBridge) | 37 | Mesure d'énergie multiplateforme (Linux/macOS/Windows, Intel/AMD/Apple Silicon) — utile là où RAPL ne suffit pas. |
| [kajalv/nvml-power](https://github.com/kajalv/nvml-power) | 26 | Mesure de puissance GPU par polling NVML — la brique GPU minimale. |
| [green-coding-solutions/green-metrics-tool](https://github.com/green-coding-solutions/green-metrics-tool) | 254 | Banc de mesure complet : énergie et émissions d'un logiciel, timelines, intégration git, comparaison de versions. |

### B.3 — Impacts de fabrication et ACV matérielle

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [Boavizta/boaviztapi](https://github.com/Boavizta/boaviztapi) | 99 | **API des impacts de fabrication** (serveur, CPU, GPU, RAM, SSD) : GWP, ADPe, PE. La brique *embodied* qui manque à CodeCarbon. |
| [Boavizta/environmental-footprint-data](https://github.com/Boavizta/environmental-footprint-data) | 130 | Base de données ouverte des impacts environnementaux d'équipements (issue des fiches constructeurs). |
| [cloud-carbon-footprint/cloud-carbon-coefficients](https://github.com/cloud-carbon-footprint/cloud-carbon-coefficients) | 45 | Notebooks de dérivation des coefficients énergie/carbone du cloud — **la méthode, pas seulement le résultat**. |

### B.4 — Cloud, datacenter, intensité carbone

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [cloud-carbon-footprint/cloud-carbon-footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) | 1050 | kWh + tCO₂e à partir des factures AWS/GCP/Azure. [Plugin Backstage](https://github.com/cloud-carbon-footprint/ccf-backstage-plugin) disponible. |
| [electricitymaps/electricitymaps-contrib](https://github.com/electricitymaps/electricitymaps-contrib) | 4032 | Parsers open source de l'**intensité carbone du réseau électrique** mondial — la donnée gCO₂e/kWh, horaire et localisée. |
| [Green-Software-Foundation/carbon-aware-sdk](https://github.com/Green-Software-Foundation/carbon-aware-sdk) | 592 | SDK pour décaler/placer un calcul selon l'intensité carbone. |
| [Green-Software-Foundation/real-time-cloud](https://github.com/Green-Software-Foundation/real-time-cloud) | 75 | Standards de données énergie/carbone temps réel pour les fournisseurs cloud. |
| [GoogleCloudPlatform/region-picker](https://github.com/GoogleCloudPlatform/region-picker) | 69 | Choix d'une région cloud arbitrant carbone / prix / latence. |
| [Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC](https://github.com/Cambridge-Sustainable-Computing-Lab/GreenAlgorithms4HPC) | 73 | Rapport énergie + carbone de ses jobs sur un cluster HPC (Slurm). Pendant HPC de Green Algorithms. |

### B.5 — Normalisation et cadres de calcul

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [Green-Software-Foundation/sci](https://github.com/Green-Software-Foundation/sci) | 296 | **Software Carbon Intensity** : spécification normative du calcul d'intensité carbone d'un logiciel (`SCI = (E×I + M) / R`). Cadre de référence pour structurer un calculateur. |
| [Green-Software-Foundation/if](https://github.com/Green-Software-Foundation/if) | 183 | Impact Framework : pipeline déclaratif (YAML) de calcul d'impact, composable à partir de plugins. **Architecture inspirante** pour l'outil à construire. |

### B.6 — CI/CD et ordonnancement

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [green-coding-solutions/eco-ci-energy-estimation](https://github.com/green-coding-solutions/eco-ci-energy-estimation) | 116 | Estimation d'énergie dans GitHub Actions, GitLab CI et Jenkins. |
| [GreenScheduler/cats](https://github.com/GreenScheduler/cats) | 79 | Climate-Aware Task Scheduler : décale un job vers un créneau à faible intensité carbone. |
| [gwittebolle/claude-carbon](https://github.com/gwittebolle/claude-carbon) | 186 | Suivi de l'empreinte carbone de **sessions d'agent de code** (Claude Code) — cas d'usage très proche de l'objectif. |
| [Institut-du-Numerique-Responsable/green-claude](https://github.com/Institut-du-Numerique-Responsable/green-claude) | 45 | Skill d'éco-conception (RGESN, GR491, Green Software) pour Claude Code. |

### B.7 — Écoconception des services numériques

| Projet | ⭐ | Ce que c'est |
|---|---:|---|
| [marmelab/greenframe-cli](https://github.com/marmelab/greenframe-cli) | 283 | Empreinte carbone d'un **scénario utilisateur** sur une application web (mesure conteneurisée, pas modèle). |
| [green-code-initiative/creedengo-rules-specifications](https://github.com/green-code-initiative/creedengo-rules-specifications) | 216 | Règles d'écoconception logicielle pour SonarQube (ex-ecoCode). |
| [green-code-initiative/EcoSonar](https://github.com/green-code-initiative/EcoSonar) | 59 | Outil d'audit d'écoconception intégré à la CI. |
| [cnumr/EcoIndex](https://github.com/cnumr/EcoIndex) | 92 | EcoIndex : score environnemental d'une page web. Voir [EcoIndex_python](https://github.com/cnumr/EcoIndex_python). |

## C. Publications (HAL)

Rangées par **brique du calculateur** à construire.

### C.1 — Méthodes de référence : ACV complète d'un modèle

- **Life Cycle Assessment of Pre-training the Lucie 7B Open-Source LLM on the Jean Zay Supercomputer** (2026, rapport) — ACV complète d'un pré-entraînement réel de LLM sur supercalculateur. **La référence méthodo la plus proche de l'objectif.** <https://hal.science/hal-05685132v1>
- **More than carbon: cradle-to-grave environmental impacts of GenAI training on the Nvidia A100 GPU** (2026) — multicritère, du berceau à la tombe, à l'échelle du GPU. <https://hal.science/hal-05667182v1>
- **L'empreinte environnementale complète d'un usage numérique : contribution à l'ACV de services numériques** (2024, thèse) — cadre ACV complet pour un service numérique. <https://theses.hal.science/tel-04874694v1>
- **Analysis of the Relationship Between Carbon Footprint and Mineral Resource Depletion in the LCA of Digital Systems** (2026) — pourquoi ne pas s'arrêter au carbone (ADPe). <https://hal.science/hal-05631178v1>
- **Automating Inventory for LCA of Computing Systems through Machine Vision** (2026) — automatiser l'inventaire matériel, verrou classique de l'ACV. <https://hal.science/hal-05661956v1>

### C.2 — Énergie d'entraînement et d'inférence (modèle prédictif)

- **WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks** (2026) — estimation de l'énergie d'inférence **couche par couche**. <https://hal.science/hal-05681820v1>
- **A Framework for Analytical Performance and Energy Prediction of DL Training on GPUs** (2025) — modèle analytique, pas seulement mesure. <https://minesparis-psl.hal.science/hal-05398496v1>
- **Assessing the Energy and Carbon Emissions of Neural Speaker Verification Model in Training and Inference** (2026) — protocole de mesure entraînement vs inférence. <https://hal.science/hal-05643961v1>
- **Energy-Aware Deep Learning on GPUs through Parameter Sharing and Mixed Precision Training** (2025) — effet des choix d'implémentation sur la conso. <https://minesparis-psl.hal.science/hal-05393922v1>
- **Energy-Aware Scheduling of Large-Scale Deep Learning Training** (2026). <https://hal.science/hal-05531422v1>
- **Adaptive Inference for Cost-Efficient Deep Neural Networks** (2026, thèse). <https://hal.science/tel-05504891v2>
- **A Testbed Framework for Estimating the Environmental Impact of Agentic AI Workflows in HPC** (2026) — cas des **workflows agentiques**, plusieurs appels chaînés. <https://hal.science/hal-05594455v1>
- **Heuristique, CSP ou LLM ? Étude comparative du coût énergétique du placement de services** (2026) — comparer le coût énergétique de l'IA à celui d'une alternative classique. <https://hal.science/hal-05713191v1>

### C.3 — Infrastructure : datacenter, HPC, stockage

- **The Environmental Impacts Of High-Performance Computing: A Systematic Mapping Study** (2026) — revue de littérature, bonne porte d'entrée. <https://hal.science/hal-05601113v2>
- **Analyse de l'empreinte carbone du HPC** (2025). <https://hal.science/hal-05248774v1>
- **Life Cycle Assessment of Edge Data Centers** (2025) — renouvelables et serveurs reconditionnés. <https://hal-lirmm.ccsd.cnrs.fr/lirmm-05015619v2>
- **Micro-Datacenters Model for Carbon Footprint Assessment and Energy Optimization** (2025). <https://hal.science/hal-05252340v1>
- **Modélisation et évaluation d'un concept de mini data center à faible impact environnemental** (2025, thèse). <https://hal.science/tel-05520680v1>
- **Carbon Footprint of Storage in Data Centers: the Impact of Using SSDs for Key-Value Stores** (2025) — le stockage, souvent oublié. <https://hal.science/hal-05447447v1>
- **Carbon Topography Representation: Improving Impacts of Data Center Lifecycle** (2025). <https://hal.science/hal-05138320v1>
- **ETP4HPC SRA 6 White Paper — Energy Efficiency and Sustainability** (2026). <https://hal.science/hal-05494490v1>
- **Energy-Aware Computing in the Year 2026** (Mines Paris). <https://minesparis-psl.hal.science/hal-05632692v1>

### C.4 — Cadrage, politiques publiques, effet rebond

- **Recommandations pour une action publique en faveur d'une IA générative respectueuse de l'environnement** (2023). <https://hal.science/hal-04371031v2>
- **Promouvoir des modèles d'intelligence artificielle frugale pour et par les politiques publiques** (2024). <https://hal.science/hal-04510171v1>
- **The Environmental Impacts of Machine Learning Training Keep Rising — Evidencing Rebound Effect** (2025) — pourquoi l'efficacité seule ne suffit pas. <https://hal.science/hal-04839926v5>
- **When rebound effect is not a side effect: analyzing sociotechnical contexts of digital technologies** (2026). <https://hal.science/hal-05566029v1>
- **How Hyper-Datafication Impacts the Sustainability Costs in Frontier AI** (2026, FAccT). <https://inria.hal.science/hal-05651665v1>

### C.5 — Restitution, pédagogie, perception

- **EcoDashAI: A Visual Analytics Dashboard for Multi-Criteria Evaluation of Language Models Frugality** (2026) — comment **afficher** un résultat multicritère. <https://hal.science/hal-05629071v1>
- **Estimer l'empreinte carbone via LLM : vers une architecture frugale et adaptative** (2026). <https://hal.science/hal-05694015v1>
- **The Invisible Cost of AI-Empowered Education** (2025) — perception de l'empreinte par les utilisateurs. <https://hal.science/hal-05630227v1>
- **Cross-Cultural Differences in Perceptions of the Environmental Impact of Generative AI** (2026). <https://hal.science/hal-05630387v1>
- **TD programmation — empreinte environnementale du numérique** (2025, support de cours). <https://hal.science/hal-05017574v1>
- **Les ressources pour enseigner le numérique responsable en IUT** (2026). <https://hal.science/hal-05632185v1>

---

## D. Ce que la lecture croisée impose au calculateur

Structure minimale qui ressort du corpus ci-dessus :

```
Impact(usage IA) =
    Énergie_calcul (kWh)          # mesure (RAPL/NVML) ou modèle analytique
  × PUE                            # surcoût datacenter (refroidissement, infra)
  × Intensité_carbone (gCO₂e/kWh)  # mix électrique, si possible horaire et local
  + Impacts_fabrication amortis    # GPU/CPU/RAM/stockage, au prorata du temps d'usage
  + Eau (L)                        # refroidissement datacenter + eau du mix électrique
```

Points de vigilance récurrents dans la littérature :

1. **Déclarer le périmètre.** Entraînement seul ≠ entraînement + inférence + données + réseau + terminal.
2. **Ne pas s'arrêter au carbone.** ADPe (ressources abiotiques) et eau changent les conclusions — cf. `impacts-hpc`, *More than carbon*.
3. **Amortir la fabrication.** L'embodied domine sur les usages courts ; c'est le rôle de BoaviztAPI.
4. **Donner l'incertitude et les sources**, pas un chiffre unique (parti pris explicite d'`impacts-hpc`).
5. **Intensité carbone locale et horaire**, pas une moyenne mondiale.
6. **Séparer mesure et estimation.** Mesurer quand on a la machine (RAPL/NVML) ; modéliser quand on n'a qu'une API (approche EcoLogits : tokens + taille de modèle).
7. **S'aligner sur une spec existante.** `SCI = (E × I + M) / R` (Green Software Foundation, section B.5) évite de réinventer le cadre ; l'Impact Framework en donne une implémentation composable.

## E. Angles morts du corpus

- **Littérature anglophone** : HAL couvre surtout la recherche francophone. À compléter par arXiv / ACM DL (*SweetSpot*, *LLMCarbon*, *Sustainable AI*…). Côté eau, l'essentiel est dans *Making AI Less Thirsty* (section B.1).
- **Eau** : très peu de sources chiffrées, en dehors du refroidissement datacenter. C'est l'axe le moins documenté du corpus.
- **Inférence à l'échelle** : la littérature porte majoritairement sur l'entraînement, alors que l'inférence domine l'impact cumulé d'un modèle en production.
- **Données de fabrication des GPU** : peu de LCI publiques ; *More than carbon* (A100) est une des rares références chiffrées.
