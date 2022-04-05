from schema import PredictPneumoniaResponseSchema
import sys
from keras.models import model_from_json
import matplotlib.pyplot as plt
import cv2
import numpy as np
from keras.preprocessing import image

sys.path.append("..")

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING 
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""


def predict(absolute_image_path: str) -> PredictPneumoniaResponseSchema:
    """_summary_

    Args:
        absolute_image_path (str): _description_

    Returns:
        PredictPneumoniaResponseSchema: _description_
    """
    # casting
    # load model
    model = model_from_json(
        open("models/weights/pneumonia/pneumonia.json").read())
    model.load_weights("models/weights/pneumonia/pneumonia.h5")

    # model.predict
    img_dims = 64
    img = absolute_image_path
    img = cv2.resize(img, (img_dims, img_dims))
    img = np.dstack([img, img, img])
    img = img.astype('float32') / 255
    result = model.predict(np.expand_dims(image.img_to_array(img), axis=0))

    if result[0][0] > 0.5:
        prediction = 'Present'
    else:
        prediction = 'Absent'

    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictPneumoniaResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictPneumoniaResponseSchema
    res: PredictPneumoniaResponseSchema = {
        "outcome": prediction
    }
    return res
