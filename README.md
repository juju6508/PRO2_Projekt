# Verwaltung von Feriendestinationen
## Ausgangslage/Problemstellung
Es gibt viele schöne Feriendestinationen in Europa. Doch welche sind für Camper/innen geeignet? Diese Seite soll spezifisch für Camper/innen eine Lösung bieten, um sich einen besseren Überblick über mögliche Länder und Orte in Europa zu verschaffen.
Besonders wenn man viel mit dem Camper unterwegs ist, hat man irgendwann keine Ideen mehr wohin man als nächstes fahren soll. Dieses Tool soll helfen, den interessierten Personen aufzuzeigen, welche Ortschaften gut mit einem Camper erreichbar sind. 

## Funktion/Projektidee
Das Projekt beinhaltet viele Möglichkeiten. Eine Übersicht von relevanten Informationen:

- Auflistung vieler Länder in Europa mit Top-Spots in den jeweiligen Ländern der Ortschaften
- Möglichkeit zur Erfassung von neuen Spots nach Angabe des Landes
- Möglichkeit zum Ausschluss von Regionen, die man bereits mit dem Camper besichtigt hat
- Möglichkeit zum Ausschluss von Aktivitäten

*Wie die Codes aufgebaut sind und welche Funktionen verwendet werden, sind als Kommentare in main.py und html file erfasst.*

## Ablauf des Programms
![img_1.png](img_1.png)

## Workflow
Folgende Module werden importiert, damit die Web-Applikation korrekt funktioniert:
- Flask
- Plotly
- Pandas 

### 1. Dateneingabe
Die Dateneingabe kann durch mehrere Wege erfolgen. Auf der Startseite des Programms kann man:
- die gewünschten Feriendestinationen auswählen
- neue Feriendestinationen erfassen
- sich registrieren oder einloggen mit Username und Passwort

### 2. Datenverarbeitung/Speicherung
Die Feriendestinationen sowie die Userdaten werden in einer JSON-Datei gespeichert. 

### 3. Datenausgabe
- Ausgabe der Vorschläge für Feriendestinationen
- Ausgabe der gespeicherten Feriendestinationen
- Darstellungen in einem Balkendiagramm

## Mögliche zukünftige Erweiterungen des Programms
Damit das Tool noch mehr Nutzen erhält, könnte man folgende Erweiterungen vornehmen:
- Ausweitung der Länder oder sogar Kontinente (z.B. Amerika mit den Bundesstaaten hinzufügen)
- Noch mehr Kriterien als Ausschluss zur Verfügung
- Vorschläge von ähnlichen Destinationen mit den gleichen Kriterien
- Destinationen favorisieren (z.B. für zukünftige Reisen usw.)