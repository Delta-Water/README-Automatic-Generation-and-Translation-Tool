- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Outil de Génération et de Traduction Automatique de README 🛠️✨

Bienvenue dans le projet **Outil de Génération et de Traduction Automatique de README** ! Cet outil a pour but de simplifier et d'améliorer la gestion et la traduction des fichiers README dans les dépôts GitHub, que vous soyez mainteneur de projet ou nouvel utilisateur, cela rendra votre flux de travail plus efficace et agréable ! 😄

## Structure du Projet 🗂️

Voici la structure des répertoires, qui vous aidera à comprendre rapidement l'utilisation de chaque fichier et dossier :

```
.github
└── workflows
    ├── generate.yml         # Flux de travail pour générer automatiquement le fichier README
    ├── optimize.yml         # Flux de travail pour optimiser automatiquement le fichier README
    └── translate.yml        # Flux de travail pour traduire automatiquement le fichier README

LICENSE                        # Fichier de licence du projet
README.md                     # Fichier README principal du projet
README
├── README_Deutsch.md        # README en allemand
├── README_English.md        # README en anglais
├── README_Español.md        # README en espagnol
├── README_Français.md       # README en français
├── README_日本語.md         # README en japonais
└── README_繁体中文.md      # README en chinois (traditionnel)

config.json                   # Fichier de configuration
requirements.txt              # Fichier de dépendances Python
tool.py                       # Script de l'outil d'automatisation
```

## Aperçu des Flux de Travail 🚀

### 1. `generate.yml`
Ce flux de travail GitHub Actions est utilisé pour générer et mettre à jour automatiquement le fichier README. Les étapes principales comprennent :

- Vérification du code
- Configuration de l'environnement Python 3.8
- Installation des dépendances requises (`requests`, `openai`, `GitPython`)
- Exécution du script (`tool.py generate`) pour générer ou mettre à jour le fichier README
- Configuration de Git et envoi du fichier README mis à jour

Ce processus simplifie la maintenance du fichier README, vous permettant de vous concentrer sur des tâches plus importantes ! 😎

### 2. `optimize.yml`
Ce flux de travail optimise automatiquement le fichier README, et peut également être déclenché manuellement via l'événement `workflow_dispatch`. Les étapes clés incluent :

- Vérification du code
- Configuration de l'environnement Python 3.8
- Installation des dépendances
- Exécution du script (`tool.py optimize`) pour améliorer le contenu du README
- Soumission et envoi du fichier README mis à jour

Améliorons ensemble la qualité du contenu ! 💪

### 3. `translate.yml`
Ce flux de travail traduit automatiquement le fichier README, garantissant que votre projet atteigne un public plus large. Les étapes comprennent :

- Vérification du code
- Configuration de l'environnement Python 3.8
- Installation des dépendances
- Exécution du script de traduction (`tool.py`)

C’est votre assistant ultime à l'ère du multilinguisme ! 🌍

## Licence 📄
Ce projet est sous la licence Apache 2.0, vous permettant d'utiliser, modifier et distribuer le code tout en protégeant vos droits et obligations.

## Gestion de la Configuration 🛠️
Le fichier `config.json` définit les paramètres importants, comme les points de terminaison API et les langues de traduction prises en charge, afin d'assurer le bon fonctionnement de l'outil et de prendre en charge les fonctionnalités multilingues. 🤓

## Gestion des Dépendances 🐍
Le fichier `requirements.txt` liste les paquets Python nécessaires, notamment :

- **requests** : Simplifie les requêtes HTTP
- **openai** : Accède à l'API OpenAI pour diverses opérations
- **GitPython** : Interagit avec les dépôts Git en Python

Assurez-vous d'installer ces dépendances pour garantir le bon fonctionnement de l'outil ! 🌟

## Comment l'utiliser ?

Vous pouvez choisir de fork ce projet et d’utiliser `GitHub Actions`, ou de le cloner localement.

Voici un exemple d'utilisation de GitHub Actions :

1. Ajoutez `PAT` et `OPENAI_API_KEY` dans les Secrets GitHub.
2. Modifiez le fichier `config.json` pour configurer les paramètres.
3. Si vous souhaitez générer et traduire le fichier README :
   - Exécutez manuellement le flux de travail `generate`, ce qui générera un fichier `.README.md` à la racine du dépôt.
   - Révisez et modifiez ce fichier avant de le soumettre.
   - Déclenchez manuellement le flux de travail `translate`, l'outil ajoutera le README modifié au dépôt cible et générera la version traduite.

C'est fait ! 🎉

Si vous avez déjà un fichier README et souhaitez simplement le traduire :
- Poussez-le dans le fichier `.README.md` du dépôt de l'outil.
- Déclenchez manuellement le flux de travail `translate`.

C'est fait ! 🎉

## Retours et Contributions 🙌
Nous accueillons vos retours et suggestions ! N'hésitez pas à donner une étoile à ce projet ⭐️ et à vous impliquer, afin d'améliorer ensemble la qualité et l'utilité du projet.

Merci pour votre attention et votre soutien ! Ensemble, rendons les fichiers README plus vivants et intéressants ! 🎉