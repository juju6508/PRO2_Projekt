# Auflistung aller Flask-Module
from flask import Flask
from flask import render_template
from flask import request

# Alle Daten aus dem Datenbank-Ordner importieren
from datenbank.datenbank import *

app = Flask("Verwaltung von Feriendestinationen")


# Die Startseite
@app.route('/', methods=['POST', 'GET'])
def startseite():
    return render_template('startseite.html', app_name="Where to next? - Home")


# Die "Auswahl"-Seite
@app.route('/auswahl', methods=['POST', 'GET'])
def auswahl():
    # Datenbank laden, damit mit "anzeigen" die Filter-Option geladen werden kann.
    anzeigen = laden_destinationen()
    # Mit Register wird eine neue Auflistung der Länder gemacht.
    register_land = [ergebnis['land'] for ergebnis in anzeigen]
    register_land = set(register_land)  # erzeugt keine Doppelnennungen der Länder
    register_land = sorted(register_land)  # Sortierung der Länder nach dem Alphabet

    # Mit Register wird eine neue Auflistung der Aktivitäten gemacht.
    register_activities = [ergebnis['activities'] for ergebnis in anzeigen]
    register_activities = set(register_activities)  # erzeugt keine Doppelnennungen der Aktivitäten
    register_activities = sorted(register_activities)  # Sortierung der Aktivitäten nach dem Alphabet

    # Definierte Auswahlmöglichkeiten
    land = register_land
    activities = register_activities

    # Die sortierten/ausgefilterten Destinationen werden angezeigt.
    if request.method == "POST":
        anzeigen = anzeigen_sorted(request.form)
    return render_template("auswahl.html", app_name="Where to next? - Auswahl", laender=land, activities=activities,
                           anzeigen=anzeigen)


# Die "Neue Eingabe"-Seite
@app.route('/erfassung', methods=['POST', 'GET'])
def erfassung():
    # Informationen zur Destination werden abgefragt und abgefangen.
    if request.method == "POST":
        ortschaft = request.form['input_ortschaft']
        region = request.form['input_region']
        land = request.form['input_land']
        activities = request.form['input_activities']
        # Getätigte Angaben werden gespeichert.
        destination_speichern(ortschaft, region, land, activities)
        # Sobald die Destination erfolgreich gespeichert wurde, werden dem Nutzer die eingegebenen Daten angezeigt.
        success = f"Deine Destination wurde gespeichert: Ortschaft: {ortschaft}, Region: {region}, Land: {land}, Aktivitäten: {activities} "
        return render_template('erfassung.html', success=success, app_name="Where to next? - Neue Eingabe")
    return render_template('erfassung.html', app_name="Where to next? - Neue Eingabe")


# Die "Übersicht"-Seite
@app.route("/uebersicht", methods=["POST", "GET"])
def daten_auswerten():
    # Wenn die Seite aufgerufen wird, erscheint die "Übersicht"-Seite im normalen Design.
    if request.method == "GET":
        return render_template("uebersicht.html", app_name="Where to next? - Übersicht")

    # Weiterer Code wird für die Darstellung und Funktion der x-Achse und y-Achse gebraucht.
    if request.method == "POST":
        y_achse = request.form.to_dict()["y-Achse"]
        div = daten_definieren(y_achse)  # Weiterleitung zur Datenbank
        return render_template("uebersicht.html", grafik=div, app_name="Where to next? - Übersicht")


if __name__ == "__main__":
    app.run(debug=True, port=5100)
