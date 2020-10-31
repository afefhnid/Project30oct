from flask import Flask, render_template, request
from tools import model
from tools import nettoyage
from tools import entrainement
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=['POST'])
def prediction():
    user_text = request.form.get('input_text')
    prediction = model(user_text)
    res = getPrediction(user_text)
    return json.dumps({'text_user': prediction})


if __name__ == "__main__":
    app.run(debug=True)
