import datetime
import time
from enum import Enum


FIVE_MINUTES = 60*5

class DaysOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def main():

    cachedfile = 'cachedData.json'
    templatefile = 'dataTemplate.json'
    api = 'apiLinks.json'
    dataFile = 'goldsilverprice.json'

    while True:

        today = datetime.date.today()

        if today.weekday() not in (DaysOfWeek.SATURDAY,DaysOfWeek.SUNDAY):   
            time.sleep(FIVE_MINUTES)
            #collect data every 5 minutes (cachedData Very important)
            #only when date changes from Monday -> Tuesday (for example)
            #data from cachedData gets calculated to store the average, max, and min price 
            # into goldsilverprice.json file
            # want the log manager here at this level to handle saving exception errors from lower classes. 
            # May need to build up goldSilverPrice class again depending how complex this function gets... 



if __name__ == '__main__':
    main()

