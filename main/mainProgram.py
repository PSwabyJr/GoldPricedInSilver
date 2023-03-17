"""
Collects price information (Gold Priced in Silver Ounces) from  
API (https://forex-data-feed.swissquote.com) and stores data into cachedData.json.
Script executed by Windows Scheduler or Chron.
"""
# TODO: re-evaluate this file (it might be deleted)

import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from main.goldPricedInSilver import GoldPricedInSilver
from os.path import exists as file_exists
from main.jsonManager import JsonManager

def setUpJsonFiles():
    mainFileName = 'GoldPricedInSilver.json' 
    cachedFileName = 'cachedData.json'

    # Header for GoldPricedInSilver.json
    mainHeader = {}
    mainHeader['GoldPricedInSilver'] = []

    # Headers for cachedData.json
    cachedDataHeaders = {}
    cachedDataHeaders['sum'] = 0
    cachedDataHeaders['priceList'] = []
    cachedDataHeaders['priceListNegative'] = []

    """
    Using JsonManager to create 'GoldPricedInSilver.json' and
    'cachedData.json.
    """
    mainJsonFile = JsonManager(mainFileName, **mainHeader)
    cachedJsonFile = JsonManager(cachedFileName, **cachedDataHeaders)


if __name__ == '__main__':
    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']

    if not file_exists('cachedData.json') and not file_exists('GoldPricedInSilver.json'):
        setUpJsonFiles()

    goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
    goldSilverPricing.addNewPrice()


# TODO: What's the difference between addNewPrice() and saveNewData()
# We may need to delete updateData.py based on what we can figure out.... 
"""
    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']

    if file_exists('GoldPricedInSilver.json') and file_exists('cachedData.json'):
        goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
        goldSilverPricing.saveNewData()


"""
