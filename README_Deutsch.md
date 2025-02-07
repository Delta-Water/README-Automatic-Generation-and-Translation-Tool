# Automatisches Generierungs- und Übersetzungstool 📄🌍

## Projektübersicht

Das automatisches Generierungs- und Übersetzungstool ist ein Open-Source-Projekt basierend auf Python, das darauf abzielt, die Erstellung von README-Dateien und den mehrsprachigen Übersetzungsprozess zu vereinfachen. Dieses Tool integriert die GitHub-API und das Sprachmodell von OpenAI, um qualitativ hochwertige README-Dateien automatisiert zu erstellen und diese in verschiedene Sprachen zu übersetzen. Dies hilft den Projektbetreuern, die Zugänglichkeit der Dokumentation und die Benutzererfahrung zu verbessern. 🚀

## Funktionen 🛠️

- **Automatische Inhaltserstellung**: Holt Dateien aus einem angegebenen GitHub-Repository und generiert die README-Dokumentation des Projekts.
- **Mehrsprachige Übersetzung**: Verwendet fortschrittliche Übersetzungstechnologien, um die README-Dokumentation in mehrere Sprachen zu konvertieren.
- **Einfache Konfiguration**: Verwalten der Interaktion mit dem GitHub-Repository über einfache JSON-Konfigurationsdateien.
- **Effiziente Dokumentenverwaltung**: Automatisierte Aktualisierung und Übermittlung der generierten README-Dateien sowie deren Übersetzungen an GitHub. 📥

## Installationsschritte 🔧

1. **Repository klonen**:
   ```bash
   git clone <Repository-URL>
   cd <Repository-Verzeichnis>
   ```

2. **Abhängigkeiten installieren**:
   Installieren Sie die erforderlichen Python-Bibliotheken im Wurzelverzeichnis des Projekts mit folgendem Befehl:
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurationsdatei**:
   Bearbeiten Sie die `config.json`-Datei, um `repo_url` auf die gewünschte GitHub-Repository-Adresse einzustellen und andere Einstellungen wie `branch` und `main_language_index` auf den Standardwerten zu belassen.

## Benutzungsanleitung 📖

1. **Tool ausführen**:
   Verwenden Sie den folgenden Befehl, um das Tool zu starten und die README-Dokumentation zu generieren und zu übersetzen:
   ```bash
   python tool.py
   ```

2. **Zugriffstoken speichern**:
   Stellen Sie sicher, dass das GitHub-Zugriffstoken in der Umgebung gesetzt ist, damit das Tool erfolgreich auf den Inhalt des Repositories zugreifen kann.

## Beitragende Anleitung 🤝

Wir freuen uns über jede Art von Beiträgen! Sie können durch die folgenden Schritte am Projekt teilnehmen:

1. **Forken Sie dieses Repository**.
2. **Erstellen Sie einen Feature-Branch**:
   ```bash
   git checkout -b feature/neues_feature
   ```
3. **Änderungen committen**:
   ```bash
   git commit -m "Neues Feature hinzugefügt"
   ```
4. **In remote pushen**:
   ```bash
   git push origin feature/neues_feature
   ```
5. **Pull-Anfrage einreichen**.

## Lizenz 📜

Dieses Projekt steht unter [Apache Lizenz 2.0](http://www.apache.org/licenses/LICENSE-2.0). Sie können dieses Software frei verwenden und verteilen, müssen jedoch die Bedingungen der Lizenz einhalten.

---

Vielen Dank für Ihr Interesse und Ihre Unterstützung für das automatisches Generierungs- und Übersetzungstool! Wenn Sie Fragen oder Anregungen haben, zögern Sie nicht, im Projekt-Tracker Feedback zu hinterlassen. ✉️