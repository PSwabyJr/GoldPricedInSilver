"""
This script is reponsible for the price of gold and silver concurrently through
the use of the ThreadPoolExecutor function from the concurrent.futures library.
"""
import time
import concurrent.futures
import requests
#from apiLinks import forexLinks
class PriceCollector:
    def __init__(self, apiLinks):
        self.apiLinks = apiLinks

    def getForexData(self, apiLink):
        response = requests.get(apiLink)
        if response.ok:
            return response
        else:
            return None
        
    def getForexDataPrice(self, apiLink) -> float:
        priceRequest = self.getForexData(apiLink)
        priceData = priceRequest.json()
        MT5ServerPrices = priceData[0]['spreadProfilePrices']
        # Price Type: 'Premium'= 0, 'Prime' = 1, 'Standard' = 2
        priceType = 2
        price = MT5ServerPrices[priceType]['ask']
        return price

    def getPricing(self) -> list:
        failedAPICall = True
        priceResults = []
        beginningTime = time.time()
        timeElapsed = 0.0  #units in seconds
        while failedAPICall and timeElapsed < 240.0:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                try:
                    for result in executor.map(self.getForexDataPrice, self.apiLinks):
                        priceResults.append(result)
                except Exception as err:
                    currentTime = time.time()
                    timeElapsed = currentTime - beginningTime
                    priceResults.clear()
                    if timeElapsed >= 240.0:
                        print('Could not get pricing within 4 minutes')
                        priceResults = err
                    continue
                else:
                    print('Success')
                    failedAPICall = False
        return priceResults