import keras as K
from azureml.core.model import Model
from keras.models import Sequential
from keras.models import load_model
import h5py
import sys
import os
import numpy as np
import json

def init():
    global model
    print("Python version: " + str(sys.version) + ", keras version: " + K.__version__)
    print("Executing init() method...")
    model_path = Model.get_model_path('model.h5')
    print("got model...")
    model = K.models.load_model(model_path)
    print("loaded model...")

def run(raw_data):
    print("Executing run(raw_data) method...")
    data = np.array(json.loads(raw_data)['data'])
    data = np.reshape(data, (30,28,28,1))
    y_hat = model.predict(data)
    print("Eexcuted predictions...")
    return json.dumps(y_hat.tolist())
