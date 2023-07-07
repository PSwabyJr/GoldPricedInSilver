import heapq
from abc import ABC, abstractclassmethod
from priceManipulator import PriceManipulator, PriceMax, PriceMin, PriceAverage
from priceCollector import PriceCollector

class Processor(ABC):
    @abstractclassmethod
    def resetProcessor(self): 
        pass

    @abstractclassmethod
    def processData(self): 
        pass

class PriceProcessorBuilder(ABC):
    @abstractclassmethod
    def buildPriceProcessor(self) -> Processor:
        pass

class GoldSilverPriceProcessor(Processor):
    def __init__(self, priceCollector: PriceCollector, *priceManipulators: PriceManipulator):        
        self.priceCollector = priceCollector
        self._priceManipulators = []
        self._addPriceManipulators(*priceManipulators)
    
    def _addPriceManipulators(self, *priceManipulators):        
        for priceManipulator in priceManipulators:
            self._priceManipulators.append(priceManipulator)
    
    def resetProcessor(self):
        for priceManipulator in self._priceManipulators:
            priceManipulator.reset()
    
    def processData(self) -> list:
        priceResults = []
        
        for priceManipulator in self._priceManipulators:
            priceData = priceManipulator.getPriceDataAfterManipulation()
            priceResults.append(priceData)
        
        self.resetProcessor()
        return priceResults
    
    def _addNewPrice(self, price):
        for priceManipulator in self._priceManipulators():
            priceManipulator.addPriceForManipulation(price)

    def getPricing(self):
        try:
            goldPrice,silverPrice = self.priceCollector.getPricing()
        except Exception as err:
            return f'{err}: GoldSilverPriceProcessor.getPricing()-> Failed to retrieve data due to down server'            
        else:
            goldPricedInSilver = goldPrice/silverPrice
            self._addNewPrice(goldPricedInSilver)

class GoldSilverPriceProcessorBuilder(PriceProcessorBuilder):
    def __init__(self, priceCollector: PriceCollector):
        self._priceCollector= priceCollector
        self._priceManipulators = (PriceAverage(), PriceMin(), PriceMax())
    
    def buildPriceProcessor(self):
        return GoldSilverPriceProcessor(self._priceCollector, self._priceManipulators)
    
    