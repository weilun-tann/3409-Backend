import sys
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

sys.path.append("../..")
from schema import PredictDiabetesResponseSchema

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""

def arrange_vals(X, scaler):
    X_cont = X.iloc[:,[2,10,12,13]]
    X_cat = X.iloc[:,[0,1,3,4,5,6,7,8,9,11]]
    X_cont = scaler.fit_transform(X_cont)
    ohe = OneHotEncoder().fit(X_cat)
    columns = X_cat.columns
    columns = ohe.get_feature_names_out(columns)
    X_cat = pd.DataFrame(ohe.transform(X_cat).todense(), columns=columns)
    X = pd.concat([X_cont.reset_index(drop=True),X_cat.reset_index(drop=True)], axis=1)
    print(X)
    return X

def predict(
    hypertension: str,
    high_cholesterol: str,
    bmi: str,
    smoker: str,
    stroke: str,
    coronary_artery_disease: str,
    active_lifestyle: str,
    fruits_consumption: str,
    vegetable_consumption: str,
    alcohol_consumption: str,
    general_health: str,
    sex: str,
    age: str,
    income: str,
) -> PredictDiabetesResponseSchema:

    """_summary_

    Args:
        age (str): _description_
        gender (str): _description_

    Returns:
        PredictCataractResponseSchema: _description_
    """
    # casting
    bmi = float(bmi)
    general_health = float(general_health)
    age = float(age)
    income = float(income)

    # load model
    model = joblib.load('diabetes_nn.gz')
    scaler = joblib.load('diabetes_scaler.bin')
    values = pd.DataFrame([[hypertension, high_cholesterol, bmi, smoker, stroke, coronary_artery_disease, active_lifestyle, fruits_consumption, vegetable_consumption, alcohol_consumption, general_health, sex, age, income]])
    X = arrange_vals(values, scaler)
    pred = model.predict(X)
    return {
       "outcome": pred[0],
    }

    # model.predict


    # return results

    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictCataractResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictCataractResponseSchema
    res: PredictDiabetesResponseSchema = {
        "outcome": "nuclear",
    }
    return res
