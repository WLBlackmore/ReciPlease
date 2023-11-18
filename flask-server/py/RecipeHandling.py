import csv
from collections import defaultdict
from FoodProduct import FoodProduct, Unit


class RecipeHandler:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)
        self.groceryList = {}  # Initialize the grocery list


    #csv file reading, loads food products into a dictionary
    def load_products(self, csv_file):
        products = {}
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = FoodProduct(
                    food_type=row['foodName'],
                    product_name=row['productName'],
                    price=float(row['price'][1:]),  # price starts with a currency symbol
                    quantity=float(row['quantity']),
                    unit=Unit(row['unit'])
                )
                products.update({product.productName: product})
        return products

    #Want to return a list of FoodTypes that share a common FoodName
    def check_ingredient_availability(self, ingredient_list):
        results = {}
        for ingredient in ingredient_list:
            # Find all products matching the foodName
            matching_products = [product for product in self.products.values() if product.foodType == ingredient['name']]

            if matching_products:
                # Add the matching products to the results
                results[ingredient['name']] = matching_products
            else:
                print(f"{ingredient['name']} is not found.")

        return results

   
    # Cost for SINGLE ingredient
    def optimizeCostForIngredient(self, foodType, desiredAmount):
        # Get products in descending order
        
        total = 0
        toBuy = []

        for i in range(len(dummyList)):
            counter = 0
            while (total + dummyList[i].quantity <= desiredAmount):
                counter += 1
                total += dummyList[i].quantity

            if counter > 0:
                toBuy.append((dummyList[i].productName, counter))

            if (total >= desiredAmount): break
        
        if total < desiredAmount:
            smallest_item = dummyList[-1]
            additional_units =  -(- (desiredAmount - total) // smallest_item.quantity)
            toBuy.append((smallest_item.productName, additional_units))
        
        return toBuy      
        

    def getPricePerUnit(self, product_name):
        product = self.products.get(product_name)
        if product:
            return product.GetPricePerUnit()
        else:
            print(f"Product '{product_name}' not found.")
            return None
        
    def addToGroceryList(self, productName, required_quantity):
        productName, amount_to_purchase = self.checkExcess(productName, required_quantity)
        if productName in self.groceryList:
            self.groceryList[productName] += amount_to_purchase
        else:
            self.groceryList[productName] = amount_to_purchase

    def printGroceryList(self):
        print("Grocery List:")
        for product, quantity in self.groceryList.items():
            print(f"{product}: {quantity}")

'''
handler = RecipeHandler('ReciPlease/src/Grocery Items Dataset - Sheet1.csv')
pb1 = FoodProduct("Peanut Butter", "big peebee", 3.99, 1000, Unit.G)
pb2 = FoodProduct("Peanut Butter", "medium peebee", 1.99, 500, Unit.G)
pb3 = FoodProduct("Peanut Butter", "wee peebee", 0.99, 250, Unit.G)
    
dummyList = [pb1, pb2, pb3]
AmtNeeded = 2100
toBuy = handler.optimizeCostForIngredient(dummyList, AmtNeeded)
print(toBuy)
'''

'''Example use:
recipe_handler = RecipeHandler('flask-server/py/Grocery Items Dataset - Sheet1.csv')
ingredients = [
    {'name': 'Mixed Nuts', 'quantity': 200, 'unit': Unit.G},
    {'name': 'Olive Oil', 'quantity': 500, 'unit': Unit.ML}
]

# Call the method and store the results
results = recipe_handler.check_ingredient_availability(ingredients)

# Display the results
for ingredient_name, products in results.items():
    print(f"\n{ingredient_name}:")
    for product in products:
        print(f"  Product Name: {product.productName}")
        print(f"  Food Type: {product.foodType}")
        print(f"  Price: {product.price}")
        print(f"  Quantity: {product.quantity} {product.unit.value}")
'''

# recipe_handler = RecipeHandler('src/Grocery Items Dataset - Sheet1.csv')
# ingredients = [
#     {'name': 'Peanut Butter', 'quantity': 1400, 'unit': Unit.G},
#     # Add more ingredients as needed
# ]
# results = recipe_handler.checkExcess(ingredients)
# for ingredient, combos in results.items():
#     for combo in combos:
#         print(f"{ingredient}: {combo[0]}, {combo[1]} units")
