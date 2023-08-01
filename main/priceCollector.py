#priceCollector.py

import time
import concurrent.futures
import requests
from abc import abstractmethod, ABC
from days import APITimeout


class RequestError(Exception):
    pass

class PriceCollector:
    @abstractmethod
    def getPricing(self): 
        pass

class PriceCollectorBuilder:
    @abstractmethod
    def buildPriceCollector(self)-> PriceCollector:
        pass
    
class PriceDataFeed(ABC):
    def __init__(self, apiLinks):
        self._apiLinks = apiLinks
        
    @abstractmethod
    def _parsePriceFromDataFeed(self, response):
        pass

    def _getAPIPriceData(self) -> float:
        response = requests.get(self._apiLinks)    
        if response.ok:
            price = self._parsePriceFromDataFeed(response)
            return price
        else:
            raise RequestError(f"Request Unsuccessful. Returned status code {response.status_code} instead of 200!!")

    def getRetrievedPricingFromFeed(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            return executor.map(self._getAPIPriceData(), self._apiLinks)

class ForexDataFeedSwissquote(PriceDataFeed):
    def _parsePriceFromDataFeed(self, response):
        priceData = response.json()
        MT5ServerPrices = priceData[0]['spreadProfilePrices']
        # Price Type: 'Premium'= 0, 'Prime' = 1, 'Standard' = 2
        priceType = 2
        price = MT5ServerPrices[priceType]['ask']
        return price
    
class ForexPriceCollector(PriceCollector):
    
    def __init__(self, apiDataFeed: PriceDataFeed, timeout: APITimeout):
        self._dataFeed = apiDataFeed
        self._timeout = timeout
        
    def getPricing(self) -> list:
        stillWaitingForPricing = True
        priceResults = []
        self._timeout.setNewBeginningTimeInSeconds(time.time())
        
        while stillWaitingForPricing:
            try:
                fetchedData = self._dataFeed.getRetrievedPricingFromFeed()
                for result in fetchedData:
                    priceResults.append(result)
            except RequestError as err:
                priceResults.clear()
                if self._timeout.isTimeUpAfterFailedAttempts():
                    stillWaitingForPricing = False
                continue
            else:
                stillWaitingForPricing = False
        return priceResults

class ForexPriceCollectorBuilder(PriceCollectorBuilder):
    def __init__(self, apiLinks):
        self._dataFeed = ForexDataFeedSwissquote(apiLinks)
        self._timeout = APITimeout()
    
    def buildPriceCollector(self) -> PriceCollector:
        return ForexPriceCollector(self._dataFeed, self._timeout)
    
