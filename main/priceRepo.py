#priceReop.py

class PriceRepo:
    def __init__(self):
        self._priceRepo = []

    def add_price(self, price:float):
        self._priceRepo.append(price)

    def get_price(self) -> list:
        return self._priceRepo
    
    def reset_price_repo(self):
        self._priceRepo.clear()    