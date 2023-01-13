# Alle Flask-Module
from flask import Flask
from flask import render_template
from flask import request

# Alle Daten aus dem Datenbank-Ordner importieren
from datenbank.datenbank import *

app = Flask("Verwaltung von Feriendestinationen")

# Die Startseite
@app.route('/', methods=['POST', 'GET'])
def startseite():
    return render_template('startseite.html')

# Die "Auswahl" Seite
@app.route('/auswahl', methods=['POST', 'GET'])
def auswahl():
    return render_template('auswahl.html')

# Die "Neue Eingabe" Seite
@app.route('/erfassung', methods=['POST', 'GET'])
def erfassung():
    # Informationen zur Destination werden abgefragt und abgefangen
    if request.method == "POST":
        ortschaft = request.form['input_ortschaft']
        region = request.form['input_region']
        land = request.form['input_land']
        activities = request.form['input_activities']
        # Angaben werden gespeichert
        destination_speichern(ortschaft, region, land, activities)
        # Sobald die Destination erfolgreich gespeichert wurde, werden dem Nutzer die eingegebenen Daten angezeigt
        success = f"Destination gespeichert: Ortschaft: {ortschaft}, Region: {region}, Land: {land}, Aktivitaeten: {activities}"
        return render_template('erfassung.html', success=success)
    return render_template('erfassung.html')

if __name__ == "__main__":
    app.run(debug=True, port=5100)
