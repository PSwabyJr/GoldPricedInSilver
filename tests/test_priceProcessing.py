import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceProcessing import PriceProcessor

class TestPriceProcessor(unittest.TestCase):
    def setUp(self):
        self.func = PriceProcessor()

    def testNumbersAreBeingAdded(self):
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        self.assertEqual(self.func.sum, 15)
    
    def testGetMinMaxAvgPrices(self):
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        max,min,avg = self.func.getMaxMinAveragePrices()
        self.assertEqual([max,min,avg], [5,1,3])
    
    def testResettingProcessor(self):
        sampleData = [4,2,1,3,5]
        for number in sampleData:
            self.func.addToList(number)
        max,min,avg = self.func.getMaxMinAveragePrices()
        self.func.resetProcessor()
        self.assertEqual(self.func.sum, 0)
    
    def testClearLists(self):
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
        self.assertEqual(size,0)

if __name__ == '__main__':
    unittest.main()
