from flask import Flask
from flask import render_template

app = Flask("Verwaltung der Feriendestinationen")


@app.route('/hello')
def hello_world():
    return render_template('index.html', name="Debora")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

app=Flask(__name__,template_folder='templates')