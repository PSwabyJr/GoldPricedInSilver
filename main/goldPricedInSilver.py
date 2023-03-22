import sys
import datetime
import pytz
import time
from main.days import DaysOfWeek
from fileManager import JsonManager
from priceProcessing import ForexPriceProcessor
from priceCollector import ForexPriceCollector

FIVE_MINUTES = 60*5

def getDate()-> str:
    today = datetime.datetime.today()
    formatted_date = today.strftime("%m-%d-%Y")
    return formatted_date

def update_file(fileName, data):
    savedData = JsonManager.loadFile(fileName)
    savedData.update(data)
    JsonManager.addToFile(savedData)
    
def getAPILink(fileName):
    try:
        forexLinks = JsonManager.loadFile(fileName)
        apiLink = forexLinks['forexLinks']
    except Exception as error:
        hell = f'{error}: fileName does not exist!!!' # how to pass this to log
        sys.exit()

    return apiLink

    
def main():

    api = 'apiLinks.json'
    dataFile = 'goldsilverprice.json'

    apiLinks = getAPILink(api)
    priceCollector = ForexPriceCollector(apiLinks)
    priceProcessor = ForexPriceProcessor(priceCollector)

    est_timezone = pytz.timezone('US/Eastern')
    today = datetime.datetime.now(est_timezone).weekday()

    while True:

        time.sleep(FIVE_MINUTES)
        # get the current date and time in EST
        now = datetime.datetime.now(est_timezone)
        weekday = now.weekday()        
        
        #check to see if date changed. If changed during trading hours, updated json file with average, min, max prices
        if weekday != today:
            if weekday != DaysOfWeek.SUNDAY.value:
                averagePrice, minimumPrice, maximumPrice = priceProcessor.getPricing()
                
                data = {
                    'Date': getDate(),
                    'AveragePrice': averagePrice,
                    'MinimumPrice': minimumPrice,
                    'MaximumPrice': maximumPrice
                }
                update_file(dataFile, data)

            today = weekday
        
        # Forex market trades between Sunday 5 pm EST and Friday 4 pm EST
        if weekday == DaysOfWeek.SUNDAY.value:
            if now.time() >= datetime.time(hour= 17, tzinfo= est_timezone):
                priceProcessor.processInfo()
        
        elif weekday >= DaysOfWeek.MONDAY.value and weekday <= DaysOfWeek.THURSDAY.value:
            priceProcessor.processInfo()
        
        elif weekday == DaysOfWeek.FRIDAY.value:
            if now.time() <= datetime.time(hour= 16, tzinfo= est_timezone):
                priceProcessor.processInfo()
        
        else:
            pass


        # TODO: Notes to be cognizant of..... 
        # want the log manager here at this level to handle saving exception errors from lower classes. 
        # May need to build up goldSilverPrice class again depending how complex this function gets... 
        # consider ways to refactor this stuff as well


if __name__ == '__main__':
    main()

