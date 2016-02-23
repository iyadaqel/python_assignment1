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
               def searchSKU (sSKU):
                   for i in range (Product.total):
                       if ((Product.productListita[i].find(sSKU))!= (-1)):
                           print(Product.productListita[i])
                       else:
                           print("The SKU number doesn´t exist")

               def __str__(self):
                              rep ="#SKU:" + self.SKU + " #Price:"+ self.price
                              return rep
