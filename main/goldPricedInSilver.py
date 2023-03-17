"""
Manages the saving and adding data of Gold Priced in Silver
 """
import datetime
from main.jsonManager import JsonManager
from main.priceProcessing import PriceProcessor
from main.logManager import LogManager

# TODO: This straight up violates Single Responsiblity principle... consider a huge restructure of this class.

class GoldPricedInSilver:
    def __init__(self, *args):
        self.fileName = args[0]
        self.headerTitle = args[1]
        self.jsonManager = JsonManager(self.fileName, self.headerTitle)
        self.cachedFile = args[2]
        self.processor = PriceProcessor()
        self.headerList = ['sum', 'priceList', 'priceListNegative']  # TODO:Suppose headerlist was different for a new change.... 
        self.log = LogManager('log.txt')
    
    def _saveToCachedJson(self, data):
        cachedJson = JsonManager(self.cachedFile, *self.headerList)
        cachedData = cachedJson.loadJsonFile()
        if cachedData == -1:
            self.log.logDebugMessage('GoldPricedInSilver Class, _saveToCachedJson(): FileName '+ self.cachedFile + ' not found!!')
        else:
            self.processor.setAttributes(cachedData['sum'], cachedData['priceList'], cachedData['priceListNegative'])
            cachedJson.addToJsonFile(data)    
        
    def _getCachedJson(self):
        cachedJson = JsonManager(self.cachedFile, *self.headerList)
        cachedData = cachedJson.loadJsonFile()
        if cachedData == -1:
            self.log.logDebugMessage('GoldPricedInSilver Class, _saveToCachedJson(): FileName '+ self.cachedFile + ' not found!!')
        else:
            self.processor.setAttributes(cachedData['sum'], cachedData['priceList'], cachedData['priceListNegative'])
        
    def _updatedJsonData(self, list, *args):
        data = {}
        for arg in args:
            data[arg] = list[arg]
        return data
    
    def _createPriceDictionary(self):
        maxPrice,minPrice,avgPrice = self.processor.getMaxMinAveragePrices()
        newData = {}
        newData['Date'] = '{:%m-%d-%Y}'.format(datetime.date.today())
        newData['Average'] = avgPrice
        newData['Maximum'] = maxPrice
        newData['Minimum'] = minPrice
        return newData
    
    def _clearCacheFile(self):
        self.processor.resetProcessor()
        sum, priceList, priceListNegative = self.processor.getAttributes()
        clearedData = {}
        clearedData['sum'] = sum
        clearedData['priceList'] = priceList
        clearedData['priceListNegative'] = priceListNegative
        return clearedData

    def addNewPrice(self):
        try:
            self._getCachedJson()
            results = self.processor.addNewPrice()
        except Exception as err:
            self.log.logDebugMessage('GoldPricedInSilver class, addNewPrice():Failed to retrieve data due to down server')
        else:
            newData = self._updatedJsonData(results, *self.headerList)
            self._saveToCachedJson(newData)

    def saveNewData(self):
        self._getCachedJson()
        newData = self._createPriceDictionary()
        jsonData = self.jsonManager.loadJsonFile()
        jsonData[self.headerTitle].append(newData)
        self.jsonManager.addToJsonFile(jsonData)
        clearedData = self._clearCacheFile()
        self._saveToCachedJson(clearedData)
