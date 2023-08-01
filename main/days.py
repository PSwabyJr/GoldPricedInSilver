# days.py
import pytz
import time
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

class APITimeout:

    def __init__(self, maxAllowedElapsedTimeInSeconds = 240.0):
        self._maxAllowedElapsedTimeInSeconds = maxAllowedElapsedTimeInSeconds
        self._beginningTimeInSeconds = 0.0
    
    def setNewBeginningTimeInSeconds(self, newTimeInSeconds):
        self._beginningTimeInSeconds = newTimeInSeconds

    def _isTimeElapsedExceedMaximumAllowed(self):
        currentTimeInSeconds = time.time()
        timeElapsedInSeconds = currentTimeInSeconds - self._beginningTimeInSeconds
        if timeElapsedInSeconds >= self._maxAllowedElapsedTimeInSeconds:
            return True
        else:
            return False

    def isTimeUpAfterFailedAttempts(self):
        return self._isTimeElapsedExceedMaximumAllowed()  