import functools
import pandas as pd


def drop_rows_occurs_less_than(df, columnName, low_bound):
    counts = df[columnName].value_counts()
    to_remove = counts[counts <= low_bound].index
    new_df = df[~df[columnName].isin(to_remove)]
    return new_df


def drop_rows_with_values(df, columnName, values):
    new_df = df[~df[columnName].isin(values)]
    return new_df


def encode_boolean_to_float(df, columnName):
    df[columnName] = df[columnName].astype(float)
    return df


def fillna_with_lowest_occurance(df, columnName):
    df = df.fillna(value={columnName: df[columnName].value_counts().index[-1]})
    return df


def fillna_with_highest_occurance(df, columnName):
    df = df.fillna(value={columnName: df[columnName].value_counts().index[0]})
    return df


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
