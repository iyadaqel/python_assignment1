class Sale(object):
    totalDailySales = 0
    saleList=[]

    def __init__(self,product,PayMethod,Customer):
        self.product = product
        self.PayMethod = PayMethod
        self.Customer = Customer
        Sale.totalDailySales += 1
        Sale.saleList.append(self)


    def getTotalDailySales():
        print("The total daily sales are", Sale.totalDailySales)

    def getSaleList():
        for i in range (len(Sale.saleList)):
            print(Sale.saleList[i])



        
sale1=Sale("kk","cc","99")
print
print(sale1.product, sale1.PayMethod, sale1.Customer)
Sale.getTotalDailySales()
print(len(Sale.saleList))
print(Sale.saleList[0])
Sale.getSaleList()
