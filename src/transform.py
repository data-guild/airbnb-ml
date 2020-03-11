import functools, re
import pandas as pd


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
    df = df.fillna(value={column_name: df[column_name].value_counts().index[-1]})
    return df


def fillna_with_highest_occurance(df, column_name):
    df = df.fillna(value={column_name: df[column_name].value_counts().index[0]})
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


def foldleft(func, acc, xs):
    return functools.reduce(func, xs, acc)
