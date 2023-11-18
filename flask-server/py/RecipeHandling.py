import csv
from collections import defaultdict
from FoodProduct import FoodProduct, Unit


class RecipeHandler:
    def __init__(self, csv_file):
        self.products = self.load_products(csv_file)

    def load_products(self, csv_file):
        products = defaultdict(list)
        with open(csv_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = FoodProduct(
                    food_type=row['foodName'],
                    product_name=row['productName'],
                    price=float(row['price'][1:]),
                    quantity=float(row['quantity']),
                    unit=Unit(row['unit'])
                )
                products[product.foodType] = product
        return products

    def check_ingredient_availability(self, ingredient_list):
        for ingredient in ingredient_list:
            product = self.products.get(ingredient['name'])
            if product:
                required_quantity = ingredient['quantity']
                if product.quantity >= required_quantity:
                    print(f"{ingredient['name']} is available in sufficient quantity.")
                else:
                    print(f"{ingredient['name']} is not available in sufficient quantity.")
            else:
                print(f"{ingredient['name']} is not found.")

   
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

handler = RecipeHandler('ReciPlease\src\Grocery Items Dataset - Sheet1.csv')
pb1 = FoodProduct("Peanut Butter", "big peebee", 3.99, 1000, Unit.G)
pb2 = FoodProduct("Peanut Butter", "medium peebee", 1.99, 500, Unit.G)
pb3 = FoodProduct("Peanut Butter", "wee peebee", 0.99, 250, Unit.G)
    
dummyList = [pb1, pb2, pb3]
AmtNeeded = 2100
toBuy = handler.optimizeCostForIngredient(dummyList, AmtNeeded)
print(toBuy)

'''Example use:
recipe_handler = RecipeHandler('src/Grocery Items Dataset - Sheet1.csv')
ingredients = [
    {'name': 'Eggs', 'quantity': 200, 'unit': Unit.G},
    {'name': 'Whole Milk', 'quantity': 500, 'unit': Unit.ML}
]
recipe_handler.check_ingredient_availability(ingredients)
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
