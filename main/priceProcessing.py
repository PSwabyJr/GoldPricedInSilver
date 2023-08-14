import statistics
from abc import ABC, abstractclassmethod

from main.priceRepo import PriceRepo

class Processor(ABC):
    @abstractclassmethod
    def _resetProcessor(self): 
        pass

    @abstractclassmethod
    def processData(self): 
        pass

class PriceProcessor(Processor):
    @abstractclassmethod
    def addPrice(self, prices:tuple):
        pass

class GoldSilverPriceProcessor(PriceProcessor):
    def __init__(self, priceRepo: PriceRepo):
        self._priceRepo = priceRepo

    def _resetProcessor(self):
        self._priceRepo.reset_price_repo()

    def processData(self) -> tuple:
        pricesList = self._priceRepo.get_price()
        if len(pricesList) > 0:
            meanPrice = statistics.mean(pricesList)
            minPrice = min(pricesList)
            maxPrice = max(pricesList)
            self._resetProcessor()
            return (minPrice, maxPrice, meanPrice)
        else:
            return (0, 0, 0)
    
    def _convertgoldpricingintosilverounce(self, price_tuple: tuple) -> float:        
        try:
            goldUSDollarPrice = price_tuple[0]
            silverUSDollarPrice = price_tuple[1]
            goldPriceInSilverOunces = goldUSDollarPrice / silverUSDollarPrice
        except ZeroDivisionError:
            goldPriceInSilverOunces = 0
        except IndexError:
            goldPriceInSilverOunces = 0
        except Exception:
            goldPriceInSilverOunces = 0

        return goldPriceInSilverOunces
            
    def addPrice(self, prices: tuple):
        goldPriceInSilverOunces = self._convertgoldpricingintosilverounce(prices)
        self._priceRepo.add_price(goldPriceInSilverOunces)
    

class GoldSilverPriceProcessorBuilder:
    @staticmethod
    def build():
        return GoldSilverPriceProcessor(PriceRepo())