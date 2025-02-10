<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automatisches README Generierungs- und Übersetzungstool

Willkommen beim **README Automatisierungs-Generierungs- und Übersetzungstool** Projekt! 🎉 Dieses Projekt zielt darauf ab, Entwicklern und Projektbetreuern eine bequeme Möglichkeit zu bieten, README-Dateien einfach zu generieren, zu optimieren und zu übersetzen. Egal, ob du ein Anfänger oder ein Experte bist, mit nur wenigen einfachen Schritten kannst du ein professionelles und ansprechendes README-Dokument erhalten! 🚀

## 📂 Projektstruktur

```plaintext
./
└── workflows/
│   ├── generate.yml      # Workflow zur automatischen Generierung der README-Datei
│   ├── optimize.yml      # Workflow zur automatischen Optimierung der README-Datei
│   └── translate.yml      # Workflow zur automatischen Übersetzung der README-Datei
└── LICENSE                # Apache Lizenzdatei
└── README.md              # README-Datei des Projekts
└── config.json            # Konfigurationsdatei zur Definition der Projektparameter
└── requirements.txt       # Liste der Python-Abhängigkeiten
└── tool.py                # Automatisierungstool
```

## ⚙️ Dateiübersicht

### `.github/workflows/generate.yml`
Dieser Workflow generiert die README-Datei des Projekts automatisch über GitHub Actions. Nach manueller Auslösung führt er folgende Schritte aus:
1. Checkout des Projektcodes;
2. Einrichten der Python 3.8 Umgebung;
3. Installieren der benötigten Abhängigkeiten (`requests`, `openai`, `GitPython`);
4. Ausführen des `tool.py generate` Skripts zur Erstellung der README-Datei.

### `.github/workflows/optimize.yml`
Dieser Workflow optimiert automatisch die README-Datei. Nach manueller Auslösung werden die folgenden Schritte hauptsächlich durchgeführt:
1. Checkout des Codes;
2. Einrichten der Python 3.8 Umgebung;
3. Installieren der notwendigen Abhängigkeiten;
4. Ausführen von `tool.py optimize`, um über die OpenAI API Optimierungen vorzunehmen.

### `.github/workflows/translate.yml`
Dieser Workflow übersetzt automatisch die README-Datei des Projekts, ebenfalls durch manuelle Auslösung. Die Schritte umfassen:
1. Checkout des Codes;
2. Einrichten der Python 3.8 Umgebung;
3. Installieren der Abhängigkeiten;
4. Ausführen von `tool.py translate` zur Übersetzung.

### `LICENSE`
Diese Datei enthält die Apache Lizenz Version 2, die es Benutzern erlaubt, das Projekt unter Einhaltung der entsprechenden Bedingungen frei zu nutzen, zu modifizieren und zu verteilen, um die Rechte des ursprünglichen Autors und der Mitwirkenden zu schützen.

### `config.json`
Diese Konfigurationsdatei definiert verschiedene Parameter, die für den Betrieb des Projekts benötigt werden, einschließlich der Repository-Informationen, der Basis-API-URLs, des Modells und der unterstützten Übersetzungssprachen.

### `requirements.txt`
Listet die benötigten Python-Pakete für das Projekt auf, einschließlich:
- `requests`: Zur Verarbeitung von HTTP-Anfragen und Vereinfachung der Netzwerkinteraktionen.
- `openai`: Zur Interaktion mit der OpenAI API und zum Abrufen von KI-Modellen.
- `GitPython`: Bietet Unterstützung für Operationen mit Git-Repositories.

### `tool.py`
Das Kernskript zur Automatisierung der README-Verarbeitung hat folgende Hauptfunktionen:
1. Laden der Konfiguration;
2. Abrufen des Repository-Inhalts;
3. Generieren des README-Inhalts;
4. Vervollständigen und Übersetzen des README;
5. Übermitteln der Änderungen;
6. Bereitstellen einer Befehlszeilenschnittstelle.

## 🌸 So benutzt du es?

Du kannst dieses Projekt forked und mit `GitHub Actions` verwenden oder es lokal klonen, um es zu nutzen. Im Folgenden wird ersteres als Beispiel verwendet; für letzteres konfiguriere es bitte selbst.

1. Zuerst füge `PAT` und `OPENAI_API_KEY` zu den Secrets hinzu.
2. Gehe dann in die `config.json` und konfiguriere die entsprechenden Parameter.
3. Um die README zu generieren, löse den `generate` Workflow manuell aus.
4. Um die README zu optimieren, löse den `optimize` Workflow manuell aus.
5. Um die README zu übersetzen, löse den `translate` Workflow manuell aus.

## 🌟 Lass uns anfangen!

Zögere nicht länger! Nutze dieses Tool, um die Qualität deiner Projekt-Dokumentation zu verbessern und mehr Zusammenarbeit und Aufmerksamkeit zu gewinnen! Wenn du denkst, dass dieses Projekt dir geholfen hat, gib uns einen 💖 Star! Lass uns gemeinsam daran arbeiten, die Open-Source-Community schöner zu gestalten! 🌈

## 📄 Lizenz

Dieses Projekt verwendet die Apache Lizenz. Detaillierte Informationen findest du in der [LICENSE](LICENSE) Datei.

Willkommen in unserem Team, lass uns README einfacher und effizienter gestalten! 🚀