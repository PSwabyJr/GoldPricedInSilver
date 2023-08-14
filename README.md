# GoldPricedInSilver
Tracking the Price of Gold in Ounces of Silver

Inspired by pricedIngold.com, this software saves the price of gold in ounces of silver. 
It uses api from https://forex-data-feed.swissquote.com to get the price of gold and silver in USD. 
Then it calculates price of gold in ounces of silver by dviding the price of gold (USD) by the price of silver (USD).

main.py starts the execution of this application. Pricing information stored in goldsilverpricejson in the following
format:

{
    "Date": {

                "priceMin": Minimum price,
                "priceMax": Maximum price,
                "priceAvg": Average price

            }

}
