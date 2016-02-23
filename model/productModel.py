class Product (object):
               total=0

               def __init__ (self, SKU, price):
                              Product.total+=1
                              self.SKU=SKU
                              self.price=price


               @staticmethod
               def totals():
                              print("The total number of products is", Product.total)

               def __str__(self):
                              rep ="#SKU: " + self.SKU + "#Price: "+ self.price
                              return rep

               def getPrice (self):
                              return self.price
