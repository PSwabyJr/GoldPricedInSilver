import heapq
from abc import abstractclassmethod
from priceManipulator import PriceManipulator
from priceCollector import PriceCollector

class Processor:
    @abstractclassmethod
    def resetProcessor(self): 
        pass

    @abstractclassmethod
    def processData(self): 
        pass

class ForexGoldSilverPriceProcessor(Processor):
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
            return f'{err}: ForexGoldSilverPriceProcessor.getPricing()-> Failed to retrieve data due to down server'            
        else:
            goldPricedInSilver = goldPrice/silverPrice
            self._addNewPrice(goldPricedInSilver)
