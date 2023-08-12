from goldPricedInSilver import GoldPricedInSilverApp
from priceProcessing import GoldSilverPriceProcessorBuilder
from main.apiSource import APIJSON
from priceCollector import DataFeedBuilder


def main():
    
    apiLinks = APIJSON(filename='apiLinks.json', key="forexLinks")
    apidatafeed = DataFeedBuilder.buildForexDataFeedSwissquote(apiLinks)
    processor = GoldSilverPriceProcessorBuilder.build()
    app = GoldPricedInSilverApp(priceProcessor=processor, dataFeed=apidatafeed)
    app.start()

if __name__ == '__main__':
    main()