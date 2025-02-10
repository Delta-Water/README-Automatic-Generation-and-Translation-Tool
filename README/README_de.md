<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automatisches README-Generierungs- und Übersetzungstool

Willkommen in der Welt des **Automatischen README-Generierungs- und Übersetzungstools**! 🎉 Dieses Projekt bietet Entwicklern und Projektbetreuern eine effiziente und bequeme Lösung, um README-Dateien einfach zu erstellen, zu optimieren und zu übersetzen, und um professionelles und ansprechendes Dokumentation für den Code bereitzustellen. Egal, ob Sie ein Anfänger oder ein erfahrener Entwickler sind, hier finden Sie die Werkzeuge, die Sie brauchen! 🌟

## 🛠️ Projektstruktur

Hier ist die grundlegende Struktur des Projekts, die Ihnen den Überblick erleichtert:

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # Workflow zum automatischen Generieren von README-Dateien
│       ├── optimize.yml      # Workflow zur Optimierung von README-Dateien
│       └── translate.yml      # Workflow zum Übersetzen von README-Dateien
├── LICENSE                   # Projektlizenz
├── README.md                 # Projektdokumentation
├── config.json               # Konfigurationsdatei des Tools
├── requirements.txt          # Liste der Abhängigkeiten
└── tool.py                   # Automatisches Skript
```

## ✨ Kernfunktionen

1. **Automatisches README-Generieren**: Mit GitHub Actions kann aus dem Projektcode automatisch eine professionelle README-Datei erstellt werden.
2. **Optimierungsfunktion**: Durch die OpenAI-API wird eine KI-gesteuerte Optimierung realisiert, die die Qualität bestehender README-Dokumente verbessert.
3. **Übersetzungskapazität**: Automatische Übersetzung der README-Datei in mehrere Sprachen, um einem breiteren Publikum den Zugriff auf Ihr Projekt zu erleichtern.👌

## ⚙️ Workflows

### 1. `generate.yml`
- Manuelle Auslösung, die README-Datei wird durch `workflow_dispatch` generiert.
- Wird in einer Ubuntu-Umgebung ausgeführt, installiert die erforderlichen Abhängigkeiten (`requests`, `openai`, `GitPython`).
- Schließlich wird das Skript `tool.py generate` ausgeführt, um die professionelle README zu erstellen.

### 2. `optimize.yml`
- Manuelle Auslösung, automatisierte Optimierung der vorhandenen README-Datei.
- Enthält Schritte zur Codeüberprüfung, Einrichtung der Python-Umgebung und Installation der Abhängigkeiten.
- Ausführung des Skripts `tool.py optimize`, um die Lesbarkeit der README zu verbessern.

### 3. `translate.yml`
- Manuelle Auslösung, automatische Übersetzung der README-Datei.
- Nach dem Auschecken des Codes, Einrichten der Python-Umgebung und Installation der erforderlichen Abhängigkeiten wird das Übersetzungsskript gestartet.

## 📝 Konfigurationsbeschreibung

Die Datei `config.json` enthält die grundlegende Konfiguration und Optionen des Tools, einschließlich:
- Name und Eigentümer des Repositories
- Basis-URL der API und verwendetes Sprachmodell
- Sprachen, die übersetzt werden sollen, sowie deren Abkürzungen
- …

Bitte stellen Sie sicher, dass Sie diese Datei korrekt konfigurieren, um eine reibungslose Funktion des Tools zu gewährleisten. 🔑

## 📦 Abhängigkeiten

In `requirements.txt` finden Sie die benötigten Abhängigkeiten des Projekts:
- **requests**: Benutzerfreundliche HTTP-Anforderungsbibliothek.
- **openai**: Bibliothek zur Interaktion mit der OpenAI-API.
- **GitPython**: Python-Bibliothek zur Interaktion mit Git-Repositories.

Bitte stellen Sie sicher, dass Sie diese Abhängigkeiten installieren, um das Projekt reibungslos auszuführen! 🚀

## 🖥️ Detaillierte Funktionen

Das Skript `tool.py` ist das Herzstück dieses Projekts und bietet folgende Funktionen:
- Automatisches Laden der Konfigurationsdatei und Verwaltung der Projekteinstellungen.
- Interaktive Abfrage von Repository-Dateien und Generierung von Dateizusammenfassungen.
- Erstellen, Optimieren und Übersetzen von README-Dateien sowie Durchführung von Git-Operationen zur Einreichung.

Sie können auch bestimmte Befehle über die Kommandozeile flexibel ausführen, um verschiedene Anforderungen zu erfüllen! 🎈

## 🌸 So benutzen Sie es?

Sie können dieses Projekt forken, `GitHub Actions` nutzen oder es lokal klonen. Hier ein Beispiel für die Verwendung von `GitHub Actions`:

1. Fügen Sie `PAT` und `OPENAI_API_KEY` zu den Secrets hinzu.
2. Konfigurieren Sie die entsprechenden Parameter in `config.json`.
3. Lösen Sie den gewünschten Workflow manuell aus.

Bitte beachten Sie, dass `optimize.yml` und `translate.yml` nur ausgeführt werden können, wenn im Zielrepository bereits eine README-Datei vorhanden ist.

## 📜 Lizenz

Dieses Projekt folgt der **Apache License 2.0**, weitere Informationen finden Sie in der Datei `LICENSE`.

## 🤝 Beiträge und Unterstützung

Wir freuen uns sehr über Ihre Beiträge! Wenn Sie denken, dass dieses Tool Ihnen hilft, geben Sie uns bitte ein ⭐️. Ihre Unterstützung ist unsere Motivation, weiterzumachen! 💪

---

Mit diesem Tool können Sie professionelle und leicht lesbare Dokumentationen problemlos erstellen. Probieren Sie es aus, sparen Sie Zeit und Mühe, und machen Sie dieses Projekt zu Ihrem Favoriten! 🌟