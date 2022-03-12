"""
This script is a setup script for creating files
goldPricedInSilver.json and cachedData.json for 
storing data. 
"""
from jsonManager import JsonManager

if __name__ == '__main__':

    mainFileName = 'goldPricedInSilver.json' 
    cachedFileName = 'cachedData.json'

    # Header for goldPricedInSilver.json
    mainHeader = {}
    mainHeader['goldpricedInSilver'] = []

    # Headers for cachedData.json
    cachedDataHeaders = {}
    cachedDataHeaders['sum'] = 0
    cachedDataHeaders['pricedLists'] = []
    cachedDataHeaders['priecListsNegative'] = []

    """
    Using JsonManager to create 'goldPricedInSilver.json' and
    'cachedData.json.
    """
    mainJsonFile = JsonManager(mainFileName, **mainHeader)
    cachedJsonFile = JsonManager(cachedFileName, **cachedDataHeaders)