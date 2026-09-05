# Sources analysées

Ce fichier trace d'où vient le contenu du [README](README.md) : ce qui a été
balayé, comment, et ce qui a été écarté. Le README ne garde que la sélection
retenue ; les inventaires bruts complets sont dans `output/`.

Dernier passage : 2026-09-05.

## 1. Ce qui a été balayé automatiquement

| Source | Interrogée via | Requêtes | Retenus après filtrage | Fichiers |
|---|---|---:|---:|---|
| **GitLab**, 12 forges | API REST `/api/v4/projects` | 50 | 374 dépôts | `output/gitlab_projets.{csv,json,md}` |
| **GitHub** | API REST `/search/repositories` | 40 | 1610 dépôts | `output/github_projets.{csv,json,md}` |
| **HAL** | API Solr `api.archives-ouvertes.fr` | 14 | 556 publications | `output/hal_publications.{csv,json,md}` |
| **arXiv** | API Atom `export.arxiv.org` | 18 | 1737 publications | `output/arxiv_publications.{csv,json,md}` |

Sur ces 4277 entrées, le README en retient 56 en partie A et
63 en partie B. Le reste sert de réserve : les fichiers `output/` portent pour
chaque ligne un score, les axes d'impact détectés (`carbone`, `energie`, `eau`,
`acv`, `mesure`), un indicateur `ia` et les requêtes qui l'ont fait remonter.

### Forges GitLab interrogées

`gitlab.com`, `framagit.org`, `gitlab.inria.fr`, `gitlab.in2p3.fr`,
`forge.apps.education.fr`, `gitlab.ow2.org`, `gitlab.univ-lille.fr`,
`gitlab.irit.fr`, `gitlab.imt-atlantique.fr`, `gitlab.huma-num.fr`,
`gricad-gitlab.univ-grenoble-alpes.fr`, `plmlab.math.cnrs.fr`.

### Comment refaire tourner

```bash
pip install -r requirements.txt
python scrape_gitlab.py                 # 12 forges GitLab
python scrape_github.py                 # token pris via `gh auth token`
python scrape_hal.py --rows 80          # HAL
python scrape_arxiv.py --validate       # arXiv, avec papiers de contrôle
```

`scrape_arxiv.py --validate` vérifie que dix articles fondateurs connus
remontent bien dans les résultats. Le dernier passage en retrouve huit sur dix.
Les deux manquants, *Power Hungry Processing* et *Energy and Policy
Considerations*, sont dans le README, ajoutés à la main : ils sortent du filtre
par catégorie arXiv retenu.

## 2. Ce qui a été ajouté à la main

Le balayage automatique ne couvre ni les rapports institutionnels, ni les
revues à comité de lecture hors arXiv, ni les publications d'entreprise. Ces
sources ont été ajoutées une par une, après vérification du lien et du contenu.

| Catégorie | Exemples | Vérification |
|---|---|---|
| Rapports d'organisations | UNU-INWEH, AI Index de Stanford, AIE, Arcep | Page éditeur, titre et année confirmés |
| Revues à comité de lecture | Applied Energy, Patterns, PLOS ONE, JMIR AI, Sustainability, Energies, Eco-Environment & Health | DOI résolu via l'API Crossref ou les identifiants PMC via NCBI eutils |
| Publications d'éditeurs de modèles | ACV de Mistral Large 2, rapport technique de Llama 2 | Page officielle et contenu lus |
| Rapports d'opérateurs | Google, Microsoft, Amazon, Meta, Apple, NVIDIA | Page de publication de chaque opérateur |
| Bases de données ACV | ecoinvent, Base Empreinte de l'ADEME | Site officiel |

Chaque lien du README a été testé : il répond en 200, ou en 202, 203 ou 403
quand l'éditeur bloque les requêtes automatisées tout en servant la page à un
navigateur. C'est le cas de MDPI, de tandfonline et de Microsoft.

## 3. Ce qui a été écarté

Le tri suit une règle simple : une source primaire, une revue à comité de
lecture, ou rien.

| Écarté | Motif |
|---|---|
| Copies d'articles sur Scribd | Reproduction sans autorisation, lien instable. L'article d'Applied Energy concerné a été retrouvé et cité par son DOI. |
| Pages de méthodologie d'éditeurs de logiciels | Contenu commercial, méthode non vérifiable. |
| Agrégateurs de données d'émissions d'entreprises | Reprise non sourcée des rapports officiels, qui sont cités directement. |
| Revues étudiantes | Absence de comité de lecture établi. |
| Articles de presse généraliste et spécialisée | Ils commentent des rapports déjà cités dans le README. |
| Bibliométrie de l'IA appliquée à la gestion du carbone | Hors périmètre : ce dépôt mesure l'impact de l'IA, pas l'IA comme outil de mesure. |
| Bases sectorielles alimentaires et cosmétiques | Hors périmètre. |
| Explorateur de données de Google | Lien mort au moment de la vérification. |

## 4. Limites du balayage automatique

Le filtrage reste lexical : il lit un titre, une description, un résumé, jamais
le contenu. Trois conséquences.

Un dépôt sans description est invisible. Sur GitLab, cela concerne une part
notable des projets de recherche.

Le mot *energy* est ambigu sur arXiv, où il désigne aussi une fonction de coût
ou une grandeur physique. Une liste d'exclusion et une restriction aux
catégories `cs`, `eess` et `stat` limitent le bruit sans l'éliminer.

HAL indexe surtout la recherche francophone, arXiv surtout les préprints
anglophones. Les revues à comité de lecture hors de ces deux canaux n'entrent
que par l'ajout manuel décrit en partie 2.
