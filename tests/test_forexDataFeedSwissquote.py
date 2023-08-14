import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceCollector import ForexDataFeedSwissquote
from unittest.mock import patch, Mock
from main.priceCollector import RequestError
from mockData import forexMockData

class TestForexDataFeedSwissquote(unittest.TestCase):
    def test_parsePriceFromDataFeed(self):
        """test_parsePriceFromDataFeed()"""
        # Prepare a mock response for the test
        mock_response = Mock()
        mock_response.json.return_value = forexMockData
        
        # Create an instance of ForexDataFeedSwissquote
        data_feed = ForexDataFeedSwissquote(apiLinks="http://example.com")
        
        # Call the method being tested
        result = data_feed._parsePriceFromDataFeed(mock_response)
        
        # Check if the result matches the expected price
        self.assertEqual(result, 23.0657)

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
    
    @patch('main.priceCollector.PriceDataFeed._getAPIPriceData')
    def test_getRetrievedPricingFromFeed_success(self, mock_getAPIPriceData):
        # Configure the mock responses for successful requests
        results = []
        mock_response_1 = Mock()
        mock_response_1.return_value = 1.12345

        mock_response_2 = Mock()
        mock_response_2.return_value = 1.23456
        
        # Configure the mock _getAPIPriceData to return the mock responses
        mock_getAPIPriceData.side_effect = [mock_response_1, mock_response_2]
        
        # Create an instance of ForexDataFeedSwissquote
        data_feed = ForexDataFeedSwissquote(apiLinks=["http://example.com", 
                                                      "http://example2.com"])
        
        # Call the method being tested
        retreived_prices = data_feed.getRetrievedPricingFromFeed()

        for price in retreived_prices:
            results.append(price.return_value)

        # Check if the results match the expected prices
        self.assertEqual(results, [1.12345, 1.23456])


    @patch('main.priceCollector.requests.get')
    def test_getRetrievedPricingFromFeed_request_error(self, mock_get):
        # Configure the mock to raise a RequestError
        mock_get.side_effect = RequestError("Test request error")
        
        # Create an instance of ForexDataFeedSwissquote
        data_feed = ForexDataFeedSwissquote(apiLinks=["http://example.com"])
        
        # Call the method being tested and expect a RequestError
        result =data_feed.getRetrievedPricingFromFeed()

        self.assertEqual(result, [0])
            
if __name__ == '__main__':
    unittest.main()
