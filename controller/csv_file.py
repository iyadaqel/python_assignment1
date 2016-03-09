# """
# Created on Mon Mar  7 23:23:29 2016
#
# @author: begum
# """
import sqlite3 as lite
import csv

def downloadAllFiles():

    con = lite.connect('../pos.db')

    #SALES
    data = con.execute("SELECT * FROM SALE")
    with open('../sales.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','payMethod','customerID','productID','total','date'])
        writer.writerows(data)


    #PRODUCTS
    data = con.execute("SELECT * FROM PRODUCT")
    with open('../product.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','SKU'])
        writer.writerows(data)


    data = con.execute("SELECT * FROM CUSTOMER")
    with open('../customer.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name'])
        writer.writerows(data)



'''
    f = open('sales.csv', 'w')
    print >> f, "id,primaryKey,payMethod,customerID,productID,total,date"
    for row in data:
      print >> f, row

    #PRODUCT
    con.execute("SELECT * FROM PRODUCT")
    data=con.fetchone()

    f = open('product.csv', 'w')
    print >> f, "id,primaryKey,payMethod,customerID,productID,total,date"
    for row in data:
      print >> f, row


    #Customers
    con.execute("SELECT * FROM PRODUCT")
    data=con.fetchone()

    f = open('customers.csv', 'w')
    print >> f, "id,primaryKey,payMethod,customerID,productID,total,date"
    for row in data:
      print >> f, row


    f.close()

'''

