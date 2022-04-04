import sys
from typing import Dict

import joblib
import pandas as pd

sys.path.append("..")
from schema import PredictStrokeResponseSchema
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def preprocess(X: pd.DataFrame, scaler: StandardScaler, ohe: OneHotEncoder):
    X_cont = X.iloc[:, [1, 4, 5]]
    X_cat = X.iloc[:, [0, 2, 3, 6]]
    X_cont = pd.DataFrame(scaler.transform(X_cont))
    X_cat = pd.DataFrame(ohe.transform(X_cat).todense())
    X = pd.concat([X_cont.reset_index(drop=True), X_cat.reset_index(drop=True)], axis=1)
    return X


def predict(request_args: Dict[str, str]) -> PredictStrokeResponseSchema:
    """
    Predict the outcome of stroke

    Args:
        request_args: The arguments passed into the HTTP request

    Returns:
        PredictStrokeResponseSchema: The HTTP response
    """
    # Read the required URL params from request_args
    gender = request_args.get("gender")
    age = float(request_args.get("age"))
    hypertension = request_args.get("hypertension")
    corornary_artery_disease = request_args.get("corornary_artery_disease")
    glucose_level = float(request_args.get("glucose_level"))
    bmi = float(request_args.get("bmi"))
    smoking_status = request_args.get("smoking_status")

    # load the model, scaler, one-hot-encoder
    model = joblib.load("models/weights/stroke/stroke_nn.gz")
    scaler = joblib.load("models/weights/stroke/stroke_scaler.bin")
    ohe = joblib.load("models/weights/stroke/stroke_onehot.joblib")
    values = pd.DataFrame(
        [
            [
                gender,
                age,
                hypertension,
                corornary_artery_disease,
                glucose_level,
                bmi,
                smoking_status,
            ]
        ]
    )

    # Perform preprocessing of the given user input
    X = preprocess(values, scaler, ohe)

    # Predict and return
    pred = model.predict(X)
    res: PredictStrokeResponseSchema = {
        "outcome": str(pred[0]),
    }
    return res
