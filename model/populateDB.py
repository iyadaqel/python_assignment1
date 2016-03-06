from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale
import controller.pos as pos


import sqlite3

conn = sqlite3.connect('pos.db')


conn.execute(''' DROP TABLE  IF EXISTS PRODUCT; ''')
conn.execute(''' DROP TABLE  IF EXISTS CUSTOMER; ''')
conn.execute(''' DROP TABLE  IF EXISTS SALE; ''')


conn.execute('CREATE  TABLE PRODUCT (SKU CHAR(50) PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PRICE INT NOT NULL, ADDRESS CHAR(50));')
conn.execute('CREATE  TABLE CUSTOMER  (customerID CHAR(50) PRIMARY KEY     NOT NULL, customerName  TEXT  NOT NULL);')
conn.execute('CREATE  TABLE SALE (ID INTEGER PRIMARY KEY AUTOINCREMENT, paymethod CHAR(50) NOT NULL, customerID CHAR(50) NOT NULL, productID CHAR(50) NOT NULL, total    INT NOT NULL ,date CHAR(50));')



conn.execute("INSERT INTO CUSTOMER (customerID,customerName) \
      VALUES (1, 'IYAD')");

conn.execute("INSERT INTO CUSTOMER (customerID,customerName) \
      VALUES (2, 'Karmen')");

conn.execute("INSERT INTO CUSTOMER (customerID,customerName) \
      VALUES (3, 'Begum')");

conn.execute("INSERT INTO CUSTOMER (customerID,customerName) \
      VALUES (4, 'Monice')");


#ADDING DEFAULTS

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


sales = Sale.getSaleList()
for sale in sales:
    paymethod= str(sale.paymethod)
    customerID = str(sale.customer.customerID)
    productID = str(sale.product.SKU)
    total = str(sale.total)
    conn.execute("INSERT INTO SALE (ID, paymethod, customerID , productID , total) VALUES (NULL,'" +
                 paymethod + "','" + customerID + "','" + productID + "','" + total + "')")


sales = conn.execute("SELECT * FROM SALE")
for sale in sales:

    print("SALE IS: " + str(sale[0]) + " " +  str(sale[1])+  " " + str(sale[2])+ " " + str(sale[3])+ " " + str(sale[4]))


conn.close()