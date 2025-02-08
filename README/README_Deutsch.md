- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Projektname

Willkommen zu unserem Projekt!✨ Dieses Projekt zielt darauf ab, README-Dateien automatisch zu generieren und zu übersetzen, um umfassende Dokumentationsunterstützung für Ihr GitHub-Repository zu bieten. Lassen Sie uns als Nächstes die Struktur des Projekts und die detaillierte Beschreibung jeder Datei ansehen!

## Projektstruktur

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/main.yml": "main.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "config.json": "config.json",
  "requirements.txt": "requirements.txt",
  "tool.py": "tool.py"
}
```

### Detaillierte Dateibeschreibung

#### `.github/workflows/main.yml`
Dies ist die Schlüsseldatei zur Definition des GitHub Actions-Workflows mit dem Namen „Automatisch README generieren und übersetzen“.🔄 
Sie wird durch manuelles Auslösen des `workflow_dispatch`-Ereignisses gestartet. Sie beinhaltet einen Task mit dem Namen „build“, der in einer Ubuntu-Umgebung läuft. Das Ziel dieses Workflows ist die Automatisierung der Erstellung und Übersetzung von README-Dateien, um das manuelle Aktualisieren zu vermeiden.

#### `LICENSE`
Diese Datei enthält den vollständigen Text der Apache License Version 2.0 und umreißt die Bedingungen und Vorschriften für die Nutzung, Vervielfältigung und Verteilung der Software und ihrer Derivate.🛡️ 
Sie bietet den Benutzern weitreichende Berechtigungen zur Modifikation, Nutzung und Verteilung der durch diese Lizenz geschützten Werke, legt aber auch bestimmte Verpflichtungen fest. Mit dieser Lizenz hoffen wir, offene Zusammenarbeit und den Austausch von geistigem Eigentum zu fördern.

#### `README.md`
Dies ist die Haupt-README-Datei des Projekts, die den Benutzern einen Überblick über das Projekt, Nutzungshinweise und andere wichtige Informationen bietet.📊 
Hier haben wir alle wichtigen Informationen zum Projekt zusammengefasst, um den Benutzern den schnellen Einstieg zu erleichtern!

#### `README`-Ordner
- `README/README_Deutsch.md`: Deutsche Übersetzung.
- `README/README_English.md`: Englische Übersetzung.
- `README/README_Español.md`: Spanische Übersetzung.
- `README/README_Français.md`: Französische Übersetzung.
- `README/README_日本語.md`: Japanische Übersetzung.
- `README/README_繁体中文.md`: Übersetzung in Traditionelles Chinesisch.

Dieser Ordner enthält mehrsprachige Versionen der Projekt-README, damit Benutzer weltweit das Projekt einfach verstehen und verwenden können.🌍📚

#### `config.json`
Diese Datei ist die Konfigurationsdatei für das Tool zur automatischen Generierung und Übersetzung von README-Dokumenten.🔧 
Sie enthält Parameter wie den Repositories-Namen, den Eigentümer, die Basis-URL für den API-Zugriff, den verwendeten Hauptbranch und die unterstützten Übersetzungssprachen. Das Ziel der Konfiguration ist es, den Prozess der Lokalisierung und Übersetzung der Projektdokumentation zu vereinfachen.

#### `requirements.txt`
Dies ist eine Standard-Python-Abhängigkeitenliste, die sicherstellt, dass die Entwicklungsumgebung die erforderlichen externen Bibliotheken und Abhängigkeiten für den reibungslosen Betrieb des Projekts bereitstellt.📦 
Dazu gehören:
1. **requests**: Eine Bibliothek für die einfache Interaktion mit Webdiensten und REST-APIs.
2. **openai**: Eine Bibliothek, die den Zugriff auf die OpenAI API ermöglicht und natürliche Sprachverarbeitung sowie Machine-Learning-Aufgaben unterstützt.
3. **GitPython**: Eine Bibliothek, die es Benutzern ermöglicht, programmgesteuert mit Git-Repositories zu interagieren.

#### `tool.py`
Dies ist ein Python-Skript zur automatischen Erstellung und Aktualisierung der README-Datei eines GitHub-Repositories.🤖 
Die Hauptfunktionen sind:
- Laden von Konfigurationsparametern.
- Interaktion mit dem GitHub-Repository zur Extraktion von Dateistruktur und -inhalten.
- Nutzung der OpenAI API zur Erstellung von Datei-Zusammenfassungen.
- Zusammenstellung der generierten Zusammenfassungen und Struktur zur Erstellung einer professionellen README-Datei.
- Übersetzung des README-Inhalts in mehrere Sprachen, um die Zugänglichkeit zu erhöhen.
- Aktualisierung der README- und Übersetzungsdateien und Rückübermittlung der Änderungen an GitHub.

### 📢 Legen Sie los!
Wenn Sie denken, dass dieses Projekt Ihnen hilfreich ist, zögern Sie nicht, uns ⭐️ zu geben! Jeder Stern ist eine Anerkennung unserer Arbeit! Vielen Dank für Ihre Unterstützung, und lassen Sie uns gemeinsam den Fortschritt von Open Source fördern!🚀

--- 

Wenn Sie Fragen oder Vorschläge haben, können Sie uns jederzeit kontaktieren! Wir freuen uns auf Ihr wertvolles Feedback!❤️