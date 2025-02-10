<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Outil de génération et de traduction automatique de README

Bienvenue dans le projet **Outil de génération et de traduction automatique de README** ! 🎉 Ce projet a pour but de fournir aux développeurs et aux mainteneurs de projets un moyen pratique de générer, d'optimiser et de traduire facilement des fichiers README. Que vous soyez débutant ou expert, il vous suffit de quelques étapes simples pour obtenir un document README professionnel et engageant ! 🚀

## 📂 Structure du projet

```plaintext
./
└── workflows/
│   ├── generate.yml      # Flux de travail pour la génération automatique de README
│   ├── optimize.yml      # Flux de travail pour l'optimisation automatique du document README
│   └── translate.yml      # Flux de travail pour la traduction automatique du document README
└── LICENSE                # Fichier de licence Apache
└── README.md              # Fichier de description du projet
└── config.json            # Fichier de configuration définissant les paramètres du projet
└── requirements.txt       # Liste des dépendances Python
└── tool.py                # Outil de traitement automatisé
```

## ⚙️ Description des fichiers

### `.github/workflows/generate.yml`
Ce flux de travail génère automatiquement le fichier README du projet via GitHub Actions. Après un déclenchement manuel, il exécute les étapes suivantes :
1. Récupérer le code du projet ;
2. Configurer l'environnement Python 3.8 ;
3. Installer les dépendances nécessaires (`requests`, `openai`, `GitPython`) ;
4. Exécuter le script `tool.py generate` pour générer le fichier README.

### `.github/workflows/optimize.yml`
Ce flux de travail sert à optimiser automatiquement le fichier README. Après un déclenchement manuel, il réalise principalement les étapes suivantes :
1. Récupérer le code ;
2. Configurer l'environnement Python 3.8 ;
3. Installer les dépendances nécessaires ;
4. Exécuter `tool.py optimize` pour l'optimisation via l'API OpenAI.

### `.github/workflows/translate.yml`
Ce flux de travail est utilisé pour traduire automatiquement le fichier README du projet. Il se déclenche également manuellement. Les étapes comprennent :
1. Récupérer le code ;
2. Configurer l'environnement Python 3.8 ;
3. Installer les dépendances ;
4. Exécuter `tool.py translate` pour la traduction.

### `LICENSE`
Ce fichier contient la licence Apache version 2, permettant aux utilisateurs d'utiliser, de modifier et de distribuer ce projet, en respectant certaines conditions, afin de protéger les droits des auteurs et contributeurs originaux.

### `config.json`
Ce fichier de configuration définit divers paramètres nécessaires au fonctionnement du projet, y compris les informations sur le dépôt, l'URL de base de l'API, le modèle et les langues de traduction supportées.

### `requirements.txt`
Liste les paquets Python nécessaires au projet, incluant :
- `requests`: pour gérer les requêtes HTTP et simplifier les interactions réseau.
- `openai`: pour interagir avec l'API OpenAI et permettre l'appel des modèles AI.
- `GitPython`: pour fournir un support d'opération sur les dépôts Git.

### `tool.py`
Le script central utilisé pour le traitement automatisé du README dont les principales fonctionnalités incluent :
1. Charger la configuration ;
2. Obtenir le contenu du dépôt ;
3. Générer le contenu du README ;
4. Compléter et traduire le README ;
5. Soumettre les modifications ;
6. Proposer une interface en ligne de commande.

## 🌸 Comment utiliser ?

Vous pouvez soit forker ce projet et utiliser `GitHub Actions`, soit le cloner localement pour l'utiliser. Prenons l'exemple du fork, pour le clonage, veuillez effectuer les configurations vous-même.

1. Tout d'abord, ajoutez `PAT` et `OPENAI_API_KEY` dans les Secrets.
2. Ensuite, accédez à `config.json` pour configurer les paramètres pertinents.
3. Pour générer un README, déclenchez manuellement le flux de travail `generate`.
4. Pour optimiser le README, déclenchez manuellement le flux de travail `optimize`.
5. Pour traduire le README, déclenchez manuellement le flux de travail `translate`.

## 🌟 Commençons !

N'hésitez plus ! Utilisez cet outil pour améliorer la qualité de la documentation de votre projet et attirer davantage de collaborations et d'attention ! Si vous trouvez ce projet utile, donnez-nous une 💖 étoile ! Ensemble, faisons en sorte que la communauté open source soit encore meilleure ! 🌈

## 📄 Licence

Ce projet est sous licence Apache, pour plus de détails, veuillez consulter le fichier [LICENSE](LICENSE).

Rejoignez-nous et rendons le README plus simple et efficace ! 🚀