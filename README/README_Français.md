[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) | [English](/README/README_en.md) | [Español](/README/README_es.md) | [Deutsch](/README/README_de.md) | [日本語](/README/README_ja.md)

- [切换语言: 繁体中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Outil de génération et de traduction automatique de README

Bienvenue dans le projet **README-Automatic-Generation-and-Translation-Tool** ! 🎉 Ce projet vise à simplifier la génération et la traduction de la documentation de vos projets GitHub, rendant ainsi vos fichiers README plus professionnels et multilingues, afin d'attirer facilement plus de développeurs, où que vous soyez ! 🌍✨

## 🚀 Structure du projet

Voici un aperçu de la structure du projet :

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # Fichier de workflow GitHub Actions
│
├── LICENSE            # Licence Apache 2.0
│
├── README.md          # Fichier README principal du projet
│
├── README/
│   ├── README_Deutsch.md     # README en allemand 
│   ├── README_English.md      # README en anglais 
│   ├── README_Español.md      # README en espagnol 
│   ├── README_Français.md     # README en français 
│   ├── README_日本語.md        # README en japonais 
│   └── README_繁体中文.md      # README en chinois traditionnel 
│
├── config.json       # Fichier de configuration, y compris les paramètres et langues de traduction
│
├── requirements.txt   # Bibliothèques requises par le projet
│
└── tool.py            # Script principal pour générer et traduire le README
```

## 📜 Résumé de la licence

Notre projet utilise la **licence Apache 2.0**, ce qui signifie que vous pouvez utiliser, modifier et distribuer notre code librement, tout en préservant la licence d'origine et les déclarations associées. 📝 Promouvons ensemble la collaboration open source ! 💪

## ⚙️ Fichier de configuration

`config.json` est le centre de configuration de votre projet. Il vous permet de définir des paramètres pertinents, tels que le nom du dépôt, les informations du propriétaire et les langues de traduction supportées (chinois simplifié, chinois traditionnel, anglais, espagnol, français, allemand, japonais), vous permettant ainsi de basculer et de gérer facilement le contenu multilingue. 🌐💻

## 📦 Bibliothèques

Notre projet dépend des bibliothèques suivantes, garantissant que vous pouvez facilement mettre en place votre environnement de développement :

1. **requests** - Bibliothèque de requêtes HTTP simple.
2. **openai** - Bibliothèque pour interagir avec l'API OpenAI.
3. **GitPython** - Bibliothèque pour manipuler des dépôts Git via Python.

Il vous suffit d'exécuter la commande suivante pour installer les dépendances :

```bash
pip install -r requirements.txt
```

## ⚙️ Aperçu des fonctionnalités

Le script `tool.py` offre de puissantes fonctionnalités, notamment :

1. **Chargement de configuration** - Lecture des paramètres du projet à partir du fichier de configuration.
2. **Interaction avec le dépôt** - Récupération des fichiers et de leur contenu via l'API GitHub.
3. **Résumé de contenu** - Utilisation de l'API d'OpenAI pour résumer le contenu des fichiers du dépôt et générer une description concise.
4. **Génération de README** - Création d'un fichier README professionnel en fonction de la structure des fichiers et des informations de résumé.
5. **Traduction** - Traduire le contenu du README en plusieurs langues, tout en conservant des emojis et un style vivant. 😄🎨
6. **Opérations Git** - Soumission des fichiers README mis à jour et traduits dans le dépôt.

## 🚀 Lancement du projet

Il vous suffit de déclencher manuellement le workflow GitHub Actions et d'attendre quelques minutes : un superbe fichier README sera automatiquement généré et traduit, vous pourrez alors profiter de tout cela. ✨

### 🌟 Venez nous donner une étoile ! Votre soutien est notre moteur pour avancer ! 💖

Merci de votre attention et de votre soutien ! Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter sur GitHub. Nous avons hâte de créer une meilleure communauté open source avec vous ! 🤝