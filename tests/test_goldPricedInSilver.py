import os,sys
import unittest
import time
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.jsonManager import JsonManager
from main.goldPricedInSilver import GoldPricedInSilver
from os.path import exists as file_exists

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
    
    def setUp(self):
        print(f'Testing: {self.shortDescription()}\n')
        self.headerAndfileNames = ['goldPricedInSilver.json', 'goldpricedInSilver', 'cachedData.json']
        self.goldSilverPricing = GoldPricedInSilver(*self.headerAndfileNames)
    
    def testAddingUpdatingPriceData(self):
        """Adding and Updating Price data"""
        for numOfPriceDataSaves in range(5):
            #Adds new price data Every 30 seconds
            for numOfAddingNewPriceData in range(10):
                self.goldSilverPricing.addNewPrice()
                time.sleep(30)
            self.goldSilverPricing.saveNewData()
        """TODO: Need a better way to assert we got the correct data format"""
        self.assertNotEqual(numOfAddingNewPriceData*numOfPriceDataSaves, 50, 'Product must be less than 50')
         
    def tearDown(self):
        print(f'End of Testing: {self.shortDescription()}\n ')
    
if __name__ == '__main__':
    unittest.main()
    


        