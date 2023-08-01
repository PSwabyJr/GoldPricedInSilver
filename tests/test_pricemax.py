""" 
Unit testing for PriceMax class
"""

import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceManipulator import PriceMax

class TestPriceMax(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'Beiginning of testing PriceMax class')
    
    @classmethod
    def tearDownClass(cls):
        print(f'End of testing PriceMax class')
    
    def setUp(self):
        print(f'Beginning of test {self.shortDescription()}')
        self.func= PriceMax()
    
    def testVerifyPriceMax(self):
        """testVerifyPriceMax()"""
        self.func.addPriceForManipulation(10)
        self.func.addPriceForManipulation(20)
        self.func.addPriceForManipulation(30)
        result= self.func.getPriceDataAfterManipulation()
        self.assertEqual(result, 30, "Should be 30")
    
    def testreset(self):
        """testreset()"""
        self.func.addPriceForManipulation(10)
        self.func.addPriceForManipulation(20)
        self.func.addPriceForManipulation(30)
        self.func.reset()
        result= self.func.getPriceDataAfterManipulation()
        self.assertEqual(result, 0, "Should be 0")
    
    def testaddpriceformanipulation(self):
        """testaddpriceformanipulation()"""
        self.func.addPriceForManipulation(10)
        self.func.addPriceForManipulation(20)
        self.func.addPriceForManipulation(30)
        result = len(self.func._priceHeap)
        self.assertEqual(result, 3, "Should be 3")
    
    def tearDown(self):
        print(f'End of test {self.shortDescription()}')

if __name__ == '__main__':
    unittest.main()