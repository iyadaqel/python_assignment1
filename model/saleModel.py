import time


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

    def getTotalDailySales():
        print("The total daily sales are", Sale.totalDailySales)

    def getSaleList():
        return Sale.saleList

    def __str__(self):
        return  ("Customer: " + self.customer.customerName + " bought " +  str(self.product.price) + "€ and paid by "  + self.paymethod  + " at " + self.date)

