class Product (object):
               total=0
               productListita=[]

               def __init__ (self, SKU, price):
                              Product.total+=1
                              self.SKU=SKU
                              self.price=price
                              Product.productListita.append(self)


               @staticmethod
               def totals():
                              print("The total number of products is", Product.total)

               @staticmethod
               def productList():
                   for i in range (Product.total):
                       print(Product.productListita[i])

               @staticmethod
               def searchSKU(sSKU):
                   a=0
                   for i in range (Product.total):
                       comparar=str(Product.productListita[i])
                       if ((comparar.find(sSKU))!= (-1)):
                           print(Product.productListita[i])
                           a=1
                   if a==0:
                       print("The SKU number "+ sSKU + " does not exist")


               def __str__(self):
                              rep ="#SKU:" + self.SKU + " #Price:"+ self.price
                              return rep

