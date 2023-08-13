import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceOutput import GoldSilverPriceOutputJSON
from unittest.mock import patch, Mock
from main.fileManager import JsonManager


class TestGoldSilverPriceOutputJSON(unittest.TestCase):
   
   @patch('main.priceOutput.GoldSilverPriceOutputJSON._formatData')
   def test_save_price_data(self, mock_format):

      filename = os.path.join(SCRIPT_DIR, "test.json")
      expected_output_filename = os.path.join(SCRIPT_DIR, "expected_output.json")
      priceOutput = GoldSilverPriceOutputJSON(filename)
      data = (1,2,3)

      mock_format.return_value = {
            "01-01-2021": {
                "priceMin": 1,
                "priceMax": 2,
                "priceAvg": 3
            } 
        }

      priceOutput.save_price_data(data)
      # Assert
      actual = JsonManager.loadFile(filename)
      expected = JsonManager.loadFile(expected_output_filename)
      self.assertEqual(expected, actual)
      erase_file = {}
      JsonManager.addToFile(filename, erase_file)
   
   @patch('main.priceOutput.GoldSilverPriceOutputJSON._getDate')
   def test_formatData(self, mock_getDate):
        filename = os.path.join(SCRIPT_DIR, "test.json")
        priceOutput = GoldSilverPriceOutputJSON(filename)
        data = (1,2,3)
        mock_getDate.return_value = "01-01-2021"
        expected = {
                "01-01-2021": {
                    "priceMin": 1,
                    "priceMax": 2,
                    "priceAvg": 3
                } 
            }
        actual = priceOutput._formatData(data)
        self.assertEqual(expected, actual)
    
   @patch('main.priceOutput.GoldSilverPriceOutputJSON._getDate')
   def test_formatDataWithTwoInputs(self, mock_getDate):
        filename = os.path.join(SCRIPT_DIR, "test.json")
        priceOutput = GoldSilverPriceOutputJSON(filename)
        data = (1,2,3)
        mock_getDate.return_value = "01-01-2021"
        expected = {
                "01-01-2021": {
                    "priceMin": 1,
                    "priceMax": 2,
                    "priceAvg": 3
                }, 
            }
        data_to_add = priceOutput._formatData(data)
        JsonManager.addToFile(filename, data_to_add)

        data = (4,5,6)
        mock_getDate.return_value = "01-02-2021"
        expected = {
                "01-01-2021": {
                    "priceMin": 1,
                    "priceMax": 2,
                    "priceAvg": 3
                },
                "01-02-2021": {
                    "priceMin": 4,
                    "priceMax": 5,
                    "priceAvg": 6
                }
            }
        actual = priceOutput._formatData(data)
        self.assertEqual(expected, actual)
        erase_file = {}
        JsonManager.addToFile(filename, erase_file)

    
   @patch('main.priceOutput.GoldSilverPriceOutputJSON._formatData')
   def test_addingDataOfDifferentDates(self, mock_format):
      filename = os.path.join(SCRIPT_DIR, "test.json")
      expected_output_filename = os.path.join(SCRIPT_DIR, "expected_output.json")
      priceOutput = GoldSilverPriceOutputJSON(filename)
      data = (1,2,3)

      mock_format.return_value = {
            "01-01-2021": {
                "priceMin": 1,
                "priceMax": 2,
                "priceAvg": 3
            } 
        }

      priceOutput.save_price_data(data)
    
      expected_output_filename = os.path.join(SCRIPT_DIR, "expected_output_2.json")
      data = (4,5,6)
      
      mock_format.return_value = {
            "01-01-2021": {
                "priceMin": 1,
                "priceMax": 2,
                "priceAvg": 3
            },
            "01-02-2021": {
                "priceMin": 4,
                "priceMax": 5,
                "priceAvg": 6
            }
        }

      priceOutput.save_price_data(data)
      actual = JsonManager.loadFile(filename)
      expected = JsonManager.loadFile(expected_output_filename)
      self.assertEqual(expected, actual)      

      erase_file = {}
      JsonManager.addToFile(filename, erase_file)


if __name__ == '__main__':
    unittest.main()