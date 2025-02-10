<div align="center">

[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Outil d'Automatisation pour la Génération et la Traduction de README

Bienvenue dans le projet **Outil d'Automatisation de Génération et de Traduction de README** ! 🎉 Ce projet vise à offrir aux développeurs et aux mainteneurs de projets un moyen pratique de générer, optimiser et traduire facilement des fichiers README. Que vous soyez débutant ou expert, en quelques étapes simples, vous obtiendrez un document README professionnel et captivant ! 🚀

## 📂 Structure du Projet

```plaintext
./
└── workflows/
│   ├── generate.yml      # Workflow pour la génération automatique de fichiers README
│   ├── optimize.yml      # Workflow pour l'optimisation automatique des documents README
│   └── translate.yml      # Workflow pour la traduction automatique des documents README
└── LICENSE                # Fichier de licence Apache
└── README.md              # Fichier d'introduction du projet
└── config.json            # Fichier de configuration définissant les paramètres du projet
└── requirements.txt       # Liste des dépendances Python
└── tool.py                # Outil de traitement automatisé
```

## ⚙️ Présentation des Fichiers

### `.github/workflows/generate.yml`
Ce workflow génère automatiquement le fichier README du projet via GitHub Actions. Une fois déclenché manuellement, il exécute les étapes suivantes :
1. Récupération du code du projet ;
2. Configuration de l'environnement Python 3.8 ;
3. Installation des dépendances nécessaires ( `requests`, `openai`, `GitPython`) ;
4. Exécution du script `tool.py generate` pour générer le fichier README.

### `.github/workflows/optimize.yml`
Ce workflow est utilisé pour optimiser automatiquement le fichier README. Après déclenchement manuel, il exécute principalement les étapes suivantes :
1. Récupération du code ;
2. Configuration de l'environnement Python 3.8 ;
3. Installation des dépendances nécessaires ;
4. Exécution de `tool.py optimize`, en utilisant l'API OpenAI pour le traitement d'optimisation.

### `.github/workflows/translate.yml`
Ce workflow est destiné à la traduction automatique du fichier README du projet, également démarré manuellement. Les étapes incluent :
1. Récupération du code ;
2. Configuration de l'environnement Python 3.8 ;
3. Installation des dépendances ;
4. Exécution de `tool.py translate` pour effectuer la traduction.

### `LICENSE`
Ce fichier contient la licence Apache 2.0, permettant aux utilisateurs d'utiliser, modifier et distribuer librement ce projet sous certaines conditions, afin de protéger les droits des auteurs originaux et des contributeurs.

### `config.json`
Ce fichier de configuration définit divers paramètres nécessaires au fonctionnement du projet, y compris les informations sur le dépôt, l'URL de base de l'API, les modèles et les langues de traduction supportées.

### `requirements.txt`
Liste les paquets Python nécessaires au projet, y compris :
- `requests` : pour gérer les requêtes HTTP et simplifier les interactions réseau.
- `openai` : pour interagir avec l'API OpenAI et appeler les modèles d'IA.
- `GitPython` : pour fournir un support pour les opérations sur les dépôts Git.

### `tool.py`
Le script principal utilisé pour le traitement automatisé du README, comprenant les fonctions suivantes :
1. Chargement de la configuration ;
2. Récupération du contenu du dépôt ;
3. Génération du contenu README ;
4. Amélioration et traduction du README ;
5. Soumission des modifications ;
6. Fourniture d’une interface de ligne de commande.

## 🌸 Comment Utiliser ?

Vous pouvez choisir de forker ce projet et d'utiliser `GitHub Actions`, ou de le cloner sur votre machine locale pour l'utiliser. Voici la méthode pour le premier cas, pour le second, veuillez le configurer vous-même.

1. D'abord, ajoutez `PAT` et `OPENAI_API_KEY` dans les Secrets.
2. Ensuite, rendez-vous dans `config.json` pour configurer les paramètres nécessaires.
3. Pour générer un README, déclenchez manuellement le workflow `generate`.
4. Pour optimiser le README, déclenchez manuellement le workflow `optimize`.
5. Pour traduire le README, déclenchez manuellement le workflow `translate`.

## 🌟 Commençons !

N'hésitez plus ! Utilisez cet outil pour améliorer la qualité de la documentation de votre projet et attirer plus de collaborations et d'attentions ! Si vous trouvez ce projet utile, montrez-nous votre soutien avec un 💖 Star ! Ensemble, travaillons à rendre la communauté open source encore meilleure ! 🌈

## 📄 Licence

Ce projet est sous licence Apache, pour plus d'informations, veuillez consulter le fichier [LICENSE](LICENSE).

Rejoignez-nous et rendons les README plus simples et efficaces ! 🚀