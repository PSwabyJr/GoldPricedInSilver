#TODO: Other Functions will need to be added and imports for this class
#TODO: Description needs to be added as well
import os
import sys
import datetime

from os.path import exists as file_exists
from jsonManager import JsonManager
from priceProcessing import PriceProcessor
from priceCollector import getPricing

class GoldPricedInSilver:
    def __init__(self, fileName):
        self.fileName = os.path.join(os.pardir, fileName)
        self.jsonManager = JsonManager(self.fileName)
        self.processor = PriceProcessor()
        if not file_exists(self.fileName):
            jsonHeader = {}
            jsonHeader["GoldPricedInSilver"] = []
            self.jsonManager.addToJsonFile(jsonHeader)
    def addNewPrice(self):
        goldPrice,silverPrice = getPricing()
        goldConvertedPrice = goldPrice/silverPrice
        self.processor.addToList(goldConvertedPrice)
    def saveNewData(self):
        maxPrice,minPrice,avgPrice = self.processor.getMaxMinAveragePrices()
        newData = {}
        newData['Date'] = '{:%m-%d-%Y}'.format(datetime.date.today())
        newData['Average'] = avgPrice
        newData['Max'] = maxPrice
        newData['Min'] = minPrice
        jsonData = self.jsonManager.loadJsonFile()
        jsonData["GoldPricedInSilver"].append(newData)
        self.jsonManager.addToJsonFile(jsonData)
        self.processor.resetProcessor()

if __name__ == '__main__':
    beginningObj = GoldPricedInSilver('test.json')
    beginningObj.addNewPrice()
    beginningObj.addNewPrice()
    beginningObj.addNewPrice()
    beginningObj.saveNewData()
