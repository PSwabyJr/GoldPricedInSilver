# TODO: Sounds great but I rather put this in a json format that can be changed by anyone. I rather not let anyone go into any python files :)

"""
forexLinks stores the api links from https://forex-data-feed.swissquote.com to collect the price of gold
and silver in ($USD). Both prices are collected from MT5 server. The server has 3 categories of commodity pricing
'Prenium', 'Prime', and 'Standard'. 'Standard' prices of silver and gold will be collected by this script.
"""
forexLinks = [
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD', 
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAG/USD'
    ]