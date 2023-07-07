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

# TODO: PriceMax can inherit from PriceMin since they use the same structure, look into tomorrow
class PriceMin(PriceManipulator):
    def __init__(self):
        self._priceMinHeap= []
        heapq.heapify(self._priceMinHeap)
    
    def _getMinimumPrice(self):
        minPrice = self._priceMinHeap[0]
        return minPrice

    def _addPriceToHeap(self, price):
        heapq.heappush(self._priceMinHeap,price)
    
    def reset(self):
        self._priceMinHeap.clear()

    def addPriceForManipulation(self, price):
        self._addPriceToHeap(price)
    
    def getPriceDataAfterManipulation(self):
        minPrice = self._getMinimumPrice()
        return minPrice

class PriceMax(PriceManipulator):
    def __init__(self):
        self._priceMaxHeap= []
        heapq.heapify(self._priceMaxHeap)
    
    def _getMaximumPrice(self):
        maxPrice = -1*self._priceMaxHeap[0]
        return maxPrice

    def _addPriceToHeap(self, price):
        price*=-1
        heapq.heappush(self._priceMaxHeap,price)
    
    def reset(self):
        self._priceMaxHeap.clear()

    def addPriceForManipulation(self, price):
        self._addPriceToHeap(price)
    
    def getPriceDataAfterManipulation(self):
        maxPrice = self._getMaximumPrice()
        return maxPrice

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
        average = self._getAverage()
        return average
