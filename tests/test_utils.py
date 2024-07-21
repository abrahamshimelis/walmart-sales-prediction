import unittest
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from src.utils import check_missing_data

class TestDataChecks(unittest.TestCase):

    def test_check_missing_data(self):
        df = pd.DataFrame({
            'A': [1, 2, np.nan],
            'B': [4, np.nan, np.nan],
            'C': [7, 8, 9]
        })
        result = check_missing_data(df)
        self.assertEqual(result['Column Name'].tolist(), ['A', 'B'])
        self.assertEqual(result['Missing Values'].tolist(), [1, 2])

if __name__ == '__main__':
    unittest.main()