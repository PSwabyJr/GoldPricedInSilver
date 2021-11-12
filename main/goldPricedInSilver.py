#TODO: Other Functions will need to be added and imports for this class
import os
import sys
import datetime
from os.path import exists as file_exists

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from jsonFormatter.jsonManager import JsonManager
from dataProcessing.priceProcessing import PriceProcessor
from commodityPrice.priceCollector import getCommodityPricing

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
        goldPrice,silverPrice = getCommodityPricing()
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



