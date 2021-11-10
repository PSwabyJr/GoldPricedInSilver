"""
This script collects price of gold ($USD) from API at https://forex-data-feed.swissquote.com.
The price is collected from MT5 server. The server has 3 categories of commodity pricing 'Prenimum', 
'Prime', and 'Standard'. The 'Standard' price of gold is collected by this script.
"""
import requests

apiLink = 'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD'

def getPriceOfGold():
    priceData = requests.get(apiLink).json()
    MT5ServerPrices = priceData[0]['spreadProfilePrices']
    # Price Type: 'Prenimum'= 0, 'Prime' = 1, 'Standard' = 2
    priceType = 2
    goldPrice = MT5ServerPrices[priceType]['ask']
    return goldPrice
