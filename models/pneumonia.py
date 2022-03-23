import sys

sys.path.append("..") 
from schema import PredictPneumoniaResponseSchema

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING 
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""
def predict(absolute_image_path: str) -> PredictPneumoniaResponseSchema:
    # casting
    # load model
    # model.predict
    # return results
    print(f"absolute_image_path: {absolute_image_path}")

    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictCataractResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictCataractResponseSchema
    res: PredictPneumoniaResponseSchema = {
        "probability": 0.5,
        "outcome": 1
    }
    return res
