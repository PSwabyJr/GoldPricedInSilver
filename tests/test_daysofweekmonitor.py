import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.days import DaysOfWeekMonitor
from unittest.mock import patch, Mock


class TestDaysOfWeekMonitor(unittest.TestCase):
    # @patch('main.days.datetime')
    # def test_hasDateChanged(self, mock_datetime):
    #     """test_hasDateChanged()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     mock_now = mock_datetime.now
    #     mock_now.return_value.weekday.return_value = 1
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.hasDateChanged(0)
        
    #     # Check if the result matches the expected value
    #     self.assertTrue(result, 'Result is not True')

    # @patch('main.days.datetime')    
    # def test_hasDateChanged_same_date(self, mock_datetime):
    #     """test_hasDateChanged_same_date()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     mock_now = mock_datetime.now
    #     mock_now.return_value.weekday.return_value = 1
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.hasDateChanged(1)
        
    #     # Check if the result matches the expected value
    #     self.assertFalse(result, 'Result is not False')
        
        
    def test_isCurrentTimePast5pm(self):
        """test_isCurrentTimePast5pm()"""
        # Create an instance of DaysOfWeekMonitor
        days_of_week_monitor = DaysOfWeekMonitor()
        
        # Create a mock datetime object
        mock_datetime = Mock()
        mock_datetime.now.return_value = Mock(time=Mock(return_value=Mock(hour=18)))
        
        # Call the method being tested
        result = days_of_week_monitor.isCurrentTimePast5pm(mock_datetime)
        
        # Check if the result matches the expected value
        self.assertEqual(result, True)
        
    # def test_isCurrentTimePast5pm_before_4pm(self):
    #     """test_isCurrentTimePast5pm_before_5pm()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Create a mock datetime object
    #     mock_datetime = Mock()
    #     mock_datetime.now.return_value = Mock(time=Mock(return_value=Mock(hour=16)))
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isCurrentTimePast5pm(mock_datetime)
        
    #     # Check if the result matches the expected value
    #     self.assertEqual(result, False)
        
    # def test_isTodaySunday(self):
    #     """test_is  TodaySunday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodaySunday(6)
        
    #     # Check if the result matches the expected value
    #     self.assertTrue(result, 'Today is not Sunday, expected a Sunday value')

    # def test_isTodaySunday_not_sunday(self):
    #     """test_isTodaySunday_not_sunday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodaySunday(0)
        
    #     # Check if the result matches the expected value
    #     self.assertFalse(result, 'Today is Sunday, expected a non-Sunday value') 
    
    # def test_isTodayBetweenMondayandThursday(self):
    #     """test_isTodayBetweenMondayandThursday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodayBetweenMondayandThursday(2)
        
    #     # Check if the result matches the expected value
    #     self.assertTrue(result, 'Today is not between Monday and Thursday, expected a Monday through Thursday value')
    
    # def test_isTodayBetweenMondayandThursday_not_between_monday_and_thursday(self):
    #     """test_isTodayBetweenMondayandThursday_not_between_monday_and_thursday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodayBetweenMondayandThursday(6)
        
    #     # Check if the result matches the expected value
    #     self.assertFalse(result, 'Today is between Monday and Thursday, expected a non-Monday through Thursday value')
    
    # def test_isCurrentTimeNotPast4pm(self):
    #      """test_isCurrentTimeNotPast4pm()"""
    #      # Create an instance of DaysOfWeekMonitor
    #      days_of_week_monitor = DaysOfWeekMonitor()
    #      days_of_week_monitor.isCurrentTimePast5pm = Mock(return_value=False)
    #      result = days_of_week_monitor.isCurrentTimeNotPast4pm(Mock())
    #      self.assertTrue(result, 'Current time is past 4pm, expected a time before 4pm')
    
    # def test_isCurrentTimeNotPast4pm_past_4pm(self):
    #         """test_isCurrentTimeNotPast4pm_past_4pm()"""
    #         # Create an instance of DaysOfWeekMonitor
    #         days_of_week_monitor = DaysOfWeekMonitor()
    #         days_of_week_monitor.isCurrentTimePast5pm = Mock(return_value=True)
    #         result = days_of_week_monitor.isCurrentTimeNotPast4pm(Mock())
    #         self.assertFalse(result, 'Current time is not past 4pm, expected a time after 4pm')
    
    # def test_isTodayFriday(self):
    #     """test_isTodayFriday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodayFriday(4)
        
    #     # Check if the result matches the expected value
    #     self.assertTrue(result, 'Today is not Friday, expected a Friday value')
    
    # def test_isTodayFriday_not_friday(self):
    #     """test_isTodayFriday_not_friday()"""
    #     # Create an instance of DaysOfWeekMonitor
    #     days_of_week_monitor = DaysOfWeekMonitor()
        
    #     # Call the method being tested
    #     result = days_of_week_monitor.isTodayFriday(0)
        
    #     # Check if the result matches the expected value
    #     self.assertFalse(result, 'Today is Friday, expected a non-Friday value')

if __name__ == '__main__':
    unittest.main()

         



