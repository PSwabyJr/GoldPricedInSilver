#TODO: Other Functions will need to be added and imports for this class
#TODO: Description needs to be added as well
import datetime

from main.jsonManager import JsonManager
from main.priceProcessing import PriceProcessor

class GoldPricedInSilver:
    def __init__(self, *args):
        self.fileName = args[0]
        self.headerTitle = args[1]
        self.jsonManager = JsonManager(self.fileName, self.headerTitle)
        self.cachedFile = args[2]
        self.processor = PriceProcessor()
        self.headerList = ['sum', 'priceList', 'priceListNegative']
    
    def _saveToCachedJson(self, data):
        cachedJson = JsonManager(self.cachedFile, *self.headerList)
        cachedData = cachedJson.loadJsonFile()
        self.processor.setAttributes(cachedData['sum'], cachedData['priceList'], cachedData['priceListNegative'])
        cachedJson.addToJsonFile(data)

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
            results = self.processor.addNewPrice()
        except Exception:
            #TODO: will need to print this to a log once we're done
            print('Failed to retrieve data due to down server')
        else:
            newData = self._updatedJsonData(results, *self.headerList)
            self._saveToCachedJson(newData)

    def saveNewData(self):
        newData = self._createPriceDictionary()
        jsonData = self.jsonManager.loadJsonFile()
        jsonData[self.headerTitle].append(newData)
        self.jsonManager.addToJsonFile(jsonData)
        clearedData = self._clearCacheFile()
        self._saveToCachedJson(clearedData)
