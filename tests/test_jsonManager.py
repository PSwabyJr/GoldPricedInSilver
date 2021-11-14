import os,sys
import unittest
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from jsonFormatter.jsonManager import JsonManager

class TestJsonManager(unittest.TestCase):
    def setUp(self):
        print(sys.path)
        self.func= JsonManager('test.json')   
    
    def testVerifyFileDoesntExist(self):
        result= self.func.loadJsonFile()
        self.assertEqual(result, -1)
    
    def testVerifyFileReturnsData(self):
        self.func.addToJsonFile('Twenty')
        result= self.func.loadJsonFile()
        self.assertIsInstance(result, str)
    
if __name__ == '__main__':
    unittest.main()
    