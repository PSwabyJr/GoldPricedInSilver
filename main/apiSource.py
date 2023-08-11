#apiSource.py

from abc import abstractmethod
from fileManager import JsonManager

class APISource:
    @abstractmethod
    def get_links(self)->list:
        pass

class APIJSON(APISource):

    def __init__(self, filename:str, key:str):
        self._filename = filename
        self._key = key
    
    def get_links(self)->list:
        try:
            links = JsonManager.loadFile(self._filename)
            return links[self._key]
        except KeyError:
            return ['https://www.doesntextist.com']
