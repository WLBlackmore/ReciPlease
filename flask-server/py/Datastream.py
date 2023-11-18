import csv
import json

def generateTypeUnitFromCSV(csvFile):
    result = []
    with open(csvFile, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            result.append((row[0], row[1]))
    return result

def convertToDict(arr):
    listOfDicts = [{'Type': tuple[0], 'Unit': tuple[1]} for tuple in arr]
    return listOfDicts

def convertJSONString(dict):
    json_string = json.dumps(dict)
    return json_string

def getJSONStringFromTypeUnit(csvFile):
    return convertJSONString(convertToDict(generateTypeUnitFromCSV(csvFile)))
    