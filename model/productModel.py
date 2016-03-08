import sqlite3
class Product (object):
    total=0
    products={}

    def __init__ (self, SKU, name, price):
        Product.total+=1
        self.SKU=SKU
        self.name = name
        self.price=price
        Product.products[SKU] = self
        Product.insertIntoDB(self)

    @staticmethod
    def totals():
        print("The total number of products is", Product.total)

    @staticmethod
    def getProductList():
        productsFromDB={}
        conn = sqlite3.connect('../pos.db')
        rows= conn.execute("SELECT * FROM PRODUCT")
        for row in rows:
            productsFromDB[row[0]] = Product.getProductBySKU(row[0])
        return productsFromDB
        #return Product.products


    def __str__(self):
        rep ="#SKU:" + str(self.SKU) + " #Price:"+ str(self.price)
        return rep

    def getProductBySKU(productSKU):
        productSKU = int(productSKU)
        if(productSKU in Product.products):
            return Product.products[productSKU]
        else:
            return False

    def insertIntoDB(self):
        conn = sqlite3.connect('../pos.db')
        conn.execute("INSERT INTO PRODUCT (SKU,NAME,PRICE) VALUES ('" + str(self.SKU) + "', '" + self.name + "','" + str(self.price) + "')")
        conn.commit()
        conn.close()