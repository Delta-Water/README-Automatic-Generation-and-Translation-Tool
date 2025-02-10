- [切换语言: 简体中文](/README.md) | - [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Outil de Génération et de Traduction Automatique de README

Bienvenue dans le projet **README-Automatic-Generation-and-Translation-Tool** ! 🎉 Ce projet a pour but de simplifier la génération et la traduction de la documentation de vos projets sur GitHub, rendant vos fichiers README plus professionnels et multilingues. Peu importe où vous êtes, vous pourrez facilement attirer davantage de développeurs ! 🌍✨

## 🚀 Structure du Projet

Voici un aperçu de la structure du projet :

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # Fichier de flux de travail GitHub Actions
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
├── config.json       # Fichier de configuration, y compris les paramètres et les langues de traduction
│
├── requirements.txt   # Bibliothèques nécessaires pour le projet
│
└── tool.py            # Script principal pour la génération et la traduction automatique de README
```

## 📜 Résumé de la Licence

Notre projet utilise la **Licence Apache 2.0**, ce qui signifie que vous êtes libre d'utiliser, de modifier et de distribuer notre code, tant que vous conservez la licence originale et les déclarations associées. 📝 Ensemble, promouvons la collaboration open source ! 💪

## ⚙️ Fichier de Configuration

`config.json` est le centre de configuration de votre projet. Il vous permet de définir des paramètres tels que le nom du dépôt, les informations sur le propriétaire et les langues de traduction prises en charge (chinois simplifié, chinois traditionnel, anglais, espagnol, français, allemand, japonais), vous permettant de gérer facilement le contenu multilingue. 🌐💻

## 📦 Bibliothèques Dépendantes

Notre projet dépend des bibliothèques suivantes, garantissant que vous pouvez facilement configurer votre environnement de développement :

1. **requests** - Bibliothèque simple pour les requêtes HTTP.
2. **openai** - Bibliothèque pour interagir avec l’API d’OpenAI.
3. **GitPython** - Bibliothèque pour manipuler des dépôts Git via Python.

Il vous suffit d'exécuter la commande suivante pour installer les dépendances :

```bash
pip install -r requirements.txt
```

## ⚙️ Aperçu des Fonctionnalités

Le script `tool.py` offre des fonctionnalités puissantes, notamment :

1. **Chargement de Configuration** - Lecture des paramètres de projet à partir du fichier de configuration.
2. **Interaction avec le Dépôt** - Récupération des fichiers et de leur contenu via l’API GitHub.
3. **Résumé de Contenu** - Utilisation de l’API d’OpenAI pour résumer le contenu des fichiers du dépôt et générer une description concise.
4. **Génération de README** - Création d’un fichier README professionnel basé sur la structure des fichiers et les informations de résumé.
5. **Traduction** - Traduction du contenu du README en plusieurs langues, tout en préservant des emojis et un style engageant. 😄🎨
6. **Opérations Git** - Soumission du README mis à jour et des fichiers traduits dans le dépôt.

## 🚀 Lancez Votre Voyage

Il suffit de démarrer manuellement le flux de travail des Actions GitHub, d'attendre quelques minutes, et un excellent fichier README sera généré et traduit automatiquement. Profitez de cette belle expérience ! ✨

### 🌟 N'oubliez pas de nous donner une étoile ! Votre soutien est notre moteur pour avancer ! 💖

Merci pour votre attention et votre soutien ! Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter sur GitHub. Nous sommes impatients de créer un meilleur écosystème open source avec vous ! 🤝