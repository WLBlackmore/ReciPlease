import csv

def generateTypeUnitFromCSV(csvFile):
    result = []
    with open(csvFile, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            result.append((row[0], row[1]))
    return result

res = generateTypeUnitFromCSV('flask-server\py\FoodTypes.csv')

print(res)