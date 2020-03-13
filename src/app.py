import os, json, re

import joblib
import pandas as pd
import s3fs
from flask import Flask, jsonify, request

app = Flask(__name__)

s3 = s3fs.S3FileSystem()
with s3.open('airbnb-barcelona/models/rnd_reg.price', 'rb') as f:
    loaded_model = joblib.load(f)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"response": "hello from airbnb-ml for barcelona!"})

# @app.route('/predict', methods=['POST'])
# def predict():
#     request_payload = request.json
#     input_features = pd.DataFrame([], columns=column_order)
#     input_features = input_features.append(request_payload, ignore_index=True)
#     input_features = input_features.fillna(0)

#     prediction = model.predict(input_features.values.tolist()).tolist()[0]

#     return jsonify({'predicted price (thousands)': prediction})

if __name__ == '__main__':
    # import settings
    # if settings.PORT == 8080:
    app.run(port=8080, host='0.0.0.0', debug=True)
    # else:
        # app.run()