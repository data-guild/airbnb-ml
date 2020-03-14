import json
import joblib
import os
import pandas as pd
import re
import

from flask import Flask, jsonify, request

import const

app = Flask(__name__)
column_order = const.column_order

s3 = s3fs.S3FileSystem()
with s3.open('airbnb-barcelona/models/rnd_reg.price', 'rb') as f:
    loaded_model = joblib.load(f)


@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"response": "hello from airbnb-ml for barcelona!"})


@app.route('/predict_price', methods=['POST'])
def predict():
    request_payload = request.json
    input_features = pd.DataFrame([], columns=column_order)
    input_features = input_features.append(request_payload, ignore_index=True)
    # predict using model
    prediction = loaded_model.predict([input_features.iloc[0]])
    return jsonify({"prediction": prediction.tolist()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
