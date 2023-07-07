import heapq
from abc import abstractclassmethod

# TODO: classes PriceMinMaxAvg and PriceAverage should implement some interface/abstract class... in my opionion, these
# two classes plus the abstract class I'm making will probably belong in a different file. :) We can do that tommorrow.... :)
class PriceMinMaxAvg:
    __priceList = []   # minHeap for storing prices. Used to determine minimum price stored
    __priceListNegative = [] #maxHeap for storing prices. Used to determine maximum priced stored

    def __init__(self):
        heapq.heapify(self.__priceList)
        heapq.heapify(self.__priceListNegative)
    
    def getMaximumPrice(self):
        maxPrice = -1*self.__priceListNegative[0]
        return maxPrice
    
    def getMinimumPrice(self):
        minPrice = self.__priceList[0]
        return minPrice

    def addToHeap(self,newValue):
        heapq.heappush(self.__priceList,newValue)
        newValue*=-1
        heapq.heappush(self.__priceListNegative,newValue)
    
    def resetHeap(self):
        self.__priceList.clear()
        self.__priceListNegative.clear()
    

class PriceAverage:
    __sum = 0.0
    __num_of_times_added = 0

    def addNewPrice(self, price):
        self.__sum += price
        self.__num_of_times_added += 1
    
    def getAverage(self)-> int:        
        return self.__sum/self.__num_of_times_added
        
    def reset(self):
        self.__sum = 0.0
        self.__num_of_times_added = 0

class Processor:
    @abstractclassmethod
    def resetProcessor(self): pass

    @abstractclassmethod
    def processInfo(self, *args): pass


class ForexPriceProcessor(Processor):
    
    __priceAverage = PriceAverage()  # TODO: Will get rid of this (Tightly coupled)
    __priceHeap = PriceMinMaxAvg() # TODO: Will get rid of this (Tightly coupled)

    def __init__(self, priceCollector):        
        self.priceCollector = priceCollector
    
    def __resetProcessor(self):
        self.__priceHeap.resetHeap()
        self.__priceAverage.reset()

    # TODO: What happens if servers are down for the whole day
    def getPricing(self) -> tuple:
        averagePrice = self.__priceAverage.getAverage()
        minimumPrice = self.__priceHeap.getMinimumPrice()
        maximumPrice = self.__priceHeap.getMaximumPrice()
        self.__resetProcessor()
        return averagePrice, minimumPrice, maximumPrice

    def processInfo(self):
        try:
            firstPrice,secondPrice = self.priceCollector.getPricing()
        except Exception as err:
            return f'{err}: ForexPriceProcessor.processInfo()-> Failed to retrieve data due to down server'            
        else:
            price = firstPrice/secondPrice
            self.__priceAverage.addNewPrice(price)
            self.__priceHeap.addToHeap(price)
