import sys
from typing import Dict

import joblib
import pandas as pd

sys.path.append("..")
from schema import PredictDiabetesResponseSchema
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def preprocess(X: pd.DataFrame, scaler: StandardScaler, ohe: OneHotEncoder):
    X_cont = X.iloc[:, [2, 10, 12, 13]]
    X_cat = X.iloc[:, [0, 1, 3, 4, 5, 6, 7, 8, 9, 11]]
    X_cont = pd.DataFrame(scaler.transform(X_cont))
    X_cat = pd.DataFrame(ohe.transform(X_cat).todense())
    X = pd.concat([X_cont.reset_index(drop=True), X_cat.reset_index(drop=True)], axis=1)
    return X


def predict(request_args: Dict[str, str]) -> PredictDiabetesResponseSchema:
    """
    Predict the outcome of diabetes

    Args:
        request_args: The arguments passed into the HTTP request

    Returns:
        PredictDiabetesResponseSchema: The HTTP response
    """
    # Read the required URL params from request_args
    hypertension = str(request_args.get("hypertension"))
    high_cholesterol = str(request_args.get("high_cholesterol"))
    smoker = str(request_args.get("smoker"))
    stroke = str(request_args.get("stroke"))
    coronary_artery_disease = str(request_args.get("coronary_artery_disease"))
    active_lifestyle = str(request_args.get("active_lifestyle"))
    fruits_consumption = str(request_args.get("fruits_consumption"))
    vegetable_consumption = str(request_args.get("vegetable_consumption"))
    alcohol_consumption = str(request_args.get("alcohol_consumption"))
    sex = str(request_args.get("sex"))
    age = str(request_args.get("age"))
    income = str(request_args.get("income"))
    bmi = float(request_args.get("bmi"))
    general_health = float(request_args.get("general_health"))

    # load the model, scaler, one-hot-encoder
    model = joblib.load("models/weights/diabetes/diabetes_nn.gz")
    scaler = joblib.load("models/weights/diabetes/diabetes_scaler.bin")
    ohe = joblib.load("models/weights/diabetes/diabetes_onehot.joblib")
    values = pd.DataFrame(
        [
            [
                hypertension,
                high_cholesterol,
                bmi,
                smoker,
                stroke,
                coronary_artery_disease,
                active_lifestyle,
                fruits_consumption,
                vegetable_consumption,
                alcohol_consumption,
                general_health,
                sex,
                age,
                income,
            ]
        ]
    )

    # Perform preprocessing of the given user input
    X = preprocess(values, scaler, ohe)

    # Predict and return
    pred = model.predict(X)
    res: PredictDiabetesResponseSchema = {
        "outcome": str(pred[0]),
    }
    return res
