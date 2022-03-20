import os,sys
import unittest
import datetime
from unittest import suite

from requests_mock import mock
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from unittest.mock import patch, Mock
from main.jsonManager import JsonManager
from main.goldPricedInSilver import GoldPricedInSilver
from main.priceProcessing import PriceProcessor
from os.path import exists as file_exists
from mockData import expectedResult
from diagnosticAid import doesStringExistInFile
import filecmp
import os 

class TestGoldPricedInSilver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not file_exists('cachedData.json'):
            cachedDataHeaders = {}
            cachedDataHeaders['sum'] = 0
            cachedDataHeaders['priceList'] = []
            cachedDataHeaders['priceListNegative'] = []
            JsonManager('cachedData.json', **cachedDataHeaders)

        if not file_exists('goldPricedInSilver.json'):
            mainHeader = {}
            mainHeader['goldpricedInSilver'] = []
            JsonManager('goldPricedInSilver.json', **mainHeader)

    @classmethod
    def tearDownClass(cls):
        print(f'End of testing')
        os.remove('cachedData.json')
        os.remove('goldPricedInSilver.json')
        os.remove('log.txt')
    
    def setUp(self):
        print(f'Testing: {self.shortDescription()}\n')
        self.headerAndfileNames = ['goldPricedInSilver.json', 'goldpricedInSilver', 'cachedData.json']
        self.goldSilverPricing = GoldPricedInSilver(*self.headerAndfileNames)
    
    @patch.object(PriceProcessor, 'addNewPrice')
    def testAddNewPrice(self, mock_get_pricing):
        """Testing addNewPrice()"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.return_value = expectedResult
        self.goldSilverPricing.addNewPrice()
        doesfileMatch = filecmp.cmp('expectedCachedData.json', 'cachedData.json')
        print(SCRIPT_DIR)
        if doesfileMatch:
            result = 'Match'
        else:
            result = 'No Match'
        self.assertEqual(result, 'Match', 'File Does not match')
    
    @patch.object(PriceProcessor, 'addNewPrice')
    def testAddNewPriceException(self, mock_get_pricing):
        """Testing addNewPrice() when Exception occurs"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.side_effect = Exception()
        self.goldSilverPricing.addNewPrice()
        result = doesStringExistInFile('log.txt', 'GoldPricedInSilver class, addNewPrice():Failed to retrieve data due to down server')
        self.assertTrue(result, 'Expected a True reponse')
    
    @patch.object(PriceProcessor, 'addNewPrice')
    def testSaveNewData(self, mock_get_pricing):
        """Testing saveData()"""
        mock_get_pricing.return_value = Mock()
        mock_get_pricing.return_value = expectedResult
        self.goldSilverPricing.addNewPrice()
        self.goldSilverPricing.saveNewData()
        savedData = JsonManager('goldPricedInSilver.json').loadJsonFile()
        savedDate = savedData['goldpricedInSilver'][0]['Date']
        savedAverage = savedData['goldpricedInSilver'][0]['Average']
        savedMaximum = savedData['goldpricedInSilver'][0]['Maximum']
        savedMinimum = savedData['goldpricedInSilver'][0]['Minimum']
        self.assertEqual(savedDate, '{:%m-%d-%Y}'.format(datetime.date.today()), 'Saved date should be today date')
        self.assertAlmostEqual(savedAverage, 76.9, 1, 'Saved average should does not match')
        self.assertAlmostEqual(savedMaximum, 91.6, 1, 'Saved maximum should does not match' )
        self.assertAlmostEqual(savedMinimum, 63.9, 1, 'Saved minimum should does not match' )
     
    def tearDown(self):
        print(f'End of Testing: {self.shortDescription()}\n ')
    
if __name__ == '__main__':
    newSuite = unittest.TestSuite()
    newSuite.addTest(TestGoldPricedInSilver("testAddNewPrice"))
    newSuite.addTest(TestGoldPricedInSilver("testSaveNewData"))
    newSuite.addTest(TestGoldPricedInSilver("testAddNewPriceException"))
    runner = unittest.TextTestRunner()
    runner.run(newSuite)
        