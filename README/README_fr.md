<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Outil d'Automatisation de Génération et de Traduction de README

Bienvenue dans le monde de **l'outil d'automatisation de génération et de traduction de README** ! 🎉 Ce projet est conçu pour offrir aux développeurs et aux mainteneurs de projets une solution efficace et pratique pour générer, optimiser et traduire des fichiers README, apportant ainsi une documentation professionnelle et attrayante à votre code. Que vous soyez novice ou développeur expérimenté, vous trouverez ici tous les outils dont vous avez besoin ! 🌟

## 🛠️ Structure du Projet

Voici la structure de base du projet, claire et facile à utiliser :

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # Flux de travail pour la génération automatique de README
│       ├── optimize.yml      # Flux de travail pour l'optimisation du README
│       └── translate.yml      # Flux de travail pour la traduction du README
├── LICENSE                   # Licence du projet
├── README.md                 # Fichier de description du projet
├── config.json               # Fichier de configuration de l’outil
├── requirements.txt          # Liste des bibliothèques dépendantes
└── tool.py                   # Script d'automatisation
```

## ✨ Fonctionnalités Principales

1. **Génération Automatique de README** : Grâce aux flux de travail GitHub Actions, générez automatiquement des fichiers README professionnels à partir du code du projet.
2. **Fonctionnalité d'Optimisation** : Utilisez l'API d'OpenAI pour améliorer la qualité des documents README existants grâce à l'optimisation pilotée par l'IA.
3. **Capacité de Traduction** : Traduisez automatiquement le fichier README en plusieurs langues, permettant à un public plus large d'accéder facilement à votre projet 👌.

## ⚙️ Flux de Travail

### 1. `generate.yml`
- Déclenchement manuel pour générer le fichier README via `workflow_dispatch`.
- Exécution dans un environnement Ubuntu, installation des dépendances nécessaires (`requests`, `openai`, `GitPython`).
- Finalement, exécution du script `tool.py generate` pour générer un README professionnel.

### 2. `optimize.yml`
- Déclenchement manuel pour optimiser automatiquement un fichier README existant.
- Inclut des étapes de vérification de code, de configuration d’environnement Python et d'installation des dépendances.
- Exécution du script `tool.py optimize` pour améliorer la lisibilité du README.

### 3. `translate.yml`
- Déclenchement manuel pour traduire automatiquement le fichier README.
- Après vérification du code, configuration de l’environnement Python et installation des dépendances requises, le script de traduction est exécuté.

## 📝 Explication de la Configuration

Le fichier `config.json` contient les configurations et options de base de l’outil, notamment :
- Nom et propriétaire du dépôt
- URL de base de l’API et modèle de langue utilisé
- Langues à traduire et leurs abrégés
- …

Assurez-vous de configurer correctement ce fichier pour garantir le bon fonctionnement de l’outil. 🔑

## 📦 Bibliothèques Dépendantes

Vous pouvez trouver les bibliothèques dépendantes nécessaires au projet dans `requirements.txt` :
- **requests** : Bibliothèque HTTP conviviale.
- **openai** : Bibliothèque pour interagir avec l'API d'OpenAI.
- **GitPython** : Bibliothèque Python pour interagir avec des dépôts Git.

Assurez-vous d'installer ces dépendances pour faire fonctionner le projet sans accroc ! 🚀

## 🖥️ Détails des Fonctions Clés

Le script `tool.py` est le cœur de ce projet, offrant les fonctionnalités suivantes :
- Chargement automatique du fichier de configuration pour gérer les paramètres du projet.
- Obtention interactive des fichiers du dépôt et génération d'un résumé des fichiers.
- Création, optimisation et traduction des fichiers README, avec possibilité de les soumettre via des opérations Git.

Vous pouvez également exécuter des commandes spécifiques via l'interface de ligne de commande pour répondre à différents besoins ! 🎈

## 🌸 Comment Utiliser ?

Vous pouvez choisir de forker ce projet, d'utiliser `GitHub Actions`, ou de le cloner pour une utilisation locale. Prenons l'utilisation de `GitHub Actions` comme exemple :

1. Ajoutez `PAT` et `OPENAI_API_KEY` aux secrets.
2. Accédez au fichier `config.json` pour configurer les paramètres pertinents.
3. Déclenchez manuellement le flux de travail que vous souhaitez exécuter.

Veuillez noter que `optimize.yml` et `translate.yml` nécessitent qu'un fichier README existe déjà dans le dépôt cible pour être exécutés.

## 📜 Licence

Ce projet est sous **la licence Apache 2.0**, voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contributions et Support

Nous accueillons vos contributions avec enthousiasme ! Si vous trouvez cet outil utile, merci de nous donner une ⭐️. Votre soutien est notre moteur pour continuer d'avancer ! 💪

---

Avec cet outil, vous pouvez créer facilement une documentation professionnelle et lisible. Essayez-le, économisez du temps et de l'énergie, ce projet mérite d'être mis en favoris ! 🌟