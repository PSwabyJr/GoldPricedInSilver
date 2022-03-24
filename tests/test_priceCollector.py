""" 
Unit testing for priceCollector.py
"""

import os,sys
import unittest
from requests_mock import mock

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from unittest.mock import patch, Mock
from main.priceCollector import PriceCollector
from mockData import forexMockData, silverPriceMockData, goldPriceMockData, MOCK_URL
import main.apiLinks 

class TestPriceCollector(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        print(f'Beginning of testing PriceCollector class')
    
    @classmethod
    def tearDownClass(cls):
        print(f'End of testing PriceCollector class')
    
    def setUp(self):
        print(f'Testing: {self.shortDescription()}\n')
        self.func = PriceCollector(MOCK_URL)
            
    @patch('main.priceCollector.requests.get')
    def testRequestResponseWithDecorator(self, mock_get):
        """Mocking API response using a decorator"""
        mock_get.return_value.status_code = 200  # Mock status code of response
        apiResponse = self.func.getForexData(MOCK_URL)
        # Verify request was successful with status code 200
        self.assertEqual(apiResponse.status_code, 200)
    
    @patch('main.priceCollector.requests.get')
    def testRequestFailedResponse(self, mock_get):
        """Mocking Failed API response using a decorator"""
        mock_get.return_value.status_code = None
        apiReponse = self.func.getForexData(MOCK_URL)
        #Verify API request failed
        self.assertEqual(apiReponse.status_code, None)
    
    @patch.object(PriceCollector, 'getForexData')
    def testGetPricing(self, mock_get_pricing):
        """Get pricing data through mocked API response"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.return_value.json.return_value = silverPriceMockData
        silverMockPrice= self.func.getPricing()[0]
        mock_get_pricing.return_value.json.return_value = goldPriceMockData
        goldMockPrice = self.func.getPricing()[0]
        newPrice = goldMockPrice/silverMockPrice
        self.assertAlmostEqual(newPrice, 78.61, 1)
    
    @patch('main.priceCollector.requests.get')
    def testGetForexDataPriceFails(self, mock_get_pricing):
        """Mocking failure when getForexDataPrice() fails"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.return_value.json.return_value = None
        try:
            result = self.func.getForexDataPrice(MOCK_URL)
        except Exception as err:
            return None
        self.assertRaises(Exception, result)

    @patch('main.priceCollector.requests.get')
    def testGetForexDataPrice(self, mock_get_pricing):
        """Mocking received price from API response"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.return_value.json.return_value = forexMockData
        price = self.func.getForexDataPrice(MOCK_URL)
        self.assertEqual(price, 23.0657 , 'Answer should be 23.0657')
    
    @patch.object(PriceCollector, 'getForexData')
    def testGetForexDataPriceWhenServerDown(self, mock_failed_attempts):
        """Mocking unsuccessful attempts when sending API requests to a downed Server"""
        mock_failed_attempts.return_value = Mock()
        mock_failed_attempts.return_value.json.return_value = None
        self.assertRaises(Exception, self.func.getPricing())

    def tearDown(self):
        print(f'End of Testing: {self.shortDescription()}\n')

if __name__ == '__main__':
    unittest.main()
