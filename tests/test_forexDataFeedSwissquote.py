import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceCollector import ForexDataFeedSwissquote
from unittest.mock import patch, Mock
from main.priceCollector import RequestError

#TODO: Revisit, the test made a few false assumptions about the DATA

class TestForexDataFeedSwissquote(unittest.TestCase):
    def test_parsePriceFromDataFeed(self):
        """test_parsePriceFromDataFeed()"""
        # Prepare a mock response for the test
        mock_response = Mock()
        #  TODO: mock_response.json.return_value should know nothing about the data structure. 
        # Use mockData.py definitions instead
        mock_response.json.return_value = [
            {
                "spreadProfilePrices": [
                    {"ask": 1.12345},
                    {"ask": 1.23456},
                    {"ask": 1.34567}
                ]
            }
        ]
        
        # Create an instance of ForexDataFeedSwissquote
        data_feed = ForexDataFeedSwissquote(apiLinks="http://example.com")
        
        # Call the method being tested
        result = data_feed._parsePriceFromDataFeed(mock_response)
        
        # Check if the result matches the expected price
        self.assertEqual(result, 1.34567)

    @patch('main.priceCollector.requests.get')
    def test_parsePriceFromDataFeed_request_error(self, mock_get):
        """test_parsePriceFromDataFeed_request_error()"""
        # Configure the mock to raise a RequestError
        mock_get.side_effect = RequestError("Test request error")
        
        # Create an instance of ForexDataFeedSwissquote
        data_feed = ForexDataFeedSwissquote(apiLinks="http://example.com")
        
        # Call the method being tested and expect a RequestError
        with self.assertRaises(RequestError):
            data_feed._parsePriceFromDataFeed(mock_get())
            
if __name__ == '__main__':
    unittest.main()
