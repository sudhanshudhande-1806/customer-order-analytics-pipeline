import unittest
import os

class TestPipeline(unittest.TestCase):

    def test_output_exists(self):
        self.assertTrue(
            os.path.exists(
                "data/processed/city_sales_report.json"
            )
        )

if __name__ == '__main__':
    unittest.main()