import math
import random
import pandas as pd

class Product:
    def __init__(self, prodID, prodName, prodCategory, prodPrice):
        self.prodID = prodID
        self.prodName = prodName
        self.prodCategory = prodCategory
        self.prodPrice = prodPrice

    def displayInfoAndReturnPrice(self):
        print(f"{self.prodName}: {self.prodPrice}")
        return self.prodPrice


class ElectronicProduct(Product):
    def __init__(self, prodID, prodName, prodCategory, prodPrice, warrType, warrPricePercent=0):
        super().__init__(prodID, prodName, prodCategory, prodPrice)
        self.warrantyType = warrType
        self.warrantyPricePercent = warrPricePercent
        self.warrantyPrice = round(self.prodPrice + (self.prodPrice * self.warrantyPricePercent), 2)

    def displayInfoAndReturnPrice(self):
        print(f"{self.prodName}: {self.prodPrice}. Price including {self.warrantyType}: {self.warrantyPrice}")
        return self.warrantyPrice


class Order:
    def __init__(self, orderID, prodList):
        self.orderID = orderID
        self.orderList = prodList
        self.totalPrice = 0

    def addToOrder(self, listProductsToAdd, numProductsToAdd):
        for product in range(numProductsToAdd):
            totalProducts = len(listProductsToAdd)
            randIndex = random.randint(0, totalProducts-1)
            self.orderList.append(listProductsToAdd[randIndex])
            print(listProductsToAdd)
        print(f"Added {numProductsToAdd} to order {self.orderID}")

    def showAllProductsAndTotal(self):
        print(f"Order #{self.orderID} has the following products:")
        for product in self.orderList:
            print(f"\t{product.displayInfoAndReturnPrice()}")


df = pd.read_excel("product_data.xlsx")
productList = []
print(df)
for index, row in df.iterrows():
    productID = row["Product_ID"]
    productName = row["Product_Name"]
    productCategory = row["Product_Category"]
    productPrice = row["Price"]
    warrantyType = row["Warranty_Type"]
    warrantyPricePercent = row["Warranty_Price_Percent"]
    if isinstance(warrantyType, str):
        productList.append(
            ElectronicProduct(productID, productName, productCategory, productPrice, warrantyType, warrantyPricePercent)
        )
        print("Has warranty")
    else:
        productList.append(Product(productID, productName, productCategory, productPrice))
        print("has no warranty")

print()
for product in productList:
    product.displayInfoAndReturnPrice()

orderList = []
for order in range(5):
    print("\n")
    orderToAdd = Order(random.randint(1, 50000), [])
    orderToAdd.addToOrder(productList, random.randint(1, 5))
    orderToAdd.showAllProductsAndTotal()
    orderList.append(orderToAdd)
