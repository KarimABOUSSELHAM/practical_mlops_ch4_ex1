from flask import Flask, jsonify, request

import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)

def scale(payload):
  scaler=StandardScaler().fit(payload)
  return scaler.transform(payload)

@application.route("/")
def home():
  return "<h3>Skelarn prediction container</h3>"

@application.route("/predict", methods=["POST"])
def predict():
  clf = joblib.load("boston_housing_prediction.joblib")
  inference_payload=pd.DataFrame(request.json)
  scaled_payload=scale(inference_payload)
  prediction=list(clf.predict(scaled_payload))
  return jsonify({"prediction": prediction})

@application.route('/example', methods=["GET"])
def example():
  return jsonify({"CHAS": {"0": 0},
                  "RM": {"0": 6.575},
                  "TAX": {"0": 296.0},
                  "PTRATIO": {"0": 15.3},
                  "B": {"0": 396.9},
                  "LSTAT": {"0": 4.98}})
  
@application.route("/metadata", methods=["GET"])
def metadata():
  return jsonify({"model title": "Boston housing price prediction",
                  "model type": "regression",
                  "training data source": "UCI Machine Learning Repository",
                  "training data": "Boston housing dataset",
                  "training data url": "https://www.kaggle.com/code/prasadperera/the-boston-housing-dataset",
                  "input features": ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"],
                  "output feature": "MEDV"})

if __name__ == "__main__":
  application.run(host="0.0.0.0", port=5001, debug=True)