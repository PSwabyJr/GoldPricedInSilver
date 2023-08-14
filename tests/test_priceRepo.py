# Build Unit Testing for PriceRepo class
import os,sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import unittest
from unittest.mock import patch, Mock
from main.priceRepo import PriceRepo



class TestPriceRepo(unittest.TestCase):
    def test_add_price(self):
        """test_add_price()"""
        # Create an instance of PriceRepo
        price_repo = PriceRepo()
        
        # Call the method being tested
        price_repo.add_price(1.12345)
        
        # Check if the price was added to the price repo
        self.assertEqual(price_repo.get_price(), [1.12345])
        
    def test_get_price(self):
        """test_get_price()"""
        # Create an instance of PriceRepo
        price_repo = PriceRepo()
        
        # Call the method being tested
        result = price_repo.get_price()
        
        # Check if the price repo is empty
        self.assertEqual(result, [])
        
    def test_reset_price_repo(self):
        """test_reset_price_repo()"""
        # Create an instance of PriceRepo
        price_repo = PriceRepo()
        
        # Add a price to the price repo
        price_repo.add_price(1.12345)

        #Add 3 more prices to the price repo
        price_repo.add_price(1.23456)
        price_repo.add_price(1.34567)
        price_repo.add_price(1.45678)
        
        
        # Call the method being tested
        price_repo.reset_price_repo()
        
        # Check if the price repo is empty
        self.assertEqual(price_repo.get_price(), [])

if __name__ == '__main__':
    unittest.main()