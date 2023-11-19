import csv
import json
import os

def generateTypeUnitFromCSV(csvFile):
    result = []
    with open(csvFile, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            result.append((row[0], row[1]))
    return result

def convertToDict(arr):
    listOfDicts = [{'ingredient': tuple[0], 'unit': tuple[1]} for tuple in arr]
    return listOfDicts

def convertJSONString(dict):
    json_string = json.dumps(dict)
    return json_string

def getJSONStringFromTypeUnit(csvFile):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_file_path = os.path.join(dir_path, 'FoodTypes.csv')  # Update to your file's relative location
    return convertToDict(generateTypeUnitFromCSV(csv_file_path))
    