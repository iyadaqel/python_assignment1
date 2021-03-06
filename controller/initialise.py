from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale
from controller import pos
import sqlite3
from configparser import ConfigParser
import config as configure

import os

def intialize():
    if not os.path.exists("settings.ini"):
        configure.createConfig()

    config = ConfigParser()
    config.read("settings.ini")


    dbPath = config.get("database", "url")
    isDBInstalled = config.get("firsttime", "db-installed")
    if(isDBInstalled == "0" ):
        conn = sqlite3.connect(dbPath)
        conn.execute(''' DROP TABLE  IF EXISTS PRODUCT; ''')
        conn.execute(''' DROP TABLE  IF EXISTS CUSTOMER; ''')
        conn.execute(''' DROP TABLE  IF EXISTS SALE; ''')


        conn.execute('CREATE  TABLE PRODUCT (SKU CHAR(50) PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PRICE INT NOT NULL);')
        conn.execute('CREATE  TABLE CUSTOMER  (customerID CHAR(50) PRIMARY KEY     NOT NULL, customerName  TEXT  NOT NULL);')
        conn.execute('CREATE  TABLE SALE (ID INTEGER PRIMARY KEY AUTOINCREMENT, paymethod CHAR(50) NOT NULL, customerID CHAR(50) NOT NULL, productID CHAR(50) NOT NULL, total    INT NOT NULL ,sdate DATETIME DEFAULT CURRENT_TIMESTAMP);')

        defaultCustomer = Customer(0,"Default Customer")
        Customer(1,"Monica")
        Customer(2,"I")
        Customer(3,"Carmen")
        Customer(4,"Begum")

        p1= Product(123 , "Stripes Shirt" ,  10)
        p2= Product(1234 , "Plain Shirt with Contrasting Collar" , 20)
        p3= Product(12345 ,"zapatooos i love the word zapatos btw " , 30)

        pos.addSale(customerID=1 , productSKU = 123 , cc=0 , amount=1)
        pos.addSale(customerID=2 , productSKU = 1234 , cc=1 , amount=1)
        pos.addSale(customerID=2 , productSKU = 12345 , cc=1 , amount=1)
        pos.addSale(customerID=2 , productSKU = 1234 , cc=0 , amount=1)
        conn.close()

        config.set("firsttime", "db-installed" , "1")

        # write changes back to the config file
        with open("settings.ini", "w") as config_file:
            config.write(config_file)

