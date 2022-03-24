"""
Handles logging messages into log files 
"""
from fileinput import filename
import logging


class LogManager:
    def __init__(self, fileName):
        self.fileName = fileName
    
    def logDebugMessage(self ,message):
        logging.basicConfig(filename= self.fileName, level= logging.DEBUG,
        format='%(asctime)s-%(levelname)s-%(message)s')
        logging.debug(message)
        logging.shutdown()
