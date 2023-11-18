from enum import Enum
import csv

class Unit(Enum):
    G = "g"
    ML = "mL"
    SINGLE = ()

class FoodProduct:
    def __init__(self, food_type, product_name, price, quantity, unit):
        self.foodType = food_type
        self.productName = product_name
        self.price = price
        self.quantity = quantity
        self.unit = unit

    def GetPricePerUnit(self):
        return self.price / self.quantity
