[Back to main language README](README.md)

# README: README-Automatic-Generation-and-Translation-Tool 📄🌍

## Projektübersicht ✨

Willkommen bei **README-Automatic-Generation-and-Translation-Tool**! Dieses Tool zielt darauf ab, den Prozess der Erstellung und Übersetzung von README-Dateien für GitHub-Repositories zu vereinfachen. Durch die Kombination der GitHub API und der OpenAI API kann unser Tool automatisch umfassende README-Dokumente generieren und in verschiedene Sprachen übersetzen, wodurch Ihr Projekt für globale Nutzer besser zugänglich und verständlich wird.

## Funktionen 🚀

- **Automatisierte Konfigurationsverwaltung**: Einstellungen aus Konfigurationsdateien laden.
- **Interaktion mit der GitHub API**: Inhalte von bestimmten GitHub-Repositories abrufen.
- **Integration der OpenAI API**: Verwendung der OpenAI API zur Aufbereitung von Datei-Inhalten, um ansprechende README-Texte und Übersetzungen zu generieren.
- **Mehrsprachige Unterstützung**: Generierung übersetzter Versionen basierend auf vordefinierten Sprachkonfigurationen.
- **README-Verwaltung**: Erstellung von README-Dateien, die mehrere Teile wie Projekteinführung, Installationsschritte usw. beinhalten und verlinkte Übersetzungsversionen enthalten.
- **Versionskontrolle**: Nach der Generierung von README und Übersetzung werden Änderungen automatisch im GitHub-Repository eingegeben, um die Versionskontrolle zu gewährleisten.

## Installationsschritte ⚙️

Bevor Sie dieses Tool verwenden, stellen Sie bitte sicher, dass die folgenden Abhängigkeiten installiert sind:

1. **Repository klonen**:
   ```bash
   git clone https://github.com/Delta-Water/README-Automatic-Generation-and-Translation-Tool.git
   cd README-Automatic-Generation-and-Translation-Tool
   ```

2. **Abhängigkeiten installieren**:
   Installieren Sie die benötigten Bibliotheken mit `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurationsdatei**: Erstellen oder bearbeiten Sie die `config.json`-Datei im Hauptverzeichnis des Projekts, um die API-URLs und andere Konfigurationen festzulegen.

4. **GitHub-Tokens einrichten**: Konfigurieren Sie Ihr persönliches Zugriffstoken im Bereich "Secrets" von GitHub, damit das Tool auf Ihr GitHub-Repository zugreifen kann.

## Gebrauchsanweisung 📋

1. **Konfiguration**: Stellen Sie sicher, dass die `config.json`-Datei die Basis-API-URL, den Hauptbranch und den Index der Hauptprogrammiersprache korrekt konfiguriert hat.

2. **Tool ausführen**: Führen Sie den folgenden Befehl aus, um das Tool zu starten:
   ```bash
   python tool.py
   ```

3. **Manueller Trigger von GitHub Actions**: Sie können auch GitHub Actions manuell ausführen oder so konfigurieren, dass sie bei neuen Commits automatisch ausgeführt werden.

## Beitragsrichtlinien 🤝

Wir freuen uns über jede Art von Beitrag! Bitte befolgen Sie die folgenden Schritte:
1. **Forken Sie dieses Repository**.
2. **Erstellen Sie Ihren Feature-Branch**:
   ```bash
   git checkout -b feature/MyFeature
   ```
3. **Committen Sie Ihre Änderungen**:
   ```bash
   git commit -m "Add some feature"
   ```
4. **Pushen Sie zum Branch**:
   ```bash
   git push origin feature/MyFeature
   ```
5. **Erstellen Sie einen Pull-Request**.

Vielen Dank für Ihre Unterstützung dieses Projekts! Wenn Sie Fragen oder Vorschläge haben, erstellen Sie bitte ein Issue oder kontaktieren Sie die Projektverwalter. 🙏

## Lizenz 📜

Dieses Projekt folgt der **Apache-Lizenz, Version 2.0**. Bitte lesen Sie die entsprechenden Dokumente, um detaillierte Bestimmungen und Bedingungen zu erfahren und um die Legalität und Fairness der Kooperation und Nutzung zu gewährleisten.

---

Vielen Dank, dass Sie **README-Automatic-Generation-and-Translation-Tool** verwenden! Lassen Sie uns die Open-Source-Welt offener und kollaborativer gestalten! 💪