[Back to main language README](README.md)

# README - README-Automatic-Generation-and-Translation-Tool 🚀

## Projektübersicht 📜
Dieses Projekt heißt **README-Automatic-Generation-and-Translation-Tool** und wurde von **Delta-Water** entwickelt. Es zielt darauf ab, die automatische Generierung und Übersetzung von README-Dateien in den angegebenen GitHub-Repositories zu erleichtern. Durch die Nutzung der GitHub API und der Dienste von OpenAI kann dieses Tool effizient Inhalte extrahieren, README-Texte generieren und sie in mehrere Sprachen übersetzen, sodass Benutzer weltweit sie leicht verstehen und nutzen können.

## Lizenz 📄
Dieses Projekt folgt der Apache-Lizenz, Version 2.0. Diese Lizenz beschreibt die Bedingungen für die Nutzung, Vervielfältigung und Verbreitung von Software und anderen Werken und definiert mehrere wichtige Begriffe wie „Lizenzgeber“, „Sie“, „Werk“, „abgeleitete Werke“ und „Beiträge“. Sie erhalten ein dauerhaftes, weltweites, nicht exklusives und lizenzfreies Recht zur Nutzung dieses Projekts und seiner abgeleiteten Werke. Weitere Informationen zur Lizenz finden Sie in der `LICENSE`-Datei.

## Umgebung einrichten ⚙️

Bevor Sie dieses Tool verwenden, müssen Sie sicherstellen, dass die erforderlichen Abhängigkeiten installiert sind. Dieses Projekt hängt von den folgenden Bibliotheken ab:

1. **requests** - Eine beliebte Bibliothek für einfache HTTP-Anfragen.
2. **openai** - Eine Bibliothek für den Zugriff auf die Dienste und Modelle von OpenAI, die fortschrittliche künstliche Intelligenz-Fähigkeiten integriert.
3. **GitPython** - Eine Bibliothek für die programmgesteuerte Interaktion mit Git-Repositories, die die Versionskontrolle erleichtert.

Sie können diese Abhängigkeiten installieren, indem Sie den folgenden Befehl ausführen:

```bash
pip install -r requirements.txt
```

## Verwendung 📚

1. **Konfiguration laden**: Das Tool lädt die Konfigurationseinstellungen aus der Datei `config.json`. Sie müssen diese Datei an Ihre tatsächlichen Gegebenheiten anpassen. Grundlegende Informationen umfassen die Basis-URL der API und den Hauptsprachindex.

2. **Interaktion mit GitHub**: Das Tool verwendet die GitHub API, um Inhalte aus dem angegebenen Repository abzurufen.

3. **Integration mit OpenAI**: Mit der OpenAI API wird der Inhalt der Datei zusammengefasst, README-Texte generiert und in mehreren Sprachen übersetzt.

4. **Übersetzungsmanagement**: Dieses Tool unterstützt die Übersetzung der generierten README-Dokumente in mehrere Sprachen und formatiert die Übersetzungsergebnisse.

5. **README-Update**: Das Tool erstellt die Haupt-README und fügt Links zu den Übersetzungsvarianten hinzu, bevor es die Änderungen in das ursprüngliche Repository zurücküberträgt.

6. **Fehlerbehandlung**: Es enthält Fehlerbehandlungsroutinen, die während verschiedener Betriebsphasen Nachrichten ausgeben, um Probleme frühzeitig zu erkennen.

## Beitragsrichtlinien 💡

Wir freuen uns über Ihren Beitrag zu diesem Projekt! Wenn Sie Ideen oder Vorschläge haben, beteiligen Sie sich bitte nach den folgenden Schritten:

1. Forken Sie dieses Repository
2. Nehmen Sie Änderungen in Ihrem Branch vor
3. Reichen Sie einen Pull Request ein

Bitte stellen Sie sicher, dass Sie die Code-Richtlinien und Beitragsprozesse des Projekts einhalten. Ihre Beiträge werden sorgfältig überprüft und helfen uns, die Funktionalität und Benutzerfreundlichkeit dieses Tools zu verbessern.

## Kontakt 📫

Bei Fragen oder Anregungen wenden Sie sich bitte über GitHub Issues oder direkt an den Autor **Delta-Water**.

Vielen Dank, dass Sie sich für **README-Automatic-Generation-and-Translation-Tool** entschieden haben! Wir freuen uns auf Ihr Feedback und Ihre Beiträge! 🌟