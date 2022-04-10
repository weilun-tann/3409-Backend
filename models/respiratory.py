import sys
import keras
from keras.models import model_from_json
import pickle
import numpy as np
import librosa

sys.path.append("..")
from schema import PredictRespiratoryResponseSchema

"""
TODO - ADD THE ARGUMENTS YOU NEED FOR YOUR MODEL, LEAVING TYPES AS STRING 
1. All arguments will be passed as string
2. The return value should be a dictionary, do NOT change the return type
3. Backend will simply send it back as JSON
"""


def predict(absolute_audio_path: str) -> PredictRespiratoryResponseSchema:
    """_summary_

    Args:
        absolute_audio_path (str): _description_

    Returns:
        PredictRespiratoryResponseSchema: _description_
    """
    # casting
    # load model
    # model.predict
    # return results

    # loading the model and weights
    model = model_from_json(open("models/weights/respiratory/r_model.json").read())
    model.load_weights("models/weights/respiratory/model_r_weights.h5")
    scaler = pickle.load(open("models/weights/respiratory/r_scaler.pkl", "rb"))
    model.compile(
        loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adam"
    )

    # process input audio
    features = []

    file_name = absolute_audio_path
    y, sr = librosa.load(file_name, mono=True)
    to_add = []

    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    for n in mfcc:
        to_add.append(np.mean(n))

    features.append(np.mean(chroma_stft))
    features.append(np.mean(spec_cent))
    features.append(np.mean(spec_bw))
    features.append(np.mean(rolloff))
    features.append(np.mean(zcr))
    features += to_add

    # predict results
    f = np.array(features)
    f = f.reshape(1, 25)
    f = scaler.transform(f)
    prediction = model.predict(f)
    prob = np.amax(prediction)
    pred = np.argmax(prediction, axis=1)

    if pred == 0:
        outcome = "Healthy"
    elif pred == 1:
        outcome = "Respiratory Tract Infection"
    else:
        outcome = "Chronic Obstructive Pulmonary Disease"

    # TODO - `res` should exactly match whatever schema you use for .dump(res) below
    # TODO - Ensure the key NAMES are identical to PredictCataractResponseSchema
    # TODO - Ensure the value TYPES are identical to PredictCataractResponseSchema
    res: PredictRespiratoryResponseSchema = {
        "probability": prob,
        "outcome": outcome,
    }
    return res
