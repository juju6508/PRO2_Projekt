# JSON importieren
import json

# Funktion zum Laden der Datenbank mit den Daten der Destinationen
def laden_destinationen():
    try:
        # destinationen.json wird als read geöffnet und geladen
        with open("daten/destinationen.json", "r") as datenbank_destinationen:
            eintraege_destinationen = json.load(datenbank_destinationen)
    except:
        eintraege_destinationen = {}
    return eintraege_destinationen

# Funktion, welche alle Daten der Destinationen aufruft
def alle_destinationen():
    destinationen = laden_datenbank()
    # neue Liste wird erstellt
    destination_liste = []
    # Destinationen werden der destination_liste angefügt
    for destination in destinationen.values():
        destination_liste.append(destination["destination"])

# Funktion, um eine neue Eingabe zu speichern
def destination_speichern(ortschaft, region, land, activities):
    destinationen = laden_destinationen()
    # Neue Destination wird in Dict geschrieben
    neue_destination = {
    "ortschaft": ortschaft,
    "region": region,
    "land": land,
    "activities": activities
}
    # Neue Destination wird mit append den bereits bestehenden Destinationen hinzugefügt
    destinationen.append(neue_destination)
    # Neue Destination wird in destinationen.json gedumped
    with open("daten/destinationen.json", "w") as datenbank_destinationen:
        json.dump(destinationen, datenbank_destinationen, indent=4)
