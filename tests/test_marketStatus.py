import os, sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from datetime import datetime
from unittest.mock import patch
from main.days import EST_TIMEZONE
from main.marketStatus import ForexMarketStatus

class TestForexMarketStatus(unittest.TestCase):

    @patch('main.marketStatus.datetime')
    def test_market_opened_on_sunday_after_5pm(self, mock_datetime):
        sunday = datetime(2023, 8, 13, 17, 30, tzinfo=EST_TIMEZONE)
        mock_datetime.now.return_value = sunday
        self.assertTrue(ForexMarketStatus.isMarketOpened())

    @patch('main.marketStatus.datetime')
    def test_market_opened_between_monday_and_thursday(self, mock_datetime):
        tuesday = datetime(2023, 8, 15, 12, 0, tzinfo=EST_TIMEZONE)
        mock_datetime.now.return_value = tuesday
        self.assertTrue(ForexMarketStatus.isMarketOpened())

    @patch('main.marketStatus.datetime')
    def test_market_opened_on_friday_before_4pm(self, mock_datetime):
        friday = datetime(2023, 8, 18, 15, 30, tzinfo=EST_TIMEZONE)
        mock_datetime.now.return_value = friday
        self.assertTrue(ForexMarketStatus.isMarketOpened())

    @patch('main.marketStatus.datetime')
    def test_market_closed_on_sunday_before_5pm(self, mock_datetime):
        sunday = datetime(2023, 8, 13, 16, 0, tzinfo=EST_TIMEZONE)
        mock_datetime.now.return_value = sunday
        self.assertFalse(ForexMarketStatus.isMarketOpened())

    @patch('main.marketStatus.datetime')
    def test_market_closed_on_friday_after_4pm(self, mock_datetime):
        friday = datetime(2023, 8, 18, 16, 30, tzinfo=EST_TIMEZONE)
        mock_datetime.now.return_value = friday
        self.assertFalse(ForexMarketStatus.isMarketOpened())

if __name__ == '__main__':
    unittest.main()
