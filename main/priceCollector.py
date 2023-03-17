"""
This script is reponsible for the price of gold and silver concurrently through
the use of the ThreadPoolExecutor function from the concurrent.futures library.
"""
import time
import concurrent.futures
import requests
from main.logManager import LogManager # this line should be removed
from abc import abstractmethod

class PriceCollector:
    @abstractmethod
    def getPricing(self): pass

class DataCollector:
    @abstractmethod
    def _getData(self, *args): pass

class ForexPriceCollector(PriceCollector, DataCollector):
    def __init__(self, apiLinks, log):
        self.__apiLinks = apiLinks
        self.__log = log
        #self.__log = LogManager('log.txt')  # this line should be removed

    # TODO: suppose you use a different API....  this stucture maybe irrelevant (you want this to cover anything you put in here)!!!
    # This could change if a different API stucture changes, you want to add whatever you want without changing this code that much, Think OCP!!!
    def _getData(self) -> float:
        response = requests.get(self.__apiLinks)    
        if response.ok:
            priceData = response.json()
            MT5ServerPrices = priceData[0]['spreadProfilePrices']
            # Price Type: 'Premium'= 0, 'Prime' = 1, 'Standard' = 2
            priceType = 2
            price = MT5ServerPrices[priceType]['ask']
            return price
        else:
            return None

    def getPricing(self) -> list:
        failedAPICall = True
        priceResults = []
        beginningTime = time.time()
        timeElapsed = 0.0  #units in seconds
        while failedAPICall and timeElapsed < 240.0:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                try:
                    for result in executor.map(self._getData, self.__apiLinks):
                        priceResults.append(result)
                except Exception as err:
                    currentTime = time.time()
                    timeElapsed = currentTime - beginningTime
                    priceResults.clear()
                    if timeElapsed >= 240.0:
                        self.__log.logDebugMessage('PriceCollector Class, getPricing(): Could not get pricing within 4 minutes')
                        priceResults = err
                    continue
                else:
                    failedAPICall = False
        return priceResults