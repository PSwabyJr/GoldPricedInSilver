"""
Collects price information (Gold Priced in Silver Ounces) from  
API (https://forex-data-feed.swissquote.com) and stores data into cachedData.json.
Script executed by Windows Scheduler or Chron.
"""

from main.goldPricedInSilver import GoldPricedInSilver

if __name__ == '__main__':
    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']
    goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
    goldSilverPricing.addNewPrice()
