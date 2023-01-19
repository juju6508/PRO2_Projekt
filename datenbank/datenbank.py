# In dieser Python-Datei werden alle Daten gespeichert, deshalb wird zuerst JSON importiert.
import json

# Plotly importieren, um das Diagramm zu erstellen.
import plotly.express as px
from plotly.offline import plot


# Funktion, damit die Datenbank mit den Daten der Destinationen geladen wird.
def laden_destinationen():
    try:
        # destinationen.json wird als read geöffnet und geladen
        with open("daten/destinationen.json", "r", encoding="utf-8") as datenbank_destinationen:
            eingaben_destinationen = json.load(datenbank_destinationen)
    except:
        eingaben_destinationen = {}
    return eingaben_destinationen


# Funktion, um eine neue Eingabe zu speichern
def destination_speichern(ortschaft, region, land, activities):
    destinationen = laden_destinationen()
    # Neue Destination wird in Dictionary geschrieben
    neue_destination = {
        "ortschaft": ortschaft,
        "region": region,
        "land": land,
        "activities": activities
    }
    # Neue Destination wird mit append den bereits bestehenden Destinationen hinzugefügt
    destinationen.append(neue_destination)
    # Neue Destination wird in destinationen.json gespeichert
    with open("daten/destinationen.json", "w", encoding="utf-8") as datenbank_destinationen:
        json.dump(destinationen, datenbank_destinationen, indent=4)


# Funktion, um die Destinationen der "Neue Eingabe"-Seite zu filtern
def anzeigen_sorted(filter):
    anzeigen = laden_destinationen()
    anzeigen_filtered = []
    for anzeige in anzeigen:
        # Filtermöglichkeit wird eingesetzt
        suche = (
            filter["land"] == "" or anzeige["land"] == filter["land"],
            filter["activities"] == "" or anzeige["activities"] == filter["activities"]
        )
        # Filter wird ausgeführt
        if all(suche):
            anzeigen_filtered.append(anzeige)
    return anzeigen_filtered


# Funktion, um das Diagramm der "Übersicht"-Seite anzuzeigen
def daten_definieren(y_achse):
    anzeigen = laden_destinationen()  # Damit die Länder und Aktivitäten direkt aus der Datenbank geladen werden.

    # Definierung der Länder
    laender = {}
    for anzeige in anzeigen:
        if anzeige["land"] not in laender:
            laender[anzeige["land"]] = 1
        else:
            laender[anzeige["land"]] += 1

    # Definierung der Aktivitäten
    activities = {}
    for anzeige in anzeigen:
        if anzeige["activities"] not in activities:
            activities[anzeige["activities"]] = 1
        else:
            activities[anzeige["activities"]] += 1

    if y_achse == "land":
        y = laender.keys()  # Aufgeführte Länder / y = keys
        x = laender.values()  # Anzahl Länder / x = values
    else:
        y = activities.keys()  # Aufgeführte Aktivitäten / y = keys
        x = activities.values()  # Anzahl Aktivitäten / x = values

    #  Gestaltung des Diagramms
    fig = px.bar(x=x, y=y, color_discrete_sequence=['#c2c2c2'])

    # Benennung der Achsen
    fig.update_layout(
        xaxis_title="Anzahl Länder",
        yaxis_title="Länder oder Aktivitäten",
    )

    # Ausgabe des Diagramms
    div = plot(fig, output_type="div")

    # Übergabe des Diagramms
    return div
