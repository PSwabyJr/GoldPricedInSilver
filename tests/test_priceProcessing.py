import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceProcessing import PriceProcessor

class TestPriceProcessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'Beginning of testing PriceProcessor class')
    
    @classmethod
    def tearDownClass(cls):
        print(f'End of testing PriceProcessor class')
    
    def setUp(self):
        print(f'Beginning of test {self.shortDescription()}')
        self.func = PriceProcessor()

    def testNumbersAreBeingAdded(self):
        """testNumbersAreBeingAdded()"""
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        self.assertEqual(self.func.sum, 15, "Should be 15")
    
    def testGetMinMaxAvgPrices(self):
        """testGetMinMaxAvgPrices()"""
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        max,min,avg = self.func.getMaxMinAveragePrices()
        self.assertEqual([max,min,avg], [5,1,3], "Should be [5,1,3]")
    
    def testResettingProcessor(self):
        """testResettingProcessor()"""
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        max,min,avg = self.func.getMaxMinAveragePrices()
        self.func.resetProcessor()
        self.assertEqual(self.func.sum, 0, "Should be 0")
    
    def testClearLists(self):
        """testClearLists()"""
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        max,min,avg = self.func.getMaxMinAveragePrices()
        self.func.resetProcessor()
        '''
        Lists priceList and priceListNegative should be the size of 0
        if they are cleared by PriceProcesssor.resetProcessor()
        '''
        size = len(self.func.priceList)+len(self.func.priceListNegative)
        self.assertEqual(size,0, "Should be 0.")
    
    def testAddNewPrice(self):
        """testAddNewPrice()"""
        result = self.func.addNewPrice()
        self.assertIsInstance(result, dict, "Expected a dictionary")
    
    def tearDown(self):
        print(f'End of test {self.shortDescription()}\n')

if __name__ == '__main__':
    unittest.main()
