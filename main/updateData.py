"""
Uses price information (Gold Priced in Silver Ounces) from
cachedData.json to determine the daily maximum, minimum and averages
prices. Those prices are saved in GoldPricedInSilver.json file.
Script executed by Windows Scheduler or Chron.
"""

# TODO: re-evaluate this file (it might be deleted)

import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from main.goldPricedInSilver import GoldPricedInSilver
from os.path import exists as file_exists

if __name__ == '__main__':

    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']

    if file_exists('GoldPricedInSilver.json') and file_exists('cachedData.json'):
        goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
        goldSilverPricing.saveNewData()
