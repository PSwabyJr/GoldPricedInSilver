"""
This script is reponsible for the price of gold and silver concurrently through
the use of the ThreadPoolExecutor function from the concurrent.futures library.
"""

import concurrent.futures
import requests

"""
apiLinks stores the api links from https://forex-data-feed.swissquote.com to collect the price of gold
and silver in ($USD). Both prices are collected from MT5 server. The server has 3 categories of commodity pricing
'Prenium', 'Prime', and 'Standard'. 'Standard' prices of silver and gold will be collected by this script.
"""
apiLinks = [
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD', 
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAG/USD'
    ]

"""
getForexDataPrice(apiLink) handles api calls from https://forex-data-feed.swissquote.com for gathering the
prices of silver and gold.
"""
def getForexDataPrice(apiLink):
    priceData = requests.get(apiLink).json()
    MT5ServerPrices = priceData[0]['spreadProfilePrices']
    # Price Type: 'Prenimum'= 0, 'Prime' = 1, 'Standard' = 2
    priceType = 2
    price = MT5ServerPrices[priceType]['ask']
    return price

def getPricing():
    priceResults = [] #collects the prices of gold and silver in the order [goldPrice, silverPrice]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        try:
            for result in executor.map(getForexDataPrice, apiLinks):
                priceResults.append(result)
        except Exception:
            print(Exception)
    return priceResults

if __name__ == '__main__':
    goldPrice, silverPrice = getPricing()
    print(goldPrice)
    print(silverPrice)
