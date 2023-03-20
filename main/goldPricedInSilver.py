import datetime
import pytz
import time
from main.days import DaysOfWeek

FIVE_MINUTES = 60*5

def main():

    cachedfile = 'cachedData.json'
    templatefile = 'dataTemplate.json'
    api = 'apiLinks.json'
    dataFile = 'goldsilverprice.json'

    est_timezone = pytz.timezone('US/Eastern')

    while True:

        time.sleep(FIVE_MINUTES)
        # get the current date and time in EST
        now = datetime.datetime.now(est_timezone)
        weekday = now.weekday()        
        
        #check to see if date changed. If changed during trading hours, use cachedData.json to do the necessary calculations
        # and add the pricing to goldsilverprice.json and then clear cachedData.json. 

        # Forex market trades between 
        # Process adding data to cachedData.json
        if weekday == DaysOfWeek.SUNDAY:
            if now.time() >= datetime.time(hour= 17, tzinfo= est_timezone):
                print('Do something')
        
        elif weekday >= DaysOfWeek.MONDAY and weekday <= DaysOfWeek.THURSDAY:
            print('Do Something')
        
        elif weekday == DaysOfWeek.FRIDAY:
            if now.time() <= datetime.time(hour= 16, tzinfo= est_timezone):
                print('Do something')
        
        else:
            pass


        # TODO: Notes to be cognizant of..... 
        #collect data every 5 minutes (cachedData Very important)
        #only when date changes from Monday -> Tuesday (for example)
        #data from cachedData gets calculated to store the average, max, and min price 
        # into goldsilverprice.json file
        # want the log manager here at this level to handle saving exception errors from lower classes. 
        # May need to build up goldSilverPrice class again depending how complex this function gets... 


if __name__ == '__main__':
    main()

