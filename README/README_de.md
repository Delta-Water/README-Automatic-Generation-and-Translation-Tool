<div align="center">

[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automatisches README-Generierungs- und Übersetzungstool

Willkommen im **README Automatisierungs-Generierungs- und Übersetzungstool**-Projekt! 🎉 Dieses Projekt soll Entwicklern und Projektpflegepersonen eine bequeme Möglichkeit bieten, README-Dateien einfach zu generieren, zu optimieren und zu übersetzen. Egal, ob du Anfänger oder Experte bist, mit nur wenigen einfachen Schritten erhältst du ein professionelles, ansprechendes README-Dokument! 🚀

## 📂 Projektstruktur

```plaintext
./
└── workflows/
│   ├── generate.yml      # Workflow zur automatischen Generierung der README-Datei
│   ├── optimize.yml      # Workflow zur automatischen Optimierung der README-Dokumentation
│   └── translate.yml      # Workflow zur automatischen Übersetzung der README-Dokumentation
└── LICENSE                # Apache-Lizenzdatei
└── README.md              # Projektbeschreibung
└── config.json            # Konfigurationsdatei, die die Projektparameter definiert
└── requirements.txt       # Liste der Python-Abhängigkeiten
└── tool.py                # Automatisierungstool
```

## ⚙️ Dateibeschreibung

### `.github/workflows/generate.yml`
Dieser Workflow generiert automatisch die Projekt-README-Datei über GitHub Actions. Nach manuellem Auslösen führt er die folgenden Schritte aus:
1. Projektdaten auschecken;
2. Python 3.8-Umgebung einrichten;
3. Notwendige Abhängigkeiten installieren (`requests`, `openai`, `GitPython`);
4. Skript `tool.py generate` ausführen, um die README-Datei zu erstellen.

### `.github/workflows/optimize.yml`
Dieser Workflow dient der automatischen Optimierung der README-Datei. Nach manuellem Auslösen werden hauptsächlich die folgenden Schritte durchgeführt:
1. Code auschecken;
2. Python 3.8-Umgebung einrichten;
3. Notwendige Abhängigkeiten installieren;
4. `tool.py optimize` ausführen, um über die OpenAI-API eine Optimierung durchzuführen.

### `.github/workflows/translate.yml`
Dieser Workflow dient der automatischen Übersetzung der Projekt-README-Datei, ebenfalls manuell ausgelöst. Die Schritte beinhalten:
1. Code auschecken;
2. Python 3.8-Umgebung einrichten;
3. Abhängigkeiten installieren;
4. `tool.py translate` zur Übersetzung ausführen.

### `LICENSE`
Diese Datei enthält die Apache-Lizenz Version 2, die es Nutzern erlaubt, dieses Projekt unter Einhaltung der entsprechenden Bedingungen frei zu verwenden, zu modifizieren und zu verbreiten, um die Rechte der ursprünglichen Autoren und Mitwirkenden zu schützen.

### `config.json`
Diese Konfigurationsdatei definiert verschiedene Parameter, die für den Betrieb des Projekts erforderlich sind, einschließlich Repository-Informationen, Basis-URL der API, Modelle und unterstützte Übersetzungssprachen.

### `requirements.txt`
Listet die benötigten Python-Pakete für das Projekt auf, einschließlich:
- `requests`: Zum Verarbeiten von HTTP-Anfragen und zur Vereinfachung der Netzwerkinteraktionen.
- `openai`: Zur Interaktion mit der OpenAI-API und zum Aufrufen von KI-Modellen.
- `GitPython`: Bietet Unterstützung für Operationen an Git-Repositories.

### `tool.py`
Das Kernskript zur Automatisierung der README-Bearbeitung, mit den Hauptfunktionen:
1. Konfiguration laden;
2. Repository-Inhalte abrufen;
3. README-Inhalte generieren;
4. README vervollständigen und übersetzen;
5. Änderungen einreichen;
6. Befehlszeileninterface bereitstellen.

## 🌸 Wie benutzt man es?

Du kannst entweder dieses Projekt forken und `GitHub Actions` verwenden oder es lokal klonen, um es zu nutzen. Im Folgenden wird das Forken als Beispiel genommen, während das Klonen selbst konfiguriert werden muss.

1. Füge zunächst `PAT` und `OPENAI_API_KEY` zu den Geheimnissen (Secrets) hinzu.
2. Konfiguriere anschließend die entsprechenden Parameter in `config.json`.
3. Um die README zu generieren, löse den `generate`-Workflow manuell aus.
4. Um die README zu optimieren, löse den `optimize`-Workflow manuell aus.
5. Um die README zu übersetzen, löse den `translate`-Workflow manuell aus.

## 🌟 Lass uns anfangen!

Zögere nicht länger! Nutze dieses Tool, um die Qualität deiner Projektdokumentation zu verbessern, und ziehe mehr Zusammenarbeit und Aufmerksamkeit an! Wenn du denkst, dass dieses Projekt dir geholfen hat, gib uns einen 💖 Star! Lass uns gemeinsam an einer besseren Open-Source-Community arbeiten! 🌈

## 📄 Lizenz

Dieses Projekt steht unter der Apache-Lizenz. Weitere Informationen findest du in der [LICENSE](LICENSE)-Datei.

Willkommen, lass uns README einfacher und effizienter gestalten! 🚀