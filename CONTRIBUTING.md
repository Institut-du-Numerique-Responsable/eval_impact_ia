# Contribuer à eval_impact_ia

Merci de vouloir contribuer à ce projet ! Ce dépôt est une **ressource collaborative** maintenue par l**[Institut du Numérique Responsable](https://institutnr.org) pour rassembler les meilleures pratiques et outils autour du calcul de l'impact environnemental de l'IA.

---

## 📌 Comment contribuer ?

### 1. **Signaler une ressource manquante**
Vous avez trouvé un **article scientifique**, un **outil open source**, ou un **rapport institutionnel** qui devrait figurer dans ce dépôt ?

→ **Ouvrez une [Issue](https://github.com/Institut-du-Numerique-Responsable/eval_impact_ia/issues/new/choose)** avec :
- Le **lien** vers la ressource
- Une **brève description** de son apport
- La **catégorie** suggérée (A.x, B.x, ou D.x)

*Exemple :*
```markdown
### Nouvelle ressource à ajouter

- **Lien** : https://example.com/paper-on-ai-carbon-footprint
- **Type** : Publication scientifique (HAL)
- **Catégorie** : A.1 (ACV complète)
- **Apport** : Méthodologie innovante pour mesurer l'empreinte eau des LLM
```

---

### 2. **Proposer une modification**
Vous avez repéré une **erreur**, une **coquille**, ou une **amélioration** à apporter ?

→ **Ouvrez une Pull Request** avec :
- Une **description claire** des changements
- Un **commit atomique** (1 changement = 1 commit)
- Des **tests** si applicable (pour les scripts)

*Exemple de bon commit :*
```
git commit -m "Ajoute [outils/ecologits] dans B.1 - détection automatique manquante

- Ajout de mlco2/ecologits dans la section B.1
- Mise à jour du compte des ressources (87 → 88)
- Vérification du lien (200 OK)"
```

---

### 3. **Ajouter un outil ou une publication**
Pour ajouter une **nouvelle entrée** dans le README :

1. **Vérifiez** qu'elle n'existe pas déjà (Ctrl+F dans le README)
2. **Testez le lien** : `curl -I <URL>` doit retourner `200` ou `301`
3. **Trouvez la bonne section** :
   - **A.** = Publications scientifiques (HAL, arXiv, revues)
   - **B.** = Outils open source (GitHub, GitLab, Hugging Face)
   - **D.** = Sources à interroger (laboratoires, portails)
4. **Respectez le format** des tableaux existants

*Exemple pour la section B.1 :*
```markdown
| [org/tool](https://github.com/org/tool) | GitHub | Description concise de l'apport. |
```

---

### 4. **Améliorer la documentation**
Ce dépôt vit grâce à sa **documentation claire**.

Vous pouvez :
- Corriger des **fautes d'orthographe**
- Améliorer les **descriptions** existantes
- Ajouter des **exemples d'utilisation**
- Traduire du contenu en **anglais** (pour une audience internationale)

---

## 🎯 Règles de contribution

### ✅ **Ce qui est accepté**
- ✅ Ajout de **publications scientifiques** vérifiables (HAL, arXiv, DOI)
- ✅ Ajout d'**outils open source** actifs et maintenus
- ✅ Ajout de **laboratoires/portails** de référence
- ✅ Corrections de **liens cassés**
- ✅ Améliorations de **clarté** ou de **structure**
- ✅ Ajouts de **métadonnées** (CITATION.cff, ai.txt, etc.)

### ❌ **Ce qui est refusé**
- ❌ **Publicités** ou contenu commercial
- ❌ **Outils propriétaires** (sauf si version open source disponible)
- ❌ **Liens cassés** (200 OK requis)
- ❌ **Duplications** (une seule entrée par ressource)
- ❌ **Contenu hors sujet** (pas de ressources génériques sur l'IA)
- ❌ **Modifications sans justification**

---

## 📋 Processus de revue

1. **Vous soumettez** une PR ou une Issue
2. **Un maintaineur** (membre de l'INR) examine votre contribution sous 48h
3. **Feedback** : Demande de modifications si nécessaire
4. **Merge** : Une fois validée, votre contribution est intégrée !

---

## 🛠️ Environnement local

Pour travailler sur ce dépôt localement :

```bash
# Cloner le dépôt
git clone https://github.com/Institut-du-Numerique-Responsable/eval_impact_ia.git
cd eval_impact_ia

# (Optionnel) Installer les dépendances pour les scripts Python
pip install -r requirements.txt

# Modifier les fichiers (README.md, SOURCES.md, etc.)
# Puis soumettre une PR
```

---

## 📜 Licence

Ce dépôt est sous **licence [CC0-1.0](LICENSE)**. En contribuant, vous acceptez que vos contributions soient également sous cette licence.

---

## 🙏 Remerciements

Merci à tous les contributeurs qui aident à maintenir ce projet à jour !

*Pour toute question, contactez-nous : [contact@institutnr.org](mailto:contact@institutnr.org)*
