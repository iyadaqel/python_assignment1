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
        conn = sqlite3.connect('../pos.db')
        rows= conn.execute("SELECT * FROM PRODUCT")
        return rows
        #return Product.products


    def __str__(self):
        rep ="#SKU:" + str(self.SKU) + " #Price:"+ str(self.price)
        return rep

    def getProductBySKU(productSKU):
        conn = sqlite3.connect('../pos.db')
        cursor = conn.cursor()
        query = "SELECT * FROM PRODUCT WHERE SKU =" + str(productSKU)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return row

    def insertIntoDB(self):
        conn = sqlite3.connect('../pos.db')
        conn.execute("INSERT INTO PRODUCT (SKU,NAME,PRICE) VALUES ('" + str(self.SKU) + "', '" + self.name + "','" + str(self.price) + "')")
        conn.commit()
        conn.close()