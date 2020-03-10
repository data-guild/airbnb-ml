import unittest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal


from src.transform import dummyFun, drop_rows_occurs_less_than


class TestProcessing(unittest.TestCase):
    def test_add_derived_title(self):
        assert_series_equal(
            pd.Series([1, 2, 1, 2]),
            dummyFun()
        )

    def test_drop_rows_occurs_less_than(self):
        data = {'product': ['apple', 'apple', 'banana', 'banana', 'berry'],
                'qty': [10, 12, 6, 8, 3]}
        data_df = pd.DataFrame(data)

        expected_data = {'product': ['apple', 'apple', 'banana', 'banana'],
                         'qty': [10, 12, 6, 8]}
        expected_df = pd.DataFrame(expected_data)
        actual_df = drop_rows_occurs_less_than(data_df, 'product', 2)
        assert_frame_equal(expected_df, actual_df)
