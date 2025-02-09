- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Automatisch generiertes und übersetztes README-Tool 🛠️✨

Willkommen beim **automatisch generierten und übersetzten README-Tool**! Dieses Tool soll die Verwaltung und Übersetzung von README-Dateien in GitHub-Repositories vereinfachen und verbessern. Egal, ob Sie Projektbetreuer oder neuer Benutzer sind, es wird Ihren Workflow effizienter und angenehmer machen! 😄

## Projektstruktur 🗂️

Hier ist die Verzeichnisstruktur, die Ihnen hilft, die Verwendung jeder Datei und jedes Ordners schnell zu verstehen:

```
.github
└── workflows
    ├── generate.yml         # Workflow zur automatischen Generierung von README-Dateien
    ├── optimize.yml         # Workflow zur automatischen Optimierung von README-Dateien
    └── translate.yml        # Workflow zur automatischen Übersetzung von README-Dateien

LICENSE                        # Projektlizenzdatei
README.md                     # Haupt-README-Datei des Projekts
README
├── README_Deutsch.md        # Deutsche README
├── README_English.md        # Englische README
├── README_Español.md        # Spanische README
├── README_Français.md       # Französische README
├── README_日本語.md         # Japanische README
└── README_繁体中文.md      # Chinesische (traditionelle) README

config.json                   # Konfigurationsdatei
requirements.txt              # Python-Abhängigkeitsdatei
tool.py                       # Skript für das Automatisierungstool
```

## Workflow-Übersicht 🚀

### 1. `generate.yml`
Dieser GitHub Actions-Workflow dient zur automatischen Generierung und Aktualisierung von README-Dateien. Die Hauptschritte umfassen:

- Code auschecken
- Python 3.8 Umgebung einrichten
- Benötigte Abhängigkeiten installieren ( `requests`, `openai`, `GitPython`)
- Skript ausführen ( `tool.py generate`), um die README-Datei zu generieren oder zu aktualisieren
- Git konfigurieren und die aktualisierte README-Datei pushen

Dieser Prozess vereinfacht die Wartung von README-Dateien, sodass Sie sich auf wichtigere Aufgaben konzentrieren können! 😎

### 2. `optimize.yml`
Dieser Workflow optimiert automatisch README-Dateien und kann über das `workflow_dispatch`-Ereignis manuell ausgelöst werden. Wichtige Schritte umfassen:

- Code auschecken
- Python 3.8 Umgebung einrichten
- Abhängigkeiten installieren
- Skript ausführen ( `tool.py optimize`), um den Inhalt der README zu verbessern
- Die aktualisierte README-Datei committen und pushen

Lassen Sie uns gemeinsam die Inhaltsqualität verbessern! 💪

### 3. `translate.yml`
Dieser Workflow übersetzt automatisch README-Dateien, damit Ihr Projekt ein breiteres Publikum erreichen kann. Die Schritte umfassen:

- Code auschecken
- Python 3.8 Umgebung einrichten
- Abhängigkeiten installieren
- Übersetzungsskript ausführen ( `tool.py`)

Es ist Ihr ultimativer Helfer in einer mehrsprachigen Welt! 🌍

## Lizenz 📄
Dieses Projekt folgt der Apache-Lizenz 2.0, die Ihnen erlaubt, den Code zu verwenden, zu modifizieren und zu verteilen, während Ihre Rechte und Pflichten gewahrt bleiben.

## Konfigurationsverwaltung 🛠️
Die Datei `config.json` definiert wichtige Einstellungen wie API-Endpunkte und unterstützte Übersetzungssprachen, um einen reibungslosen Betrieb des Tools und die Unterstützung von Mehrsprachigkeit sicherzustellen. 🤓

## Abhängigkeitsverwaltung 🐍
Die Datei `requirements.txt` listet die notwendigen Python-Pakete auf, darunter:

- **requests**: Vereinfachung von HTTP-Anfragen
- **openai**: Zugriff auf die OpenAI API für verschiedene Operationen
- **GitPython**: Interaktion mit Git-Repositories in Python

Bitte stellen Sie sicher, dass Sie diese Abhängigkeiten installieren, um einen reibungslosen Betrieb des Tools zu gewährleisten! 🌟

## So verwenden Sie es?

Sie können entweder dieses Projekt forken und `GitHub Actions` verwenden oder es lokal klonen.

Hier ist ein Beispiel für die Verwendung von GitHub Actions:

1. Fügen Sie in den GitHub-Secrets `PAT` und `OPENAI_API_KEY` hinzu.
2. Bearbeiten Sie die Parameter in `config.json`.
3. Wenn Sie die README-Datei generieren und übersetzen möchten:
   - Führen Sie manuell den Workflow `generate` aus, um eine `.README.md`-Datei im Stammverzeichnis des Repositories zu generieren.
   - Überprüfen und ändern Sie diese Datei, bevor Sie sie committen.
   - Manuelle Auslösung des Workflows `translate`, das Tool wird die bearbeitete README in das Ziel-Repository hinzufügen und eine Übersetzung generieren.

Fertig! 🎉

Wenn Sie bereits eine README-Datei haben und nur eine Übersetzung wünschen:
- Pushen Sie sie in die `.README.md`-Datei des Tool-Repositories.
- Manuell den Workflow `translate` auslösen.

Fertig! 🎉

## Feedback und Mitwirkung 🙌
Wir freuen uns über Ihr Feedback und Ihre Vorschläge! Bitte geben Sie diesem Projekt ein ⭐️ und beteiligen Sie sich daran, um die Qualität und Benutzerfreundlichkeit des Projekts zu verbessern.

Vielen Dank für Ihr Interesse und Ihre Unterstützung! Lassen Sie uns gemeinsam README-Dateien lebendiger und interessanter gestalten! 🎉