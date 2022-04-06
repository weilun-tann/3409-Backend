import sys
from typing import Dict

import joblib
import pandas as pd

sys.path.append("..")
from schema import PredictCoronaryResponseSchema
from sklearn.preprocessing import OneHotEncoder


def preprocess(X: pd.DataFrame, ohe: OneHotEncoder):
    X_cont = X.iloc[:, [0, 3, 4, 7]]
    X_cat = X.iloc[:, [1, 2, 5, 6, 8]]
    X_cat = pd.DataFrame(ohe.transform(X_cat).todense())
    X = pd.concat([X_cont.reset_index(drop=True), X_cat.reset_index(drop=True)], axis=1)
    return X


def predict(request_args: Dict[str, str]) -> PredictCoronaryResponseSchema:
    """
    Predict the outcome of coronary

    Args:
        request_args: The arguments passed into the HTTP request

    Returns:
        PredictCoronaryResponseSchema: The HTTP response
    """
    # Read the required URL params from request_args
    # TODO - FLOAT CASTING
    age = float(request_args.get("age"))
    gender = request_args.get("gender")
    chest_pain_type = request_args.get("chest_pain_type")
    resting_blood_pressure = float(request_args.get("resting_blood_pressure"))
    cholesterol = float(request_args.get("cholesterol"))
    fasting_blood_sugar = request_args.get("fasting_blood_sugar")
    resting_ecg = request_args.get("resting_ecg")
    max_hr = float(request_args.get("max_hr"))
    exercise_induced_angina = request_args.get("exercise_induced_angina")

    # load the model, scaler, one-hot-encoder
    model = joblib.load("models/weights/coronary/coronary_rf.gz")
    ohe = joblib.load("models/weights/coronary/coronary_onehot.joblib")
    values = pd.DataFrame(
        [
            [
                age,
                gender,
                chest_pain_type,
                resting_blood_pressure,
                cholesterol,
                fasting_blood_sugar,
                resting_ecg,
                max_hr,
                exercise_induced_angina,
            ]
        ]
    )

    # Perform preprocessing of the given user input
    X = preprocess(values, ohe)

    # Predict and return
    pred = model.predict(X)
    res: PredictCoronaryResponseSchema = {
        "outcome": "Absent" if str(pred[0]) == "0" else "Present",
    }
    return res
