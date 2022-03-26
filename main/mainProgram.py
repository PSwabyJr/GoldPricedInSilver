"""
Collects price information (Gold Priced in Silver Ounces) from  
API (https://forex-data-feed.swissquote.com) and stores data into cachedData.json.
Script executed by Windows Scheduler or Chron.
"""

import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from main.goldPricedInSilver import GoldPricedInSilver
from main.setup import setUpJsonFiles
from os.path import exists as file_exists

if __name__ == '__main__':
    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']

    if not file_exists('cachedData.json') and not file_exists('GoldPricedInSilver.json'):
        setUpJsonFiles()

    goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
    goldSilverPricing.addNewPrice()
