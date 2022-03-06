'''
PriceProcessor class used to calculated the average, maximum and 
minimum prices. The prices collected will be stored in a Heap structure. 
'''
import heapq
from main.priceCollector import PriceCollector
from main.apiLinks import forexLinks
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
        self.priceCollector = PriceCollector(forexLinks)
    
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

    def addNewPrice(self):
        try:
            firstPrice,secondPrice = self.priceCollector.getPricing()
        except Exception as err:
            return err
        else:
            self.addToList(firstPrice/secondPrice)
            data  = {}
            data['sum'] = self.sum
            data['priceList'] = self.priceList
            data['priceListNegative'] = self.priceListNegative
            return data
