#goldPricedInSilver.py

import time
from main.days import DaysOfWeekMonitor
from main.marketStatus import ForexMarketStatus
from priceProcessing import PriceProcessor
from priceCollector import PriceDataFeed
from main.priceOutput import PriceOutput


class GoldPricedInSilverApp:
    DATA_FILE = 'goldsilverprice.json'
    FIVE_MINUTES = 60*5

    def __init__(self, priceProcessor: PriceProcessor, dataFeed:PriceDataFeed):
        self._priceProcessor = priceProcessor
        self._dataFeed = dataFeed
        self._output = PriceOutput(GoldPricedInSilverApp.DATA_FILE)
    
    def _save_results(self):
        priceData = self._priceProcessor.processData()
        self._output.save_price_data(priceData)

    def _get_pricing(self):
        retrievedprices = self._dataFeed.getRetrievedPricingFromFeed()
        self._priceProcessor.addPrice(retrievedprices)

    def start(self):
        today = DaysOfWeekMonitor.getTodayDate()
        while True:
            time.sleep(GoldPricedInSilverApp.FIVE_MINUTES)  
            if ForexMarketStatus.isMarketOpened():
                self._get_pricing()
                if DaysOfWeekMonitor.hasDateChanged(today):
                    self._save_results()
                    today = DaysOfWeekMonitor.getTodayDate()
            else:
                if DaysOfWeekMonitor.hasDateChanged(today):
                    today = DaysOfWeekMonitor.getTodayDate() # for the situation when it's Sunday but the app still thinks today is Saturday

