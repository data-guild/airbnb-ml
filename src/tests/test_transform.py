import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal, assert_series_equal


import transform as trans


class TestProcessing(unittest.TestCase):
    def test_drop_rows_occurs_less_than(self):
        data = {'product': ['apple', 'apple', 'banana', 'banana', 'berry'],
                'qty': [10, 12, 6, 8, 3]}
        data_df = pd.DataFrame(data)

        expected_data = {'product': ['apple', 'apple', 'banana', 'banana'],
                         'qty': [10, 12, 6, 8]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.drop_rows_occurs_less_than(data_df, 'product', 1)
        np.array_equal(expected_df.values, actual_df.values)

    def test_drop_rows_with_values(self):
        data = {'product': ['apple', 'apple', 'banana', 'banana', 'berry'],
                'qty': [10, 12, 6, 8, 3]}
        data_df = pd.DataFrame(data)

        expected_data = {'product': ['banana', 'banana'],
                         'qty': [6, 8]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.drop_rows_with_values(
            data_df, 'product', ['apple', 'berry'])
        np.array_equal(expected_df.values, actual_df.values)

    def test_encode_boolean_to_float(self):
        data = {'soldout': [True, False, True]}
        data_df = pd.DataFrame(data)
        expected_data = {'soldout': [1.0, 0.0, 1.1]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.encode_boolean_to_float(data_df, 'soldout')
        np.array_equal(expected_df.values, actual_df.values)

    def test_fillna_with_lowest_occurance(self):
        data = {'product': [np.NaN, "apple", "apple", "pear"],
                'color': [np.NaN, "red", "red", "white"]}
        data_df = pd.DataFrame(data)
        expected_data = {'product': ["pear", "apple", "apple", "pear"], 'color': [
            np.NaN, "red", "red", "white"]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.fillna_with_lowest_occurance(data_df, 'product')
        assert_frame_equal(expected_df, actual_df)

    def test_fillna_with_highest_occurance(self):
        data = {'product': [np.NaN, "apple", "apple", "pear"],
                'color': [np.NaN, "red", "red", "white"]}
        data_df = pd.DataFrame(data)
        expected_data = {'product': ["apple", "apple", "apple", "pear"], 'color': [
            np.NaN, "red", "red", "white"]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.fillna_with_highest_occurance(data_df, 'product')
        assert_frame_equal(expected_df, actual_df)

    def test_extract_num_of_items(self):
        data1 = "['a', 'b', 'c']"
        data2 = '{TV,Wifi,"Air conditioning"'
        self.assertEqual(trans.extract_num_of_items(data1), 3)
        self.assertEqual(trans.extract_num_of_items(data2), 3)

    def test_extract_num_of_items_for_column(self):
        data = {'product': ["['a', 'b', 'c']",  "['a', 'b', 'c', 'd']"]}
        data_df = pd.DataFrame(data)
        expected_data = {'product': [3, 4]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = trans.extract_num_of_items_for_column(data_df, 'product')
        assert_frame_equal(expected_df, actual_df)
