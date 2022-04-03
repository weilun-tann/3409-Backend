import sys
import cv2
import numpy as np
import keras
from keras.models import model_from_json

sys.path.append("..")
from schema import PredictCataractResponseSchema

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING 
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""
def predict(absolute_image_path: str) -> PredictCataractResponseSchema:
    """_summary_

    Args:
        absolute_image_path (str): _description_

    Returns:
        PredictCataractResponseSchema: _description_
    """
    # casting
    # load model
    # model.predict
    # return results

    #loading the model and weights
    model = model_from_json(open('o_model.json').read())
    model.load_weights('model_o_weights.h5')

    #process input image
    image = cv2.imread(absolute_image_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image,(200,200))
    image = np.array(image).reshape(-1, 200,200,3)

    #predict results
    pred = model.predict(image)
    if pred > 0.5:
        outcome = "Cataract"
    else:
        outcome = "Normal"


    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictCataractResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictCataractResponseSchema
    res: PredictCataractResponseSchema = {
        "cataract_type": outcome,
    }
    return res
