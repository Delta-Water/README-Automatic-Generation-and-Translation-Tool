- [切换语言: 简体中文](/README.md) | - [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatisches Generieren und Übersetzen von README-Tools

Willkommen beim **README-Automatic-Generation-and-Translation-Tool** Projekt! 🎉 Dieses Projekt zielt darauf ab, die Erstellung und Übersetzung Ihrer GitHub-Projektdokumentation zu vereinfachen, damit Ihre README-Datei professioneller und mehrsprachig wird. Egal, wo Sie sich befinden, Sie können ganz einfach mehr Entwickler anziehen! 🌍✨

## 🚀 Projektstruktur

Hier ist eine Übersicht über die Projektstruktur:

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

Unser Projekt verwendet die **Apache Lizenz 2.0**, was bedeutet, dass Sie unseren Code frei nutzen, verändern und verteilen dürfen, solange Sie die ursprüngliche Lizenz und die entsprechenden Erklärungen beibehalten. 📝 Lassen Sie uns gemeinsam die Open-Source-Zusammenarbeit fördern! 💪

## ⚙️ Konfigurationsdatei

`config.json` ist das Konfigurationszentrum Ihres Projekts. Es ermöglicht Ihnen, relevante Parameter wie Repository-Namen, Eigentümerinformationen und unterstützte Übersetzungssprachen (Vereinfacht Chinesisch, Traditionell Chinesisch, Englisch, Spanisch, Französisch, Deutsch, Japanisch) festzulegen, sodass Sie mühelos zwischen mehrsprachigen Inhalten wechseln und diese verwalten können. 🌐💻

## 📦 Abhängigkeiten

Unser Projekt ist auf die folgenden Bibliotheken angewiesen, um sicherzustellen, dass Sie Ihre Entwicklungsumgebung einfach einrichten können:

1. **requests** - Ein einfaches HTTP-Anfrage-Bibliothek.
2. **openai** - Bibliothek zur Interaktion mit der OpenAI API.
3. **GitPython** - Bibliothek für die Arbeit mit Git-Repositories in Python.

Sie müssen nur den folgenden Befehl ausführen, um die Abhängigkeiten zu installieren:

```bash
pip install -r requirements.txt
```

## ⚙️ Funktionalitätsübersicht

Das Skript `tool.py` bietet leistungsstarke Funktionen, darunter:

1. **Konfiguration laden** - Projektparameter aus der Konfigurationsdatei lesen.
2. **Repository-Interaktion** - Repository-Dateien und deren Inhalte über die GitHub API abrufen.
3. **Inhaltszusammenfassung** - Nutzung der OpenAI API, um den Inhalt der Repository-Dateien zusammenzufassen und eine prägnante Beschreibung zu erstellen.
4. **README-Generierung** - Professionelle README-Dateien basierend auf Struktur und Zusammenfassungsinformationen erstellen.
5. **Übersetzung** - README-Inhalte in mehrere Sprachen übersetzen, während lebhafte Emojis und Stile beibehalten werden. 😄🎨
6. **Git-Operationen** - Aktualisierte README- und Übersetzungsdateien ins Repository hochladen.

## 🚀 Starten Sie Ihre Reise

Starten Sie einfach den GitHub Actions Workflow manuell, warten Sie ein paar Minuten, und hervorragende README-Dateien werden automatisch generiert und übersetzt. Genießen Sie all die schönen Dinge! ✨

### 🌟 Kommen Sie und geben Sie uns ein Sternchen! Ihre Unterstützung ist unser Antrieb, weiterzumachen! 💖

Vielen Dank für Ihr Interesse und Ihre Unterstützung! Bei Fragen oder Vorschlägen können Sie sich jederzeit über GitHub mit uns in Verbindung setzen. Wir freuen uns darauf, gemeinsam mit Ihnen eine bessere Open-Source-Community zu schaffen! 🤝