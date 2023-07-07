import sys
import datetime
import pytz
import time
from main.days import DaysOfWeek
from fileManager import JsonManager
from priceProcessing import GoldSilverPriceProcessorBuilder, Processor
from priceCollector import ForexPriceCollectorBuilder


# TODO: Lots of cleanup needed in this file, will need to consider how logManager fits in when something goes wrong


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

# TODO: ForexMarketStatus class will handle all (Will utilize Static Methods) the important stuff on activity etc., may put this in a separate file
class ForexMarketStatus:
    pass

# TODO: This class will depend on abstractions, not the implementations themselves.
class GoldPricedInSilverApp:
    DATA_FILE = 'goldsilverprice.json'
    FIVE_MINUTES = 60*5
    EST_TIMEZONE = pytz.timezone('US/Eastern')

    def __init__(self, priceProcessor: Processor):
        self._priceProcessor = priceProcessor

    def start(self):
        while True:
            # TODO: Will clean this up :)
            time.sleep(GoldPricedInSilverApp.FIVE_MINUTES)
            # get the current date and time in EST
            now = datetime.datetime.now(GoldPricedInSilverApp.EST_TIMEZONE)
            weekday = now.weekday()        

            #check to see if date changed. If changed during trading hours, updated json file with average, min, max prices
            if hasDateChanged():
                    priceResults = self._priceProcessor.processData()

                    data = {
                        'Date': getDate(),
                        'AveragePrice': priceResults[0],
                        'MinimumPrice': priceResults[1],
                        'MaximumPrice': priceResults[2]
                    }
                    update_file(GoldPricedInSilverApp.DATA_FILE, data)

                #today = weekday

            if isForexMarketActive():
                self._priceProcessor.getPricing()



def main():
    api= 'apiLinks.json'
    apiLinks= getAPILink(api)

    priceCollector = ForexPriceCollectorBuilder(apiLinks).buildPriceCollector()
    priceProcessor = GoldSilverPriceProcessorBuilder(priceCollector).buildPriceProcessor()
    app = GoldPricedInSilverApp(priceProcessor)
    app.start()



if __name__ == '__main__':
    main()

