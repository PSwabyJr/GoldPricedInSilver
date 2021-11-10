"""
This script is reponsible for the price of gold and silver concurrently through
the use of the ThreadPoolExecutor function from the concurrent.futures library.
"""

import concurrent.futures
from functools import partial
from goldPriceAPI import getPriceOfGold
from silverPriceAPI import getPriceOfSilver

def getCommodityPricing():
    priceResults = []  #collects the prices of gold and silver in the order [goldPrice, silverPrice]
    """
    priceProcessing holds the functions getPriceOfGold() & getPriceOfSilver() for finding the price of Gold and Silver as partials. 
    The partials will be used in getting return values from each function using lambda.
    """
    priceProcessing = [partial(getPriceOfGold), partial(getPriceOfSilver)]
    #fetch the prices of silver and gold concurrently on different threads
    with concurrent.futures.ThreadPoolExecutor() as executor:
        try:
            for result in executor.map(lambda x: x(), priceProcessing):
                priceResults.append(result)
        except Exception:
            print(Exception)    
    return priceResults





    
        


