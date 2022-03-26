"""
This script is a setup script for creating files
goldPricedInSilver.json and cachedData.json for 
storing data. 
"""

import os,sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
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