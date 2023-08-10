#priceCollector.py

import time
import concurrent.futures
import requests
from abc import abstractmethod, ABC

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

    def _getAPIPriceData(self, apiLinks:str) -> float:
        response = requests.get(apiLinks)    
        if response.ok:
            return self._parsePriceFromDataFeed(response)
        else:
            error_message = f"Request Unsuccessful. Returned status code {response.status_code} instead of 200!!"
            raise RequestError(error_message)

    def getRetrievedPricingFromFeed(self):
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            try:
                for result in executor.map(self._getAPIPriceData, self._apiLinks):
                    results.append(result)
            except RequestError:
                results.append(0)
        return results
        
class ForexDataFeedSwissquote(PriceDataFeed):
    def _parsePriceFromDataFeed(self, response):
        priceData = response.json()
        MT5ServerPrices = priceData[0]['spreadProfilePrices']
        # Price Type: 'Premium'= 0, 'Prime' = 1, 'Standard' = 2
        priceType = 2
        price = MT5ServerPrices[priceType]['ask']
        return price
    
class ForexPriceCollector(PriceCollector):
    
    def __init__(self, apiDataFeed: PriceDataFeed):
        self._dataFeed = apiDataFeed
        
    def getPricing(self) -> list:
        priceResults = self._dataFeed.getRetrievedPricingFromFeed()   
        return priceResults

class ForexPriceCollectorBuilder(PriceCollectorBuilder):
    def __init__(self, apiLinks):
        self._dataFeed = ForexDataFeedSwissquote(apiLinks)
    
    def buildPriceCollector(self) -> PriceCollector:
        return ForexPriceCollector(self._dataFeed)
    
