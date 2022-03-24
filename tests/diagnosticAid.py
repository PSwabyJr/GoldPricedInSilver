"""
A list of method(s) that can be useful for unit testing
"""


# Responsible for ensuring if message exist in fileName
def doesStringExistInFile(fileName, message):
    with open(fileName, 'r') as data:
        fileContents = data.readlines()
        contentFound = False

        for line in fileContents:
            if message in line:
                contentFound = True
                break
        data.close()
        return contentFound

if __name__ == '__main__':
    print(doesStringExistInFile('log.txt', 'Gold'))