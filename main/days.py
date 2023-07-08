# days.py
import pytz
from enum import Enum
from datetime import datetime

EST_TIMEZONE = pytz.timezone('US/Eastern')


def getTodayDate()->int:
     return datetime.now(EST_TIMEZONE).weekday()

class DaysOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class DaysOfWeekMonitor:
    @staticmethod
    def hasDateChanged(today) -> bool:
        currentDay = datetime.now(EST_TIMEZONE).weekday()
        if currentDay != today: 
            return True
        else:
            return False
    
    @staticmethod
    def isCurrentTimePast5pm(currentTime)->bool:
        if currentTime.time() >= datetime.time(hour= 17, tzinfo= EST_TIMEZONE):
            return True
        else:
            return False
    
    @staticmethod
    def isTodaySunday(weekday)-> bool:
        if weekday == DaysOfWeek.SUNDAY.value:
            return True
        else:
            return False
    
    @staticmethod
    def isTodayBetweenMondayandThursday(weekday) -> bool:
        if weekday >= DaysOfWeek.MONDAY.value and weekday <= DaysOfWeek.THURSDAY.value:
            return True
        else:
            return False
    
    @staticmethod
    def isCurrentTimeNotPast4pm(currentTime)->bool:
        if currentTime.time() <= datetime.time(hour= 16, tzinfo= EST_TIMEZONE):
            return True
        else:
            return False
    
    @staticmethod
    def isTodayFriday(weekday)-> bool:
        if weekday == DaysOfWeek.FRIDAY.value:
            return True
        else:
            return False