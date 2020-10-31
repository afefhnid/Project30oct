from flask import Flask, render_template, request
from tools import model
from tools import nettoyage
from tools import entrainement
import json
import numpy as np


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/prediction", methods=['POST'])
def prediction():

    user_text1 = request.form.get('input_text2')
    user_text2 = request.form.get('input_text3')
    user_text3 = request.form.get('input_text4')
    user_text4 = request.form.get('input_text5')
    user_text5 = request.form.get('input_text6')
    user_text6 = request.form.get('input_text7')
    user_text7 = request.form.get('input_text8')
    user_text8 = request.form.get('input_text9')
    user_text9 = request.form.get('input_text10')
    user_text10 = request.form.get('input_text11')
    user_text11 = request.form.get('input_text12')
    user_text12 = request.form.get('input_text13')
    user_text13 = request.form.get('input_text14')
    user_text14 = request.form.get('input_text15')

    # user_text = [user_text1, user_text2, user_text3, user_text4, user_text5, user_text6, user_text7,
    # user_text8, user_text9, user_text10, user_text11, user_text13, user_text13, user_text14]
    user_text = np.array([1, 22, 222, 22, 44, 88, 564,
                          454, 8876, 16353, 66484, 66484, 987, 7764]).reshape(1, -1)
    prediction = model(user_text)
   # return json.dumps({'text_user': prediction})
    return render_template("reponse.html", input_text=user_text, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
