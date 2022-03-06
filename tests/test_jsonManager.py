import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main.jsonManager import JsonManager
from os.path import exists as file_exists

class TestJsonManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'Beiginning of testing JsonManager class')
    
    @classmethod
    def tearDownClass(cls):
        print(f'End of testing JsonManager class')
    
    def setUp(self):
        print(f'Beginning of test {self.shortDescription()}')
        self.func= JsonManager('test.json')
        os.remove('test.json')   
    
    def testVerifyFileDoesntExist(self):
        """testVerifyFileDoesntExist()"""
        result= self.func.loadJsonFile()
        self.assertEqual(result, -1, "Should be -1")
    
    def testVerifyFileReturnsData(self):
        """testVerifyFileReturnsData()"""
        self.func.addToJsonFile('Twenty')
        result= self.func.loadJsonFile()
        self.assertIsInstance(result, str, "Expected a string")
    
    def tearDown(self):
        print(f'End of test {self.shortDescription()}')
        if file_exists('test.json'):
            os.remove('test.json')
    
if __name__ == '__main__':
    unittest.main()
    