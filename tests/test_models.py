import pytest
from models import coronary, diabetes, pneumonia, stroke


def test_predict_coronary():
    # TODO - 1 test for TRUE
    assert coronary.predict(
        {
            "age": "75",
            "gender": "Male",
            "chest_pain_type": "Typical Angina",
            "resting_blood_pressure": "180",
            "cholesterol": "400",
            "fasting_blood_sugar": "More than 120 mg/dl",
            "resting_ecg": "LVH",
            "max_hr": "60",
            "exercise_induced_angina": "Y",
        }
    ) == {"outcome": "Present"}

    # TODO - 1 test for FALSE
    assert coronary.predict(
        {
            "age": "25",
            "gender": "Female",
            "chest_pain_type": "Asymptomatic",
            "resting_blood_pressure": "125",
            "cholesterol": "150",
            "fasting_blood_sugar": "Less than or equal to 120 mg/dl",
            "resting_ecg": "Normal",
            "max_hr": "180",
            "exercise_induced_angina": "N",
        }
    ) == {"outcome": "Absent"}


def test_predict_diabetes():
    # TODO - 1 test for TRUE
    assert diabetes.predict(
        {
            "hypertension": "Present",
            "high_cholesterol": "High",
            "smoker": "Previously/Existing",
            "stroke": "Previously",
            "coronary_artery_disease": "Present",
            "active_lifestyle": "Normal",
            "fruits_consumption": "Infrequent",
            "vegetable_consumption": "Infrequent",
            "alcohol_consumption": "Frequent",
            "general_health": "0",
            "sex": "Male",
            "age": "75",
            "income": "30000",
            "bmi": "40",
        }
    ) == {"outcome": "Present"}

    # TODO - 1 test for FALSE
    assert diabetes.predict(
        {
            "hypertension": "Absent",
            "high_cholesterol": "Normal",
            "smoker": "Never",
            "stroke": "Previously",
            "coronary_artery_disease": "Present",
            "active_lifestyle": "Normal",
            "fruits_consumption": "Frequent",
            "vegetable_consumption": "Frequent",
            "alcohol_consumption": "Infrequent",
            "general_health": "5",
            "sex": "Male",
            "age": "25",
            "income": "60000",
            "bmi": "21.5",
        }
    ) == {"outcome": "Absent"}


def test_predict_stroke():
    # TODO - 1 test for TRUE
    assert stroke.predict(
        {
            "gender": "Male",
            "age": "75",
            "hypertension": "Present",
            "corornary_artery_disease": "Present",
            "glucose_level": "250",
            "bmi": "36",
            "smoking_status": "formerly smoked",
        }
    ) == {"outcome": "Present"}

    # TODO - 1 test for FALSE
    assert stroke.predict(
        {
            "gender": "Female",
            "age": "25",
            "hypertension": "Absent",
            "corornary_artery_disease": "Absent",
            "glucose_level": "130",
            "bmi": "21",
            "smoking_status": "never smoked",
        }
    ) == {"outcome": "Absent"}


def test_predict_pneumonia():
    """
    TODO - change your `actual` and `expected` accordingly
    """
    actual = pneumonia.predict("uploads/sample.png")
    expected = {"probability": 0.5, "outcome": 1}
    assert actual == expected
