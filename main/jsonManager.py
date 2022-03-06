'''
Creates/Updates Json files for data storage
'''
import json
from os.path import exists as file_exists

class JsonManager:    
    def __init__(self, fileName, *args, **kwargs):
        self.fileName = fileName
        if not file_exists(self.fileName):
            jsonHeader = {}
            for titleHeader in args:
                jsonHeader[titleHeader] = []
            for titleHeader in kwargs:
                jsonHeader[titleHeader] = kwargs[titleHeader]
            self.addToJsonFile(jsonHeader) 
    
    def loadJsonFile(self):
        try:
            with open(self.fileName, "r") as read_file:
                data= json.load(read_file)
            read_file.close()
            return data
        except FileNotFoundError as error:
            return -1
    
    def addToJsonFile(self, data):
        with open(self.fileName, "w") as write_file:
            json.dump(data, write_file, indent=4)
        write_file.close()
        