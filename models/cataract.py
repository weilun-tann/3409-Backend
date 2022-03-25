import sys

sys.path.append("..")
from schema import PredictCataractResponseSchema

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING 
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""


def predict(age: str, gender: str) -> PredictCataractResponseSchema:
    """_summary_

    Args:
        age (str): _description_
        gender (str): _description_

    Returns:
        PredictCataractResponseSchema: _description_
    """
    # casting
    # load model
    # model.predict
    # return results

    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictCataractResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictCataractResponseSchema
    res: PredictCataractResponseSchema = {
        "cataract_type": "nuclear",
    }
    return res
