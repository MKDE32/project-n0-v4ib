
from flask import Flask, render_template
import os


app = Flask(__name__)


PYTHON_ORDNER = "python"



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/python")
def python():
    dateien = os.listdir(PYTHON_ORDNER)
    return render_template("python.html", dateien=dateien)



@app.route("/python/<dateiname>")
def python_anzeigen(dateiname):
    pfad = os.path.join(PYTHON_ORDNER, dateiname)

    with open(pfad, "r", encoding="utf-8") as f:
        inhalt = f.read()

    return f"<pre>{inhalt}</pre>"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
