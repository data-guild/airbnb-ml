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


# utils
def foldleft(func, acc, xs):
    return functools.reduce(func, xs, acc)


def explode_string_to_list(list_in_string, pattern_to_remove):
    return re.sub(pattern_to_remove, '', list_in_string.strip()).lower().split(',')


def flatten(list_of_lists):
    return itertools.chain.from_iterable(list_of_lists)
