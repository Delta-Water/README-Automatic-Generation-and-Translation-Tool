- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - Automatisches Generierungs- und Übersetzungstool 🌟

Willkommen beim **README-Automatic-Generation-and-Translation-Tool** Projekt! 🚀

Wir setzen uns dafür ein, Entwicklern ein automatisiertes Werkzeug zur Verfügung zu stellen, um README-Dateien von GitHub-Projekten einfach zu erstellen und zu übersetzen, damit deine Projektdokumentation ansprechender und professioneller wird! 💕

## Projektstruktur 📂

Hier ist die aktuelle Struktur des Projekts, mit Erklärungen zu den verschiedenen Dateien:

```
├── .github
│   └── workflows
│       └── main.yml     # Konfigurationsdatei für den GitHub Actions Workflow
├── LICENSE                # Projektlizenzdatei
├── README.md              # Hauptdokumentation des Projekts
├── README
│   ├── README_Deutsch.md  # Deutsche README-Datei
│   ├── README_English.md  # Englische README-Datei
│   ├── README_Español.md  # Spanische README-Datei
│   ├── README_Français.md # Französische README-Datei
│   ├── README_日本語.md    # Japanische README-Datei
│   └── README_繁体中文.md   # Traditionelle chinesische README-Datei
├── config.json            # Projektkonfigurationsdatei
├── requirements.txt       # Liste der Python-Abhängigkeiten
└── tool.py                # Skript zur automatischen Erstellung und Aktualisierung der README-Dateien
```

## Dateizusammenfassung 📄

### 1. `.github/workflows/main.yml`
Diese Konfigurationsdatei für den GitHub Actions Workflow ermöglicht es uns, die Erstellung und Übersetzung der README-Dateien zu automatisieren. Sie läuft in einer aktuellen Version der Ubuntu-Umgebung und führt folgende Schritte aus:

- **Code auschecken**: Die neuesten Codeänderungen abrufen.
- **Python einrichten**: Python 3.8 als Umgebung konfigurieren.
- **Abhängigkeiten installieren**: pip aktualisieren und erforderliche Python-Pakete (requests, openai, GitPython) installieren.
- **Skript ausführen**: Das Python-Skript (tool.py) ausführen, um mit GitHub- und OpenAI-API-Anmeldeinformationen die README zu generieren.

### 2. `LICENSE`
Diese Datei enthält die Apache-Lizenz, Version 2.0, die die Bedingungen und Konditionen für die Nutzung, Kopie und Verbreitung von Software und anderen Werken umreißt. Die Lizenz bietet einen rechtlichen Rahmen, der die Entwicklung von Open-Source-Software fördert und die Rechte der Beitragsleistenden und der Benutzer schützt.

### 3. `config.json`
Diese Konfigurationsdatei definiert wichtige Parameter für das Projekt, wie: Repository-Name, Besitzer, grundlegende API-URL und den Standardbranch (main). Sie unterstützt die automatische Erstellung und Übersetzung der README-Dateien.

### 4. `requirements.txt`
Hier sind die erforderlichen Abhängigkeiten für das Python-Projekt aufgeführt:

- **requests**: Beliebte Bibliothek zur Vereinfachung von HTTP-Anfragen.
- **openai**: Bibliothek zur Interaktion mit der OpenAI-API.
- **GitPython**: Bibliothek zur direkten Bearbeitung und Interaktion mit Git-Repositories aus Python.

### 5. `tool.py`
Dieses Skript automatisiert die Erstellung und Aktualisierung von README-Dateien und deren Übersetzungen in GitHub-Repositories. Zu den Hauptfunktionen gehören:

1. **Konfiguration und Setup**: Konfiguration laden und erforderliche Umgebungsvariablen abrufen.
2. **Dateimanagement**: Zugriff auf das GitHub-Repository, um die Dateistruktur und den Inhalt abzurufen.
3. **README-Erstellung**: Verwendung der OpenAI-API zur Erstellung detaillierter README-Dateien.
4. **Übersetzung erstellen**: Generierte README in mehrere Sprachen übersetzen.
5. **Verknüpfung und Struktur integrieren**: Erhöhung der Navigierbarkeit.
6. **Commit und Push**: Aktualisierte Dateien im GitHub-Repository speichern.

## Schnellstart 🚀

Möchtest du mitmachen? Klicke auf den ⭐ in der oberen rechten Ecke, um unser Projekt zu unterstützen! 💖 

Mit diesem Tool helfen wir jedem Entwickler, die Projektdokumentation einfach zu pflegen und das Projekt auf internationaler Ebene zu fördern! Egal, ob dein Projekt groß oder klein ist, wir helfen dir, die Dokumentation stressfrei zu gestalten und gemeinsam ein besseres Open-Source-Ökosystem zu schaffen! 🌍👩‍💻👨‍💻

Wenn du Fragen oder Vorschläge hast, zögere nicht, uns zu kontaktieren! Happy Coding! 🎉