import json
from abc import ABC


class FileManager(ABC):

    @staticmethod
    def loadFile(filename): pass

    @staticmethod
    def addToFile(filename): pass


class JsonManager(FileManager):

    @staticmethod
    def loadFile(fileName) -> dict:
        try:
            with open(fileName, "r") as read_file:
                data= json.load(read_file)
            read_file.close()
            return data
        except Exception as error:
            return error
    
    @staticmethod
    def addToFile(fileName, data):
        with open(fileName, "w") as write_file:
            json.dump(data, write_file, indent=4)
        write_file.close()        