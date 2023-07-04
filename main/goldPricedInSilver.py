import sys
import datetime
import pytz
import time
from main.days import DaysOfWeek
from fileManager import JsonManager
from priceProcessing import ForexPriceProcessor
from priceCollector import ForexPriceCollector

FIVE_MINUTES = 60*5
EST_TIMEZONE = pytz.timezone('US/Eastern')

def getDate()-> str:
    today = datetime.datetime.today()
    formatted_date = today.strftime("%m-%d-%Y")
    return formatted_date

def getUpdatedData(fileName,data):
    updatedData = JsonManager.loadFile(fileName)
    updatedData.update(data)
    return updatedData

def update_file(fileName, data):
    updatedData = getUpdatedData(fileName, data)
    JsonManager.addToFile(updatedData)
    
def getAPILink(fileName):
    try:
        forexLinks = JsonManager.loadFile(fileName)
        apiLink = forexLinks['forexLinks']
    except Exception as error:
        hell = f'{error}: fileName does not exist!!!' # how to pass this to log
        sys.exit()

    return apiLink

def hasDateChanged() -> bool:
    # get the current date and time in EST
    now = datetime.datetime.now(EST_TIMEZONE)
    weekday = now.weekday() 
    if weekday != DaysOfWeek.SUNDAY.value:
        return True
    else:
        return False    

def isForexMarketActive() -> bool:
    now = datetime.datetime.now(EST_TIMEZONE)
    weekday = now.weekday()

    # Forex market trades between Sunday 5 pm EST and Friday 4 pm EST
    if weekday == DaysOfWeek.SUNDAY.value:
        if now.time() >= datetime.time(hour= 17, tzinfo= EST_TIMEZONE):
            return True
    
    elif weekday >= DaysOfWeek.MONDAY.value and weekday <= DaysOfWeek.THURSDAY.value:
        return True
    
    elif weekday == DaysOfWeek.FRIDAY.value:
        if now.time() <= datetime.time(hour= 16, tzinfo= EST_TIMEZONE):
            return True
    else:
        return False
    
def main():

    api = 'apiLinks.json'
    dataFile = 'goldsilverprice.json'

    apiLinks = getAPILink(api)
    priceCollector = ForexPriceCollector(apiLinks)
    priceProcessor = ForexPriceProcessor(priceCollector)
   

    while True:

        time.sleep(FIVE_MINUTES)
        # get the current date and time in EST
        now = datetime.datetime.now(EST_TIMEZONE)
        weekday = now.weekday()        
        
        #check to see if date changed. If changed during trading hours, updated json file with average, min, max prices
        if hasDateChanged():
                averagePrice, minimumPrice, maximumPrice = priceProcessor.getPricing()
                
                data = {
                    'Date': getDate(),
                    'AveragePrice': averagePrice,
                    'MinimumPrice': minimumPrice,
                    'MaximumPrice': maximumPrice
                }
                update_file(dataFile, data)

            #today = weekday

        if isForexMarketActive():
            priceProcessor.processInfo()


        # TODO: Notes to be cognizant of..... 
        # want the log manager here at this level to handle saving exception errors from lower classes. 
        # May need to build up goldSilverPrice class again depending how complex this function gets... 
        # consider ways to refactor this stuff as well


# TODO: This class will depend on abstractions, not the implementations themselves.
class GoldPricedInSilver:
    def __init__(self) -> None:
        pass

    def start(self):
        pass

if __name__ == '__main__':
    main()

