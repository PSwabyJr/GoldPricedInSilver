import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.priceProcessing import GoldSilverPriceProcessor
from unittest.mock import patch, Mock
from main.priceRepo import PriceRepo

class TestGoldSilverPriceProcessor(unittest.TestCase):
    def test_addPrice(self):
        """test_addPrice()"""
        # Create an instance of GoldSilverPriceProcessor
        price_repo = PriceRepo()
        price_processor = GoldSilverPriceProcessor(priceRepo=price_repo)
        
        # Call the method being tested
        price_processor.addPrice((1, 2))
        
        # Check if the price was added to the price repo
        self.assertEqual(price_repo.get_price(), [0.5])
        
    def test_processData(self):
        """test_processData()"""
        # Create an instance of GoldSilverPriceProcessor
        price_repo = PriceRepo()
        price_processor = GoldSilverPriceProcessor(priceRepo=price_repo)
        
        # Add some prices to the price repo
        price_repo.add_price(1)
        price_repo.add_price(2)
        price_repo.add_price(3)
        
        # Call the method being tested
        result = price_processor.processData()
        
        # Check if the result matches the expected price
        self.assertEqual(result, (1, 3, 2))
        
    def test_processData_no_prices(self):
        """test_processData_no_prices()"""
        # Create an instance of GoldSilverPriceProcessor
        price_repo = PriceRepo()
        price_processor = GoldSilverPriceProcessor(priceRepo=price_repo)
        
        # Call the method being tested
        result = price_processor.processData()
        
        # Check if the result matches the expected price
        self.assertEqual(result, (0, 0, 0))
        
    def test_processData_one_price(self):
        """test_processData_one_price()"""
        # Create an instance of GoldSilverPriceProcessor
        price_repo = PriceRepo()
        price_processor = GoldSilverPriceProcessor(priceRepo=price_repo)
        
        # Add some prices to the price repo
        price_repo.add_price(1)
        
        # Call the method being tested
        result = price_processor.processData()
        
        # Check if the result matches the expected price
        self.assertEqual(result, (1, 1, 1))
        
    def test_processData_zero_price(self):
        """test_processData_zero_price()"""
        # Create an instance of GoldSilverPriceProcessor
        price_repo = PriceRepo()
        price_processor = GoldSilverPriceProcessor(priceRepo=price_repo)
        
        # Add some prices to the price repo
        price_repo.add_price(0)
        
        # Call
        result = price_processor.processData()

        # Check if the result matches the expected price
        self.assertEqual(result, (0, 0, 0))


if __name__ == '__main__':
    unittest.main()