from goldPricedInSilver import GoldPricedInSilverApp, getAPILink
from priceCollector import ForexPriceCollectorBuilder
from priceProcessing import GoldSilverPriceProcessorBuilder


def main():
    api= 'apiLinks.json'
    apiLinks= getAPILink(api)

    priceCollector = ForexPriceCollectorBuilder(apiLinks).buildPriceCollector()
    priceProcessor = GoldSilverPriceProcessorBuilder(priceCollector).buildPriceProcessor()
    app = GoldPricedInSilverApp(priceProcessor)
    app.start()

if __name__ == '__main__':
    main()