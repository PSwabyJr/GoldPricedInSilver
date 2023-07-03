#priceCollector.py

import time
import concurrent.futures
import requests
from abc import abstractmethod

class PriceCollector:
    @abstractmethod
    def getPricing(self): pass

class DataCollector:
    @abstractmethod
    def _getData(self, *args): pass

class ForexDataFeedSwissquote:

    def retrieveRequestedPriceFromDataFeed(response):
        priceData = response.json()
        MT5ServerPrices = priceData[0]['spreadProfilePrices']
        # Price Type: 'Premium'= 0, 'Prime' = 1, 'Standard' = 2
        priceType = 2
        price = MT5ServerPrices[priceType]['ask']
        return price

class ForexPriceCollector(PriceCollector, DataCollector):
    
    maximumTimeElapsedAllowedInSeconds = 240.0

    def __init__(self, apiLinks, apiDataFeed):
        self._apiLinks = apiLinks
        self._dataFeed = apiDataFeed
        self._beginningTime = 0.0

    def _getparsedPricingFromDataFeed(self,response):
        price = self._dataFeed.retrieveRequestedPriceFromDataFeed(response)
        return price
        
    def _getData(self) -> float:
        response = requests.get(self._apiLinks)    
        if response.ok:
            price = self._getparsedPricingFromDataFeed(response)
            return price
        else:
            return None  # TODO: could pass a custom Exception Error to handle the situation if nothing gets returned instead of passing None. (bad practice)

    def _getNewTimeElapsedInSeconds(self):
        currentTime = time.time()
        timeElapsedInSeconds = currentTime - self._beginningTime
        return timeElapsedInSeconds
    
    def _getRetrievedPricingFromFeed(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            return executor.map(self._getData, self._apiLinks)
        
    def _isTimeUpAfterMultipleAPICalls(self):
        timeElapsedInSeconds = self._getNewTimeElapsedInSeconds()
        if timeElapsedInSeconds >= ForexPriceCollector.maximumTimeElapsedAllowedInSeconds:
            return True
        else:
            return False

    def getPricing(self) -> list:
        IsStillWaitingForPricing = True
        priceResults = []
        self._beginningTime = time.time()
        
        while IsStillWaitingForPricing:
            try:
                for result in self._getRetrievedPricingFromFeed():
                    priceResults.append(result)
            except Exception as err:  # TODO: Will need to create a custom Exception for better readability
                priceResults.clear()
                if self._isTimeUpAfterMultipleAPICalls():
                    IsStillWaitingForPricing = False
                continue
            else:
                IsStillWaitingForPricing = False
        return priceResults
    
    # TODO: Removed the below lines once getPricing() gets updated
    # def getPricing(self) -> list:
    #     IsStillWaitingForPricing = True
    #     priceResults = []
    #     beginningTimeInSeconds = time.time()
    #     timeElapsedInSeconds = 0.0
    #     while IsStillWaitingForPricing and timeElapsedInSeconds < 240.0:
    #         with concurrent.futures.ThreadPoolExecutor() as executor:
    #             try:
    #                 for result in self._getRetrievedPricingFromFeed():
    #                     priceResults.append(result)
    #             except Exception as err:
    #                 timeElapsedInSeconds = self._getNewTimeElapsedInSeconds(beginningTimeInSeconds)
    #                 priceResults.clear()
    #                 if timeElapsedInSeconds >= 240.0:
    #                     pass
    #                 continue
    #             else:
    #                 IsStillWaitingForPricing = False
    #     return priceResults