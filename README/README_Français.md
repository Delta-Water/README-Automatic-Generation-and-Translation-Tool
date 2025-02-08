- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Outil de Génération et Traduction Automatique de README

Bienvenue dans le projet **README-Automatic-Generation-and-Translation-Tool** ! 🎉 Ce projet a pour but de simplifier la génération et la traduction de la documentation de vos projets GitHub, rendant vos fichiers README plus professionnels et multilingues. Peu importe où vous êtes, attirez facilement plus de développeurs ! 🌍✨

## 🚀 Structure du Projet

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
├── config.json       # Fichier de configuration incluant les paramètres et langues de traduction
│
├── requirements.txt   # Bibliothèques nécessaires au projet
│
└── tool.py            # Script principal pour la génération et la traduction du README
```

## 📜 Résumé de la Licence

Notre projet est sous **Licence Apache 2.0**, ce qui signifie que vous pouvez librement utiliser, modifier et distribuer notre code, à condition de conserver la licence originale et les déclarations connexes. 📝 Ensemble, promouvons la collaboration open source ! 💪

## ⚙️ Fichier de Configuration

`config.json` est le centre de configuration de votre projet. Il vous permet de définir des paramètres tels que le nom du dépôt, les informations sur le propriétaire et les langues de traduction prises en charge (chinois simplifié, chinois traditionnel, anglais, espagnol, français, allemand, japonais), vous permettant ainsi de gérer facilement du contenu multilingue. 🌐💻

## 📦 Bibliothèques Dépendantes

Notre projet dépend des bibliothèques suivantes pour vous permettre de construire facilement votre environnement de développement :

1. **requests** - Bibliothèque simple pour les requêtes HTTP.
2. **openai** - Bibliothèque pour interagir avec l'API OpenAI.
3. **GitPython** - Bibliothèque pour manipuler des dépôts Git avec Python.

Il vous suffit de lancer la commande suivante pour installer les dépendances :

```bash
pip install -r requirements.txt
```

## ⚙️ Aperçu des Fonctionnalités

Le script `tool.py` propose des fonctionnalités puissantes, y compris :

1. **Chargement de Configuration** - Lit les paramètres du projet à partir du fichier de configuration.
2. **Interaction avec le Dépôt** - Récupère des fichiers et leur contenu via l'API GitHub.
3. **Résumé de Contenu** - Utilise l'API d'OpenAI pour résumer le contenu des fichiers de dépôt et générer une description concise.
4. **Génération de README** - Crée un fichier README professionnel basé sur la structure des fichiers et les informations de résumé.
5. **Traduction** - Traduit le contenu du README dans plusieurs langues, tout en conservant des emojis et le style engageant. 😄🎨
6. **Opérations Git** - Soumet le README mis à jour et les fichiers traduits dans le dépôt.

## 🚀 Démarrez Votre Aventure

Il vous suffit de déclencher manuellement le workflow GitHub Actions, d'attendre quelques minutes, et d'excellents fichiers README seront automatiquement générés et traduits. Profitez pleinement de cette belle expérience ! ✨

### 🌟 N'hésitez pas à ajouter une étoile à notre projet ! Votre soutien est notre plus grande motivation pour avancer ! 💖

Merci de votre attention et de votre soutien ! Si vous avez des questions ou des suggestions, n'hésitez pas à nous contacter sur GitHub. Nous sommes impatients de co-créer une meilleure communauté open source avec vous ! 🤝