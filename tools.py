import pickle
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def model(param):

    cls = pickle.load(open("cls_numCardLength_model.pkl", "rb"))
    if (cls.predict(param)[0]) == 1:
        isFraud = "Fraud"
    else:
        isFraud = "Secuire"

    return (isFraud, round(cls.predict_proba(param).max(), 3))
