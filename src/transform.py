import pandas as pd


def dummyFun():
    return pd.Series([1, 2, 1, 2])


def drop_rows_occurs_less_than(data_df, columnName, low_bound):
    counts = data_df[columnName].value_counts()
    to_remove = counts[counts < low_bound].index
    df = data_df[~data_df[columnName].isin(to_remove)]
    return df
