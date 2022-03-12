"""
Uses price information (Gold Priced in Silver Ounces) from
cachedData.json to determine the daily maximum, minimum and averages
prices. Those prices are saved in GoldPricedInSilver.json file.
Script executed by Windows Scheduler or Chron.
"""

from main.goldPricedInSilver import GoldPricedInSilver

if __name__ == '__main__':
    headerAndfileNames = ['GoldPricedInSilver.json', 'GoldPricedInSilver', 'cachedData.json']
    goldSilverPricing = GoldPricedInSilver(*headerAndfileNames)
    goldSilverPricing.saveNewData()
