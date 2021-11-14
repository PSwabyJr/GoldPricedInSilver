'''
Creates/Updates Json files for data storage
'''

import json

class JsonManager:
    def __init__(self, fileName):
        self.fileName= fileName
    
    def loadJsonFile(self):
        try:
            with open(self.fileName, "r") as read_file:
                data= json.load(read_file)
            read_file.close()
            return data
        except FileNotFoundError as error:
            #print(error)
            #print('File name '+ self.fileName + ' does not exist.')
            return -1
    
    def addToJsonFile(self, data):
        with open(self.fileName, "w") as write_file:
            json.dump(data, write_file, indent=4)
        write_file.close()
        