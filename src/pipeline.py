# process data from s3
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

import s3fs
import pyarrow.parquet as pq

import transform as trans
import const as const

# load data
s3 = s3fs.S3FileSystem()
filePath = 's3://airbnb-barcelona/valid/currentDate=2020-03-13'
airbnb_df = pq.ParquetDataset(
    filePath, filesystem=s3).read_pandas().to_pandas()

# transformation
airbnb = airbnb_df.drop(columns=const.dropped_columns)
airbnb = trans.drop_rows_occurs_less_than(airbnb, "cancellation_policy", 2)
airbnb = trans.drop_rows_occurs_less_than(
    airbnb, "neighbourhood_group_cleansed", 1)
airbnb = trans.drop_rows_occurs_less_than(airbnb, "host_response_time", 1)
airbnb = airbnb.fillna(value={"host_is_superhost": False})
airbnb = airbnb.fillna(value={"host_has_profile_pic": False})
airbnb = airbnb.fillna(value={"host_identity_verified": False})
airbnb = airbnb.fillna(value={"host_response_time": "N/A"})
airbnb = trans.foldleft(trans.encode_boolean_to_float,
                        airbnb, const.boolean_to_float_cols)
airbnb = trans.extract_num_of_items_for_column(airbnb, "host_verifications")
airbnb = trans.extract_num_of_items_for_column(airbnb, "amenities")
airbnb = airbnb.fillna(airbnb.mean())
# category encode
category_encoder = trans.encode_category_dic(airbnb)
category_dic = trans.foldleft(category_encoder, {}, const.category_columns)
dic_host_response_time = {'host_response_time': {
    'N/A': 1, 'a few days or more': 2, 'within a day': 3, 'within a few hours': 4, 'within an hour': 5}}
category_dic = dict(dic_host_response_time, **category_dic)
airbnb = airbnb.replace(category_dic)

# train
y = airbnb["price"]
X = airbnb.drop(columns=['price'])
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
rnd_regr = RandomForestRegressor(
    min_samples_leaf=4, random_state=0, n_estimators=100)
rnd_regr.fit(x_train, y_train)

# save model
with s3.open('airbnb-barcelona/models/rnd_reg.price', 'wb') as f:
    joblib.dump(rnd_regr, f)
