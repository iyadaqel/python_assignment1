from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale
from controller import pos
import sqlite3
import os
from configparser import  ConfigParser
import config


#Create Config file if its not there
if not os.path.exists("settings.ini"):
    config.createConfig()


# read some values from the config
def intialize():
    print("inside the intialize function")
    #Get The configurations
    config = ConfigParser()
    config.read("settings.ini")
    dbURL = config.get("database", "url")
    isDBInstalled = int(config.get("firsttime", "db-installed"))
    if(isDBInstalled == 0):
        conn = sqlite3.connect(dbURL)
        print(conn)
        print("installing because first time")
        conn.execute(''' DROP TABLE  IF EXISTS PRODUCT; ''')
        conn.execute(''' DROP TABLE  IF EXISTS CUSTOMER; ''')
        conn.execute(''' DROP TABLE  IF EXISTS SALE; ''')
        conn.execute('CREATE  TABLE PRODUCT (SKU CHAR(50) PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PRICE INT NOT NULL);')
        conn.execute('CREATE  TABLE CUSTOMER  (customerID CHAR(50) PRIMARY KEY     NOT NULL, customerName  TEXT  NOT NULL);')
        conn.execute('CREATE  TABLE SALE (ID INTEGER PRIMARY KEY AUTOINCREMENT, paymethod CHAR(50) NOT NULL, customerID CHAR(50) NOT NULL, productID CHAR(50) NOT NULL, total    INT NOT NULL ,date CHAR(50));')
        conn.close()


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

        #Changing the Value of the firsTime
        config.set("firsttime", "db-installed" , "1")


        with open("settings.ini", "w") as config_file:
            config.write(config_file)



