import sys
import time
from main.days import DaysOfWeekMonitor, getTodayDate
from main.marketStatus import ForexMarketStatus
from datetime import datetime
from fileManager import JsonManager
from priceProcessing import GoldSilverPriceProcessorBuilder, Processor
from priceCollector import ForexPriceCollectorBuilder


# TODO: Lots of cleanup needed in this file, will need to consider how 
# logManager fits in when something goes wrong. 
# Plus some other TODO added

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

def save_results(filename, results):
    data = {
        'Date': getDate(),
        'AveragePrice': results[0],
        'MinimumPrice': results[1],
        'MaximumPrice': results[2]
    }
    update_file(filename, data)
        
def getAPILink(fileName):
    try:
        forexLinks = JsonManager.loadFile(fileName)
        apiLink = forexLinks['forexLinks']
    except Exception as error:
        hell = f'{error}: fileName does not exist!!!' # TODO: how to pass this to log
        sys.exit()

    return apiLink

# TODO: This class will depend on abstractions, not the implementations themselves.
class GoldPricedInSilverApp:
    DATA_FILE = 'goldsilverprice.json'
    FIVE_MINUTES = 60*5

    def __init__(self, priceProcessor: Processor):
        self._priceProcessor = priceProcessor

    def start(self):
        today = getTodayDate()
        while True:
            time.sleep(GoldPricedInSilverApp.FIVE_MINUTES)  
            if ForexMarketStatus.isMarketOpened():
                self._priceProcessor.getPricing()

                if DaysOfWeekMonitor.hasDateChanged(today):
                    priceResults = self._priceProcessor.processData()
                    save_results(GoldPricedInSilverApp.DATA_FILE, priceResults) # TODO: don't want this class to depend on an outside independentfunction, refactor
                    today = getTodayDate() # TODO: don't want this class to depend on an outside independent function, refactor

def main():
    api= 'apiLinks.json'
    apiLinks= getAPILink(api)

    priceCollector = ForexPriceCollectorBuilder(apiLinks).buildPriceCollector()
    priceProcessor = GoldSilverPriceProcessorBuilder(priceCollector).buildPriceProcessor()
    app = GoldPricedInSilverApp(priceProcessor)
    app.start()

if __name__ == '__main__':
    main()