[Back to main language README](README.md)

# 📄 README Automatisches Generierungs- und Übersetzungstool

## Projektbeschreibung

Willkommen beim **README Automatisches Generierungs- und Übersetzungstool**! Dieses Tool wurde von **Delta-Water** entwickelt und zielt darauf ab, die Erstellung und Verwaltung von README-Dateien und deren Übersetzungen für GitHub-Repositories zu vereinfachen. Mit diesem Tool können Sie problemlos hochwertige README-Dokumente erstellen und in mehrere Sprachen übersetzen, um die Zugänglichkeit und Benutzerbeteiligung Ihres Projekts zu verbessern. 🌍

## Lizenz

Dieses Projekt unterliegt der [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0). Diese Lizenz beschreibt die Bedingungen für die Nutzung, Vervielfältigung und Verbreitung von Software und anderen Arbeiten. Benutzer haben unter Einhaltung der entsprechenden Bedingungen eine weltweite, nicht-exklusive und lizenzfreie Urheberrechts- und Patenterlaubnis zur Nutzung und Verteilung der Arbeit sowie deren abgeleiteter Werke. 📜

## Installationsschritte

Stellen Sie sicher, dass Sie Python 3.x und pip installiert haben. Anschließend können Sie die erforderlichen Abhängigkeiten mit den folgenden Schritten installieren:

1. Klonen Sie das Projekt-Repository:
   ```bash
   git clone <Ihre Projekt-Repository-Adresse>
   cd <Ihr Projekt-Verzeichnis>
   ```

2. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

Die Bibliotheken umfassen:
- `requests`: zur Vereinfachung von HTTP-Anfragen für die Interaktion mit Webdiensten und APIs.
- `openai`: bietet Zugang zur OpenAI API und unterstützt die Integration von Sprachmodellen und KI-Funktionen.
- `GitPython`: ermöglicht nahtlose Interaktionen mit Git-Repositories und unterstützt Versionierung, Commits und Branches. 🛠️

## Benutzeranleitung

Verwenden Sie das Skript `tool.py`, um README-Dateien und deren Übersetzungen automatisch zu generieren und zu verwalten:

1. Konfigurieren Sie die Datei `config.json`, um den Repositoriumsnamen, den Eigentümer und die Hauptsprache festzulegen.
2. Führen Sie den folgenden Befehl aus, um die README-Datei zu generieren:
   ```bash
   python tool.py
   ```
3. Wenn eine Übersetzung erforderlich ist, wird das Skript die generierte README-Dokumentation automatisch in die angegebenen Sprachen übersetzen. 🌐

## Beitragsleitlinien

Wir begrüßen Beiträge aus der Community! Sie können auf folgende Weise teilnehmen:
1. Forken Sie dieses Projekt.
2. Reichen Sie Ihre Änderungen ein und starten Sie einen Pull Request.
3. Machen Sie Vorschläge oder geben Sie Feedback zu Dokumentationen, Code oder anderen Aspekten des Projekts.

Bitte stellen Sie sicher, dass Sie das [Beitragsprotokoll](./CONTRIBUTING.md) dieses Projekts befolgen. 🤝

## Unterstützung

Wenn Sie während der Nutzung auf Probleme stoßen, zögern Sie nicht, diese in den Issues zu melden. Wir werden so schnell wie möglich reagieren und helfen! 😊

Vielen Dank für Ihre Unterstützung, und wir hoffen, Sie genießen die Nutzung dieses Werkzeugs! 🎉

---

Wenn Sie weitere Fragen oder Anregungen haben, kontaktieren Sie uns jederzeit. Wir freuen uns darauf, dieses Projekt gemeinsam mit Ihnen zu verbessern und zu erweitern! ✨