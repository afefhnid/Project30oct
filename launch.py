from flask import Flask, render_template, request
from tools import model
import json
import numpy as np


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=['POST'])
def prediction():
    return render_template("prediction.html")


@app.route("/reponse", methods=['POST'])
def reponse():
    input_amt = request.form.get('input_amt')
    input_gender = request.form.get('input_gender')
    input_state = request.form.get('input_state')
    input_city_pop = request.form.get('input_city_pop')
    input_numCardLength = request.form.get('input_numCardLength')
    input_age = request.form.get('input_age')

    params = np.array([input_amt, input_gender, input_state,
                       input_city_pop, input_numCardLength, input_age]).reshape(1, -1)
    prediction = model(params)
   # return json.dumps({'text_user': prediction})
    return render_template("reponse.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
