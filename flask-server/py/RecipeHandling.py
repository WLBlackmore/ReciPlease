import csv
from collections import defaultdict
from py.FoodProduct import FoodProduct, Unit

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
    def getAllOfType(self, foodType):
        return [product for product in self.products.values() if product.foodType == foodType]
        

   
    # Cost for SINGLE ingredient
    def getMinimumProductsForIngredient(self, foodType, desiredAmount):
        # Get products in descending order
        foodTypeArr = sorted(self.getAllOfType(foodType), key=lambda x: x.quantity, reverse=True)

        desiredAmount = int(desiredAmount)
        total = 0
        toBuy = []

        if len(foodTypeArr) == 1:
            counter = 0
            while (total <= desiredAmount):
                counter += 1
                total += foodTypeArr[0].quantity

            toBuy.append((foodTypeArr[0].productName, counter))

            return toBuy


        for i in range(len(foodTypeArr)):
            counter = 0
            while total + foodTypeArr[i].quantity <= desiredAmount:
                counter += 1
                total += foodTypeArr[i].quantity

            if counter > 0:
                toBuy.append((foodTypeArr[i].productName, counter))

            if (total >= desiredAmount): break
        
        if total < desiredAmount:
            smallest_item = foodTypeArr[-1]
            additional_units =  int(-(- (desiredAmount - total) // smallest_item.quantity))
            toBuy.append((smallest_item.productName, additional_units))
        
        return toBuy   

    def getMinimumProductsForRecipe(self, recipe):
        products = []
        for ingredient in recipe:
            prods = self.getMinimumProductsForIngredient(ingredient[0], ingredient[1])
            for prod in prods:
                products.append(prod)

        return products
    
    def getPriceOfProductList(self, products):
        return sum(prod.price for prod in products)

        

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


#handler = RecipeHandler('ReciPlease/flask-server/py/Grocery Items Dataset - Sheet1.csv')
#print(handler.optimizeCostForIngredient("Eggs", 3500))

    



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
