[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) | [English](/README/README_en.md) | [Español](/README/README_es.md) | [Français](/README/README_fr.md) | [日本語](/README/README_ja.md)

- [Sprache wechseln: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatisches Generieren und Übersetzen von README-Tools

Willkommen im **README-Automatic-Generation-and-Translation-Tool** Projekt! 🎉 Dieses Projekt zielt darauf ab, die Erstellung und Übersetzung Ihrer GitHub-Projektdokumentation zu vereinfachen, damit Ihre README-Dateien professioneller und mehrsprachig werden. Egal, wo Sie sich befinden, Sie können ganz einfach mehr Entwickler anziehen! 🌍✨

## 🚀 Projektstruktur

Hier ist ein Überblick über die Projektstruktur:

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions Workflow-Datei
│
├── LICENSE            # Apache Lizenz 2.0
│
├── README.md          # Haupt-README-Datei des Projekts
│
├── README/
│   ├── README_Deutsch.md     # Deutsche README 
│   ├── README_English.md      # Englische README 
│   ├── README_Español.md      # Spanische README 
│   ├── README_Français.md     # Französische README 
│   ├── README_日本語.md        # Japanische README 
│   └── README_繁体中文.md      # Traditionelle Chinesische README 
│
├── config.json       # Konfigurationsdatei mit Einstellungen und Übersetzungssprachen
│
├── requirements.txt   # Abhängigkeiten des Projekts
│
└── tool.py            # Hauptskript zum automatischen Generieren und Übersetzen von README
```

## 📜 Lizenzübersicht

Unser Projekt verwendet die **Apache Lizenz 2.0**, was bedeutet, dass Sie unseren Code frei nutzen, ändern und verbreiten können, solange Sie die ursprüngliche Lizenz und die entsprechenden Hinweise beibehalten. 📝 Lassen Sie uns gemeinsam die Open-Source-Zusammenarbeit fördern! 💪

## ⚙️ Konfigurationsdatei

`config.json` ist das Konfigurationszentrum Ihres Projekts. Es ermöglicht Ihnen, relevante Parameter wie den Repository-Namen, Informationen über den Besitzer und unterstützte Übersetzungssprachen (vereinfachtes Chinesisch, traditionelles Chinesisch, Englisch, Spanisch, Französisch, Deutsch, Japanisch) festzulegen, damit Sie mehrsprachige Inhalte mühelos wechseln und verwalten können. 🌐💻

## 📦 Abhängigkeiten

Unser Projekt ist auf folgende Bibliotheken angewiesen, um Ihnen einen einfachen Aufbau der Entwicklungsumgebung zu ermöglichen:

1. **requests** - Eine einfache HTTP-Anfragebibliothek.
2. **openai** - Eine Bibliothek zur Interaktion mit der OpenAI API.
3. **GitPython** - Eine Bibliothek zur Arbeit mit Git-Repositories in Python.

Sie müssen nur den folgenden Befehl ausführen, um die Abhängigkeiten zu installieren:

```bash
pip install -r requirements.txt
```

## ⚙️ Funktion Übersicht

Das Skript `tool.py` bietet leistungsstarke Funktionen, darunter:

1. **Konfiguration laden** - Projektparameter aus der Konfigurationsdatei lesen.
2. **Repository-Interaktion** - Dateien und Inhalte des Repositories über die GitHub-API abrufen.
3. **Inhaltszusammenfassung** - Inhalt von Repository-Dateien mit der OpenAI-API zusammenfassen und prägnante Beschreibungen erstellen.
4. **README generieren** - Professionelle README-Dateien basierend auf der Dateistruktur und den Zusammenfassungsinformationen erstellen.
5. **Übersetzung** - Den README-Inhalt in mehrere Sprachen übersetzen, während lebendige Emojis und Stile beibehalten werden. 😄🎨
6. **Git-Operationen** - Aktualisierte README- und Übersetzungsdateien ins Repository übermitteln.

## 🚀 Starten Sie Ihre Reise

Starten Sie einfach den GitHub Actions Workflow manuell, warten Sie ein paar Minuten, und die großartigen README-Dateien werden automatisch erzeugt und übersetzt. Genießen Sie all die Schönheit! ✨

### 🌟 Geben Sie uns einen Stern! Ihre Unterstützung ist unsere treibende Kraft! 💖

Danke für Ihr Interesse und Ihre Unterstützung! Bei Fragen oder Anregungen können Sie sich jederzeit auf GitHub an uns wenden. Wir freuen uns darauf, gemeinsam mit Ihnen eine bessere Open-Source-Community zu schaffen! 🤝