# days.py
import pytz
import time
from enum import Enum
from datetime import datetime

EST_TIMEZONE = pytz.timezone('US/Eastern')

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
    def hasDateChanged(today:int) -> bool:
        currentDay = datetime.now(EST_TIMEZONE).weekday()
        if currentDay != today: 
            return True
        else:
            return False
    
    @staticmethod
    def getTodayDate()->int:
        return datetime.now(EST_TIMEZONE).weekday()
    
    @staticmethod
    def isCurrentTimePast5pm(currentDateTime:datetime)->bool:
        currentTime = currentDateTime.time()
        timeAt5pm = currentTime.replace(hour= 17, minute= 0, second= 0, microsecond= 0, tzinfo= EST_TIMEZONE)
        if currentTime >= timeAt5pm:
            return True
        else:
            return False
    
    @staticmethod
    def isTodaySunday(weekday: int)-> bool:
        if weekday == DaysOfWeek.SUNDAY.value:
            return True
        else:
            return False
    
    @staticmethod
    def isTodayBetweenMondayandThursday(weekday: int) -> bool:
        if weekday >= DaysOfWeek.MONDAY.value and weekday <= DaysOfWeek.THURSDAY.value:
            return True
        else:
            return False
    
    @staticmethod
    def isCurrentTimeNotPast4pm(currentDateTime:datetime)->bool:
        currentTime = currentDateTime.time()
        timeAt4pm = currentTime.replace(hour= 16, minute= 0, second= 0, microsecond= 0, tzinfo= EST_TIMEZONE)
        if currentTime <= timeAt4pm:
            return True
        else:
            return False
    
    @staticmethod
    def isTodayFriday(weekday: int)-> bool:
        if weekday == DaysOfWeek.FRIDAY.value:
            return True
        else:
            return False
