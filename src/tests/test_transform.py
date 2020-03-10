import unittest
import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal
from src.transform import dummyFun


class TestProcessing(unittest.TestCase):
    def test_add_derived_title(self):
        assert_series_equal(
            pd.Series([1, 2, 1, 2]),
            dummyFun()
        )
