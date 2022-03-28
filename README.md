# GoldPricedInSilver
Tracking the Price of Gold in Ounces of Silver

Inspired by pricedIngold.com, this software saves the price of gold in ounces of silver. 
It uses api from https://forex-data-feed.swissquote.com to get the price of gold and silver in USD. 
Then it calculates price of gold in ounces of silver by dviding the price of gold (USD) by the price of silver (USD).
mainProgram.py is responsible for calcuating the price and saving the price in a cached json file. 

The daily price of gold (in ounces of silver) are saved in json file using updateData.py. 
The software saves the daily maximum, average and minimum price.

Highly Recommend using windows Scheduler or Chron to call mainProgram.py and updateData.py
mainProgram.py can be used to collect data every 5 minutes. 
updateData.py can be called once a day (prefarably close to midnight).
