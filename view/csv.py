"""
Created on Mon Mar  7 23:23:29 2016

@author: begum
"""
import sqlite3 as lite

con = lite.connect('pos.db')
print('Successfully Connected!')
cur = con.cursor()
cur.execute("SELECT * FROM SALE")
data=cur.fetchone()

f = open('sales.csv', 'w')
print >> f, "id,primaryKey,payMethod,customerID,productID,total,date"
for row in data:
  print >> f, row
f.close()