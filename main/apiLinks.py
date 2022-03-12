"""
forexLinks stores the api links from https://forex-data-feed.swissquote.com to collect the price of gold
and silver in ($USD). Both prices are collected from MT5 server. The server has 3 categories of commodity pricing
'Prenium', 'Prime', and 'Standard'. 'Standard' prices of silver and gold will be collected by this script.
"""
forexLinks = [
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD', 
    'https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAG/USD'
    ]