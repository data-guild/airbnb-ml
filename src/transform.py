from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import functools
import re
import pandas as pd
import itertools
from sklearn.preprocessing import MultiLabelBinarizer
from collections import Counter


def drop_rows_occurs_less_than(df, column_name, low_bound):
    counts = df[column_name].value_counts()
    to_remove = counts[counts <= low_bound].index
    new_df = df[~df[column_name].isin(to_remove)]
    return new_df


def drop_rows_with_values(df, column_name, values):
    new_df = df[~df[column_name].isin(values)]
    return new_df


def encode_boolean_to_float(df, column_name):
    df[column_name] = df[column_name].astype(float)
    return df


def fillna_with_lowest_occurance(df, column_name):
    df = df.fillna(
        value={column_name: df[column_name].value_counts().index[-1]})
    return df


def fillna_with_highest_occurance(df, column_name):
    df = df.fillna(
        value={column_name: df[column_name].value_counts().index[0]})
    return df


def extract_num_of_items(input):
    input = input.split(",")
    return len(input)


def extract_num_of_items_for_column(df, column_name):
    df[column_name] = df[column_name].apply(extract_num_of_items)
    return df


def string_to_timestamp(input_format):
    def h(input):
        result = pd.to_datetime(input, format=input_format)
        return result
    return h


def days_from_date(compare_date=pd.to_datetime('now')):
    def h(input_date):
        return (compare_date-input_date).days
    return h


def encode_category_dic(dataframe):
    def h(dica, columnName):
        labels = dataframe[columnName].astype(
            'category').cat.categories.tolist()
        encode_dic = {columnName: {k: v for k, v in zip(
            labels, list(range(1, len(labels)+1)))}}
        return dict(dica, **encode_dic)
    return h


def get_one_hot_encoded_df(source_df):
    mlb = MultiLabelBinarizer()
    return pd.DataFrame(mlb.fit_transform(source_df),
                        columns=mlb.classes_,
                        index=source_df.index)


def get_keys_below_threshold(series, threshold):
    dictionary = dict(Counter(flatten(series.values)))
    keys_to_remove = []
    for amenity, count in dictionary.items():
        if count < threshold:
            keys_to_remove.append(amenity)

    return keys_to_remove

# cindy
def removeRowsWithValues(df , col, values):
    return df[~df[col].isin(values)]

import statsmodels.api as sm

def get_sig_columns(X, y):
    estimator = sm.OLS(y, X)
    smodel=estimator.fit()
    smodel.summary()
    smodel.pvalues
    sig_features = [f for f, p in zip(X.columns, smodel.pvalues) if p < 0.05]
    return X[sig_features]

def drop_columns(df):
    dropped_columns = ["first_review", "last_review", "has_availability", "market",'rowId','id','host_location','host_neighbourhood','street','neighbourhood','neighbourhood_cleansed','calendar_updated','license', 'amenities','property_type','zipcode','host_verifications','host_since','reviews_per_month']
    df = df.drop(dropped_columns, axis=1)
    return df

def drop_rows(df):
    dropped_cols_rows_df = df.dropna(subset=["bedrooms", "host_listings_count","host_total_listings_count","bathrooms", "beds"])
    dropped_host_response_time = ["ES","el Barri Gòtic"]
    dropped_cols_rows_df = removeRowsWithValues(dropped_cols_rows_df, "host_response_time", dropped_host_response_time)
    dropped_price = [0.0]
    dropped_cols_rows_df = removeRowsWithValues(dropped_cols_rows_df, "price", dropped_price)
    return dropped_cols_rows_df

def fill_missing_data(df):
    values = {'security_deposit': 0, 'cleaning_fee': 0, "host_response_time":"N/A", "host_response_rate": 0, "host_has_profile_pic": 0, "host_identity_verified": 0, "host_is_superhost": 0}
    return df.fillna(value=values)

def convert_boolean_to_float(df):
    cols = ["host_has_profile_pic","host_identity_verified", "host_is_superhost", "is_location_exact", "instant_bookable", "require_guest_profile_picture", "require_guest_phone_verification"]
    for col in cols:
        df[col] = pd.to_numeric(df[col]).astype('int64')
    return df

import numpy as np
from sklearn.impute import SimpleImputer
def fill_missing_data_with_mean(df):
    cols_filled_with_nums = ["review_scores_rating","review_scores_accuracy","review_scores_cleanliness","review_scores_checkin","review_scores_communication","review_scores_location","review_scores_value"]
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[cols_filled_with_nums] = imp.fit_transform(df[cols_filled_with_nums])
    return df

def one_hot_encoding(df):
    dropped_cols_rows_encoding_df = pd.get_dummies(df, columns=['host_response_time'], prefix = ['host_response_time'])
    dropped_cols_rows_encoding_df = pd.get_dummies(dropped_cols_rows_encoding_df, columns=['bed_type'], prefix = ['bed_type'])
    dropped_cols_rows_encoding_df = pd.get_dummies(dropped_cols_rows_encoding_df, columns=['room_type'], prefix = ['room_type'])
    dropped_cols_rows_encoding_df = pd.get_dummies(dropped_cols_rows_encoding_df, columns=['cancellation_policy'], prefix = ['cancellation_policy'])
    dropped_cols_rows_encoding_df = pd.get_dummies(dropped_cols_rows_encoding_df, columns=['neighbourhood_group_cleansed'], prefix = ['neighbourhood_group_cleansed'])
    return dropped_cols_rows_encoding_df

# ml util


def compute_mse_r2(_model, x_test, y_test):
    y_predict = _model.predict(x_test)
    r2 = r2_score(y_test, y_predict)
    mse = mean_squared_error(y_test, y_predict)
    return (r2, mse)


def get_best_model(_model, x_train, y_train):
    grid_search = GridSearchCV(_model, {}, cv=5, scoring=('r2'))
    _model.fit(x_train, y_train)
    return grid_search.best_estimator_

# utils


def foldleft(func, acc, xs):
    return functools.reduce(func, xs, acc)


def explode_string_to_list(list_in_string, pattern_to_remove):
    return re.sub(pattern_to_remove, '', list_in_string.strip()).lower().split(',')


def flatten(list_of_lists):
    return itertools.chain.from_iterable(list_of_lists)
