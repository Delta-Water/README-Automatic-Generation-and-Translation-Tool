[Back to main language README](README.md)

# README : README-Outil-De-Génération-Automatique-Et-De-Traduction 📄🌍

## Présentation du projet ✨

Bienvenue dans le projet **README-Outil-De-Génération-Automatique-Et-De-Traduction** ! Ce tool a pour objectif de simplifier le processus de génération et de traduction des fichiers README des dépôts GitHub. En combinant l'API GitHub et l'API OpenAI, notre outil est capable de générer automatiquement des documents README complets et de prendre en charge des traductions dans plusieurs langues, rendant ainsi votre projet plus accessible et compréhensible pour les utilisateurs du monde entier.

## Fonctionnalités 🚀

- **Gestion de configuration automatisée** : Charger les paramètres à partir de fichiers de configuration.
- **Interaction avec l'API GitHub** : Récupérer le contenu des fichiers d'un dépôt GitHub spécifié.
- **Intégration de l'API OpenAI** : Utiliser l'API OpenAI pour extraire le contenu des fichiers et générer un texte README captivant ainsi que des traductions.
- **Support multilingue** : Générer des versions traduites en fonction des langues prédéfinies.
- **Gestion du README** : Construire un fichier README comprenant plusieurs sections, telles que la présentation du projet et les étapes d'installation, tout en liant les versions traduites.
- **Contrôle de version** : Après avoir généré le README et ses traductions, soumettre automatiquement les modifications au dépôt GitHub pour maintenir le contrôle de version.

## Étapes d'installation ⚙️

Avant de commencer à utiliser cet outil, veuillez vous assurer d'avoir installé les éléments suivants :

1. **Cloner ce dépôt** :
   ```bash
   git clone https://github.com/Delta-Water/README-Outil-De-Génération-Automatique-Et-De-Traduction.git
   cd README-Outil-De-Génération-Automatique-Et-De-Traduction
   ```

2. **Installer les dépendances** :
   Utilisez `pip` pour installer les bibliothèques nécessaires au projet :
   ```bash
   pip install -r requirements.txt
   ```

3. **Fichier de configuration** : Créez ou éditez le fichier `config.json` dans le répertoire racine du projet, en définissant l'URL de l'API et d'autres options de configuration.

4. **Configurer la clé GitHub** : Dans la section “Secrets” de GitHub, configurez votre jeton d'accès personnel pour permettre à l'outil d'accéder à votre dépôt GitHub.

## Instructions d'utilisation 📋

1. **Configuration** : Assurez-vous que le fichier `config.json` est correctement configuré avec l'URL de l'API de base, la branche principale et l'index principal du langage de programmation.

2. **Exécuter l'outil** : Exécutez la commande suivante pour démarrer l'outil :
   ```bash
   python tool.py
   ```

3. **Déclencher manuellement les actions GitHub** : Vous pouvez également exécuter manuellement les actions GitHub, ou les configurer pour qu'elles s'exécutent automatiquement lors de nouveaux commits.

## Guide de contribution 🤝

Nous accueillons toutes les contributions ! Merci de suivre les étapes ci-dessous :
1. **Forkez ce dépôt**.
2. **Créez votre branche de fonctionnalités** :
   ```bash
   git checkout -b feature/MaFonctionnalité
   ```
3. **Soumettez vos modifications** :
   ```bash
   git commit -m "Ajouter une nouvelle fonctionnalité"
   ```
4. **Poussez sur votre branche** :
   ```bash
   git push origin feature/MaFonctionnalité
   ```
5. **Soumettez une demande de tirage**.

Merci pour votre soutien à ce projet ! Si vous avez des questions ou des suggestions, veuillez créer un problème ou contacter les mainteneurs du projet. 🙏

## Licence 📜

Ce projet est sous **Apache License, Version 2.0**. Veuillez consulter les documents associés pour obtenir les termes et conditions détaillés, afin d'assurer la légitimité et l'équité de la collaboration et de l'utilisation.

---

Merci d'utiliser **README-Outil-De-Génération-Automatique-Et-De-Traduction** ! Ensemble, faisons de l'open source un espace plus ouvert et collaboratif ! 💪