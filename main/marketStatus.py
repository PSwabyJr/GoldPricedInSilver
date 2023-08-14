#marketStatus.py

from datetime import datetime
from main.days import DaysOfWeekMonitor, EST_TIMEZONE

class ForexMarketStatus:
 
    @staticmethod
    def isMarketOpened()->bool:
        currentTime = datetime.now(EST_TIMEZONE)
        todayDate = currentTime.weekday()

        # Forex market trades between Sunday 5 pm EST and Friday 4 pm EST
        if DaysOfWeekMonitor.isTodaySunday(todayDate) and DaysOfWeekMonitor.isCurrentTimePast5pm(currentTime):
            return True
        elif DaysOfWeekMonitor.isTodayBetweenMondayandThursday(todayDate):
            return True
        elif DaysOfWeekMonitor.isTodayFriday(todayDate) and DaysOfWeekMonitor.isCurrentTimeNotPast4pm(currentTime):
            return True
        else:
            return False