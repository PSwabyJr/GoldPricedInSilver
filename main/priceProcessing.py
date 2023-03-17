'''
** Will need to be refactored (Violates SRP) **
PriceProcessor class used to calculated the average, maximum and 
minimum prices. The prices collected will be stored in a Heap structure. 
'''
import heapq
from main.priceCollector import ForexPriceCollector
from abc import abstractclassmethod
from main.apiLinks import forexLinks  #should be removed
from main.logManager import LogManager # should be removed

class PriceHeap:
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

    def getMinHeap(self)->list:
        return self.__priceList

    def getMaxHeap(self)->list:
        return self.__priceListNegative    
    
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
    
    def getSum(self) -> int:
        return self.__sum
    
    def reset(self):
        self.__sum = 0.0
        self.__num_of_times_added = 0

class Processor:
    @abstractclassmethod
    def resetProcessor(self): pass

    @abstractclassmethod
    def processInfo(self, *args): pass


class ForexPriceProcessor(Processor):
    
    __priceAverage = PriceAverage()
    __priceHeap = PriceHeap()

    def __init__(self, priceCollector, log):        
        self.priceCollector = priceCollector
        self.log = log
        # self.priceCollector = ForexPriceCollector(forexLinks)
        #self.log = LogManager('log.txt')  Need to go should be in a different class for logging information
    
    def resetProcessor(self):
        self.__priceHeap.resetHeap()
        self.__priceAverage.reset()
    
    def processInfo(self):
        try:
            firstPrice,secondPrice = self.priceCollector.getPricing()
        except Exception as err:
            self.log.logDebugMessage('PriceProcessor Class, addNewPrice():Failed to retrieve data due to down server')
            return err
        else:
            self.addToList(firstPrice/secondPrice)
            data  = {}
            data['sum'] = self.__priceAverage.getSum()
            data['priceList'] = self.__priceHeap.getMinHeap() #TODO: why do we need this again
            data['priceListNegative'] = self.__priceHeap.getMaxHeap() #TODO: why do we need this again
            return data



class PriceProcessor:
    def __init__(self):
        '''
        sum: Used to determine the daily average price
        '''
        self.sum = 0
        ''' 
        priceList: minHeap structure for storing prices. Will be used
        to determine the minimum price stored.
        '''
        self.priceList = []
        '''priceListNegative: maxHeap structure for storing prices. Will be
        used to determine the maximum price stored. Price entries are multiplied by -1
        since heapq library only support min Heap structure. 
        Max price will be determined by multiplying the root of the min heap by -1.
        '''
        self.priceListNegative = []
        heapq.heapify(self.priceList)
        heapq.heapify(self.priceListNegative)
        '''
        priceCollector: the class for retrieveing the price of gold/silver through 
        Forex feed's (https://forex-data-feed.swissquote.com)  API calls.
        '''
        self.priceCollector = ForexPriceCollector(forexLinks)
        self.log = LogManager('log.txt')
    
    def setAttributes(self, sum, priceList, priceListNegative):
        self.sum = sum
        self.priceList = priceList
        self.priceListNegative = priceListNegative
    
    def _computeAverage(self):
        average = self.sum/len(self.priceList)
        return average
    
    def _getMaximumPrice(self):
        maxPrice = -1*self.priceListNegative[0]
        return maxPrice
    
    def _getMinimumPrice(self):
        minPrice = self.priceList[0]
        return minPrice

    def _resetSum(self):
        self.sum = 0

    def _eraseList(self):
        self.priceList.clear()
        self.priceListNegative.clear()

    def _incrementSum(self, newValue):
        self.sum += newValue
    
    def addToList(self,newValue):
        heapq.heappush(self.priceList,newValue)
        self._incrementSum(newValue)
        newValue*=-1
        heapq.heappush(self.priceListNegative,newValue)    

    def resetProcessor(self):
        self._eraseList()
        self._resetSum()
    
    def getMaxMinAveragePrices(self):
        max = self._getMaximumPrice()
        min = self._getMinimumPrice()
        avg = self._computeAverage()
        return max,min,avg
    
    def getAttributes(self):
        return self.sum, self.priceList, self.priceListNegative

    # This violates the SRP principle
    def addNewPrice(self):
        try:
            firstPrice,secondPrice = self.priceCollector.getPricing()
        except Exception as err:
            self.log.logDebugMessage('PriceProcessor Class, addNewPrice():Failed to retrieve data due to down server')
            return err
        else:
            self.addToList(firstPrice/secondPrice)
            data  = {}
            data['sum'] = self.sum
            data['priceList'] = self.priceList
            data['priceListNegative'] = self.priceListNegative
            return data
