#priceOutput.py
import datetime
from abc import abstractmethod
from main.fileManager import JsonManager


class PriceOutput:
    @abstractmethod
    def save_price_data(self, data):
        pass

class GoldSilverPriceOutputJSON(PriceOutput):

    def __init__(self, filename:str):
        self._filename = filename

    def _getDate(self)->str:
        today = datetime.datetime.today()
        formatted_date = today.strftime("%m-%d-%Y")
        return formatted_date
    
    def _formatData(self, data:tuple)->dict:  
        
        todaydate = self._getDate()
        formattedData = JsonManager.loadFile(self._filename)

        formattedData[todaydate] = {
            "priceMin": data[0],
            "priceMax": data[1],
            "priceAvg": data[2]
        }

        return formattedData

    def save_price_data(self, data:tuple):
        try:
            formattedData = self._formatData(data)
            JsonManager.addToFile(self._filename, formattedData)
        except Exception as error:
            return error