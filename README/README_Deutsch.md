- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatisches Generierungs- und Übersetzungstool für README

Willkommen beim **README-Automatic-Generation-and-Translation-Tool** Projekt! 🎉 Dieses Projekt zielt darauf ab, die Dokumentationserstellung und -übersetzung Ihrer GitHub-Projekte zu vereinfachen. So wird Ihre README-Datei professioneller und mehrsprachig, und Sie können Entwickler überall auf der Welt leicht ansprechen! 🌍✨

## 🚀 Projektstruktur

Hier ist ein Überblick über die Struktur des Projekts:

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
└── tool.py            # Hauptskript zur automatischen Generierung und Übersetzung von README
```

## 📜 Lizenzübersicht

Unser Projekt unterliegt der **Apache Lizenz 2.0**, was bedeutet, dass Sie unseren Code frei verwenden, modifizieren und verteilen können, solange Sie die ursprüngliche Lizenz und die dazugehörigen Hinweise beibehalten. 📝 Lassen Sie uns gemeinsam zur Förderung von Open-Source-Zusammenarbeit beitragen! 💪

## ⚙️ Konfigurationsdatei

`config.json` ist das Konfigurationszentrum Ihres Projekts. Damit können Sie relevante Parameter wie den Repository-Namen, die Eigentümerinformationen und die unterstützten Übersetzungssprachen (vereinfacht Chinese, traditionelles Chinesisch, Englisch, Spanisch, Französisch, Deutsch, Japanisch) einstellen, sodass Sie ganz einfach zwischen verschiedenen Sprachen wechseln und Mehrsprachigkeitsinhalte verwalten können. 🌐💻

## 📦 Abhängigkeiten

Unser Projekt benötigt folgende Bibliotheken, um sicherzustellen, dass Sie Ihre Entwicklungsumgebung problemlos einrichten können:

1. **requests** - Eine einfache HTTP-Anfragesbibliothek.
2. **openai** - Eine Bibliothek zur Interaktion mit der OpenAI API.
3. **GitPython** - Eine Bibliothek, um Git-Repositories mit Python zu verwalten.

Sie müssen nur den folgenden Befehl ausführen, um die Abhängigkeiten zu installieren:

```bash
pip install -r requirements.txt
```

## ⚙️ Funktionsübersicht

Das Skript `tool.py` bietet leistungsstarke Funktionen, darunter:

1. **Konfigurationsladen** - Lesen von Projektparametern aus der Konfigurationsdatei.
2. **Repository-Interaktion** - Abrufen von Repository-Dateien und deren Inhalten über die GitHub API.
3. **Inhaltszusammenfassung** - Nutzung der OpenAI API zur Zusammenfassung von Repository-Datei-Inhalten und Erstellung knapper Beschreibungen.
4. **README-Generierung** - Erstellen einer professionellen README-Datei basierend auf der Dateistruktur und den Zusammenfassungsinformationen.
5. **Übersetzung** - Übersetzung des README-Inhalts in mehrere Sprachen, wobei lebendige Emojis und Stile beibehalten werden. 😄🎨
6. **Git-Operationen** - Aktualisierte README- und Übersetzungsdateien ins Repository einpflegen.

## 🚀 Starten Sie Ihre Reise

Sie müssen nur den GitHub Actions Workflow manuell starten, ein paar Minuten warten, und die hervorragenden README-Dateien werden automatisch generiert und übersetzt. Genießen Sie all dies! ✨

### 🌟 Geben Sie uns doch bitte einen Stern! Ihre Unterstützung ist unsere Motivation, ständig besser zu werden! 💖

Vielen Dank für Ihr Interesse und Ihre Unterstützung! Bei Fragen oder Anregungen stehen wir Ihnen gerne auf GitHub zur Verfügung. Wir freuen uns darauf, gemeinsam mit Ihnen eine bessere Open-Source-Community zu schaffen! 🤝