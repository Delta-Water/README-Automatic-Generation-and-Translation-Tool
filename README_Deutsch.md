# Automatisches Generierungs- und Übersetzungstool

Willkommen beim **Automatischen Generierungs- und Übersetzungstool**! 🎉 Dieses innovative Tool wurde entwickelt, um die automatische Erstellung und Übersetzung von Texten für Softwareprojekte, die auf GitHub gehostet werden, zu erleichtern. Durch den Einsatz fortschrittlicher APIs und einer benutzerfreundlichen Konfiguration können Sie mühelos professionelle README-Dateien erstellen und in verschiedene Sprachen übersetzen. 🌍

## Inhaltsverzeichnis
- [Projekt-Einführung](#projekt-einführung)
- [Funktionen](#funktionen)
- [Installationsschritte](#installationsschritte)
- [Benutzungsanleitung](#benutzungsanleitung)
- [Konfiguration](#konfiguration)
- [Beitragsrichtlinien](#beitragsrichtlinien)
- [Lizenz](#lizenz)

## Projekt-Einführung

Das Automatische Generierungs- und Übersetzungstool optimiert den Prozess der Erstellung von ansprechenden und mehrsprachigen README-Dateien für Software-Repositories. Durch das Verstehen und Zusammenfassen des Inhalts Ihrer Projektdaten generiert es nicht nur eine ansprechende README, sondern übersetzt sie auch in mehrere Sprachen, um Ihr Projekt einer globalen Zielgruppe zugänglich zu machen. 🌐

## Funktionen

- **Konfigurationsmanagement**: Vereinfachen Sie Ihr Setup mit einer JSON-Konfigurationsdatei, die wesentliche Repository-Parameter definiert.
- **Dateiwiederbeschaffung**: Holen Sie Dateien automatisch von Ihrem GitHub-Repository über die GitHub-API.
- **Inhaltserstellung**: Generieren Sie eine professionelle README mit klaren Projektdetails, Installationsanweisungen, Benutzungsanleitungen und mehr, indem Sie die API von OpenAI nutzen. ✨
- **Übersetzungsunterstützung**: Übersetzen Sie den README-Inhalt in mehrere Sprachen, um ein unterschiedliches Publikum anzusprechen.
- **Benutzerfreundliche Updates**: Ändern Sie die Haupt-README ganz einfach und erstellen Sie separate übersetzte README-Dateien. 🔄

## Installationsschritte

Um mit dem Automatischen Generierungs- und Übersetzungstool zu beginnen, befolgen Sie diese Schritte:

1. **Repository klonen:**
   ```bash
   git clone https://github.com/benutzer/repo.git
   ```

2. **In das Projektverzeichnis wechseln:**
   ```bash
   cd repo
   ```

3. **Abhängigkeiten installieren:**
   Stellen Sie sicher, dass Python installiert ist. Installieren Sie dann die benötigten Pakete mit pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Das Tool konfigurieren:**
   Bearbeiten Sie die `config.json`, um Ihre GitHub-Repository-URL, Branch-Informationen und bevorzugte Übersetzungssprachen einzugeben. ⚙️

## Benutzungsanleitung

Um das Automatische Generierungs- und Übersetzungstool zu nutzen, führen Sie das Python-Skript wie folgt aus:

```bash
python tool.py
```

Dieser Befehl liest die Konfigurationsdatei, ruft die notwendigen Dateien vom angegebenen GitHub-Repository ab, generiert den README-Inhalt, übersetzt ihn und commitet die Änderungen zurück in das Repository. 📝

### Beispiel einer Konfiguration

Hier ist ein Beispiel dafür, wie Ihre `config.json` aussehen sollte:

```json
{
    "repo_url": "https://github.com/benutzer/repo",
    "branch": "main",
    "main_language_index": 0,
    "api_token": "DEIN_GITHUB_API_TOKEN",
    "target_languages": ["es", "fr", "de"]
}
```

Stellen Sie sicher, dass Sie `"DEIN_GITHUB_API_TOKEN"` durch Ihren tatsächlichen GitHub-API-Token ersetzen. 🔑

## Beitragsrichtlinien

Wir freuen uns über Beiträge zur Verbesserung der Funktionalität des Automatischen Generierungs- und Übersetzungstools! Hier sind einige Möglichkeiten, wie Sie beitragen können:

1. **Forken Sie das Repository**: Erstellen Sie Ihren eigenen Fork, um an Ihren Änderungen zu arbeiten.
2. **Reichen Sie einen Pull-Request ein**: Sobald Sie Ihre Änderungen vorgenommen und getestet haben, reichen Sie bitte einen Pull-Request zur Überprüfung ein.
3. **Berichten Sie über Probleme**: Wenn Sie auf Bugs stoßen oder Vorschläge haben, können Sie gerne ein Problem im Repository eröffnen. 🐞

## Lizenz

Dieses Projekt steht unter den Bedingungen der [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0). Diese permissive Lizenz erlaubt Ihnen die Nutzung, Vervielfältigung und Verbreitung der Software, während die Rechte der Mitwirkenden geschützt bleiben. 📜

---

Vielen Dank, dass Sie das Automatische Generierungs- und Übersetzungstool verwenden! Wir hoffen, es verbessert die Zugänglichkeit und das Engagement Ihres Projekts. Viel Spaß beim Coden! 👩‍💻👨‍💻

[Back to main language README](README.md)