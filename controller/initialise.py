from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale
import controller.pos as pos

defaultCustomer = Customer(0,"Customer We dont know")
Customer(1,"Monica")
Customer(2,"Iyad")
Customer(3,"Karmen")
Customer(4,"Begum")

p1= Product(123 , "Stripes Shirt" ,  10)
p2= Product(1234 , "Plain Shirt with Contrasting Collar" , 20)
p3= Product(12345 ,"zabatooos i love the word zabatos btw " , 30)


pos.addSale(customerID=1 , productSKU = 123 , cc=0)
pos.addSale(customerID=2 , productSKU = 1234 , cc=1)
pos.addSale(customerID=2 , productSKU = 12345 , cc=1)
pos.addSale(customerID=2 , productSKU = 1234 , cc=0)
pos.generateCCReport()
pos.generateCustomerReport()
