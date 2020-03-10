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
        np.array_equal(expected_df.values,actual_df.values)

    def test_drop_rows_with_values(self):
        data = {'product': ['apple', 'apple', 'banana', 'banana', 'berry'],
                'qty': [10, 12, 6, 8, 3]}
        data_df = pd.DataFrame(data)

        expected_data = {'product': ['banana', 'banana'],
                         'qty': [6, 8]}
        expected_df = pd.DataFrame(expected_data)
        print(expected_df)
        actual_df = trans.drop_rows_with_values(data_df, 'product', ['apple','berry'])
        np.array_equal(expected_df.values,actual_df.values)
