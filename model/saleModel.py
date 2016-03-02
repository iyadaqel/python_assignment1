class Sale(object):
    totalDailySales = 0
    saleList=[]

    def __init__(self,Product,PayMethod,Customer):
        self.product = Product
        self.PayMethod = PayMethod
        self.Customer = Customer
        Sale.totalDailySales+=1
        Sale.saleList.append(self)


    def getTotalDailySales():
        print("The total daily sales are", Sale.totalDailySales)

    def getSaleList():
        for i in range (Sale.totalDailySales):
                       print(Sale.saleList[i].product, Sale.saleList[i].PayMethod, Sale.saleList[i].Customer)

    
        
#sale1=Sale("kk","cc","99")
#Sale.getTotalDailySales()
#Sale.getSaleList()
