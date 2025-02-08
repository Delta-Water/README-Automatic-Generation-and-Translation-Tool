- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - Outil de génération et de traduction automatisée 🌟

Bienvenue dans le projet **README-Automatic-Generation-and-Translation-Tool** ! 🚀

Nous nous engageons à fournir aux développeurs un outil automatisé pour générer et traduire facilement les fichiers README des projets GitHub, rendant la documentation de votre projet plus attrayante et professionnelle ! 💕

## Structure du projet 📂

Voici la structure actuelle du projet, accompagnée d'explications pour les différents fichiers :

```
├── .github
│   └── workflows
│       └── main.yml     # Fichier de configuration du workflow GitHub Actions
├── LICENSE                # Fichier de licence du projet
├── README.md              # Documentation principale du projet
├── README
│   ├── README_Deutsch.md  # Fichier README en allemand
│   ├── README_English.md  # Fichier README en anglais
│   ├── README_Español.md  # Fichier README en espagnol
│   ├── README_Français.md # Fichier README en français
│   ├── README_日本語.md    # Fichier README en japonais
│   └── README_繁体中文.md   # Fichier README en chinois traditionnel
├── config.json            # Fichier de configuration du projet
├── requirements.txt       # Liste des dépendances Python
└── tool.py                # Script pour générer et mettre à jour automatiquement les fichiers README
```

## Résumé des fichiers 📄

### 1. `.github/workflows/main.yml`
Ce fichier de configuration du workflow GitHub Actions aide à automatiser la génération et la traduction des fichiers README. Il s'exécute dans un environnement Ubuntu dans sa dernière version et effectue les étapes suivantes :

- **Vérification de code** : Récupération des derniers codes.
- **Configuration de Python** : Configuration de Python 3.8 comme environnement.
- **Installation des dépendances** : Mise à jour de pip et installation des paquets Python nécessaires (requests, openai, GitPython).
- **Exécution du script** : Exécution du script Python (tool.py) pour générer le README en utilisant les identifiants de l'API GitHub et OpenAI.

### 2. `LICENSE`
Ce fichier contient la version 2.0 de la licence Apache, décrivant les termes et conditions relatifs à l'utilisation, la reproduction et la distribution des logiciels et autres œuvres. La licence fournit un cadre légal encourageant le développement de logiciels open source, tout en protégeant les droits des contributeurs et des utilisateurs.

### 3. `config.json`
Ce fichier de configuration définit les paramètres importants du projet, tels que : le nom du dépôt, le propriétaire, l'URL de base de l'API et la branche par défaut (main). Il supporte la génération et la traduction automatisées des fichiers README.

### 4. `requirements.txt`
Liste les bibliothèques de dépendances nécessaires au projet Python, y compris :

- **requests** : Une bibliothèque populaire pour simplifier les requêtes HTTP.
- **openai** : Bibliothèque pour interagir avec l'API OpenAI.
- **GitPython** : Bibliothèque pour interagir directement avec des dépôts Git en Python.

### 5. `tool.py`
Ce script automatise la génération et la mise à jour des fichiers README dans le dépôt GitHub ainsi que leurs traductions. Ses fonctionnalités clés incluent :

1. **Configuration et réglages** : Chargement de la configuration et obtention des variables d'environnement nécessaires.
2. **Gestion de fichiers** : Accès au dépôt GitHub pour obtenir la structure et le contenu des fichiers.
3. **Génération de README** : Utilisation de l'API OpenAI pour générer un fichier README détaillé.
4. **Création de traductions** : Traduction du README généré dans plusieurs langues.
5. **Lien et intégration de structures** : Amélioration de la navigabilité.
6. **Soumission et envoi** : Soumission des fichiers mis à jour dans le dépôt GitHub.

## Démarrer rapidement 🚀

Envie de participer ? Cliquez sur la ⭐ en haut à droite pour apprécier notre projet ! 💖 

Avec cet outil, nous aidons chaque développeur à maintenir facilement la documentation de ses projets et à améliorer son niveau d'internationalisation ! Que votre projet soit grand ou petit, nous vous aidons à ne plus vous soucier de la documentation et à construire ensemble un meilleur écosystème open source ! 🌍👩‍💻👨‍💻

Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter ! Happy coding ! 🎉