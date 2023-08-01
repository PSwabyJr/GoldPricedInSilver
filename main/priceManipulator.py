import heapq
from abc import ABC, abstractclassmethod

class PriceManipulator(ABC):
    @abstractclassmethod
    def reset(self):
        pass
    
    @abstractclassmethod
    def addPriceForManipulation(self, price):
        pass

    @abstractclassmethod
    def getPriceDataAfterManipulation(self):
        pass

class PriceMin(PriceManipulator):
    def __init__(self):
        self._priceHeap= []
        heapq.heapify(self._priceHeap)
    
    def _getHeadOfHeap(self):
        return self._priceHeap[0]
    
    def __getMinimumPrice(self):
        minPrice = self._getHeadOfHeap()
        return minPrice

    def _addPriceToHeap(self, price):
        heapq.heappush(self._priceHeap,price)
    
    def reset(self):
        self._priceHeap.clear()

    def addPriceForManipulation(self, price):
        self._addPriceToHeap(price)
    
    def getPriceDataAfterManipulation(self):
        try:
            priceData = self.__getMinimumPrice()
        except IndexError:
            priceData = 0.0            
        return priceData

class PriceMax(PriceMin):
    # multiplying by -1 ensures we create a max heap using 
    # the heapq library to get maximum price

    def __getMaximumPrice(self):
        maxPrice = -1*self._getHeadOfHeap()
        return maxPrice

    def _addPriceToHeap(self, price):
        price*=-1
        heapq.heappush(self._priceHeap,price)
    
    def getPriceDataAfterManipulation(self):
        try:
            priceData = self.__getMaximumPrice()
        except IndexError:
            priceData = 0.0
        return priceData
    
class PriceAverage(PriceManipulator):
    def __init__(self):
        self._sum= 0.0
        self._num_of_times_added= 0
    
    def _getAverage(self)-> float:        
        return self._sum/self._num_of_times_added
        
    def reset(self):
        self._sum = 0.0
        self._num_of_times_added = 0
    
    def addPriceForManipulation(self, price):
        self._sum += price
        self._num_of_times_added += 1

    def getPriceDataAfterManipulation(self):
        try:
            average = self._getAverage()
        except ZeroDivisionError:
            average = 0.0
        return average
