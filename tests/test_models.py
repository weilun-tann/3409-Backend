import pytest
from models import cataract, pneumonia


def test_predict_cataract():
    """
    TODO - change your `actual` and `expected` accordingly
    """
    actual = cataract.predict("20", "Male")
    expected = {
        "cataract_type": "nuclear",
    }
    assert actual == expected


def test_predict_pneumonia():
    """
    TODO - change your `actual` and `expected` accordingly
    """
    actual = pneumonia.predict("uploads/sample.png")
    expected = {"probability": 0.5, "outcome": 1}
    assert actual == expected
