class Product (object):
               total=0
               products={}

               def __init__ (self, SKU, name, price):
                              Product.total+=1
                              self.SKU=SKU
                              self.name = name
                              self.price=price
                              Product.products[SKU] = self


               @staticmethod
               def totals():
                              print("The total number of products is", Product.total)

               @staticmethod
               def getProductList():
                   return Product.products


               def __str__(self):
                              rep ="#SKU:" + str(self.SKU) + " #Price:"+ str(self.price)
                              return rep

               def getProductBySKU(productSKU):
                   productSKU = int(productSKU)
                   if(productSKU in Product.products):
                       return Product.products[productSKU]
                   else:
                       return False




'''
               def searchSKU(sSKU):
                   a=0
                   for i in range (Product.total):
                       comparar=str(Product.__productListita[i])
                       if ((comparar.find(sSKU))!= (-1)):
                           print(Product.__productListita[i])
                           a=1
                   if a==0:
                       print("The SKU number "+ sSKU + " does not exist")
'''