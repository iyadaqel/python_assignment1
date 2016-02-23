class Product (object):
               total=0
               __productListita=[]

               def __init__ (self, SKU, price):
                              Product.total+=1
                              self.__SKU=SKU
                              self.__price=price
                              Product.__productListita.append(self)


               @staticmethod
               def totals():
                              print("The total number of products is", Product.total)

               @staticmethod
               def productList():
                   for i in range (Product.total):
                       print(Product.__productListita[i])

               @staticmethod
               def searchSKU(sSKU):
                   a=0
                   for i in range (Product.total):
                       comparar=str(Product.__productListita[i])
                       if ((comparar.find(sSKU))!= (-1)):
                           print(Product.__productListita[i])
                           a=1
                   if a==0:
                       print("The SKU number "+ sSKU + " does not exist")


               def __str__(self):
                              rep ="#SKU:" + self.__SKU + " #Price:"+ self.__price
                              return rep

