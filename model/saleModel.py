import time
import sqlite3

class Sale(object):
    totalDailySales = 0
    saleList=[]

    def __init__(self,product,paymethod,customer ,total):
        self.product = product
        self.paymethod = paymethod
        self.customer = customer
        self.total = total
        self.date = time.strftime("%d/%m/%Y %H:%M:%S")
        Sale.totalDailySales+=1
        Sale.saleList.append(self)
        Sale.insertIntoDB(self)

    def getTotalDailySales():
        print("The total daily sales are", Sale.totalDailySales)

    def getSaleList():
        conn = sqlite3.connect('../pos.db')
        rows= conn.execute("SELECT * FROM SALE")
        return rows
        #return Sale.saleList

    def __str__(self):
        return  ("Customer: " + self.customer.customerName + " bought " +  str(self.product.price) + "€ and paid by "  + self.paymethod  + " at " + self.date)


    def insertIntoDB(self):
        conn = sqlite3.connect('../pos.db')
        paymethod= str(self.paymethod)
        customerID = str(self.customer[0])
        productID = str(self.product[0])
        total = str(self.total)

        conn.execute("INSERT INTO SALE (ID, paymethod, customerID , productID , total) VALUES (NULL,'" +
                 paymethod + "','" + customerID + "','" + productID + "','" + total + "')")
        conn.commit()
        conn.close()

