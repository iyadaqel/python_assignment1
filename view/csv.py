# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:23:29 2016

@author: begum
"""
import sqlite3

conn = sqlite3.connect('pos.db')
conn.text_factory = str ## my current (failed) attempt to resolve this
cur = conn.cursor()
data = cur.execute("SELECT * FROM SALE")

f = open('sales.csv', 'w')
print >> f, "id,primaryKey,payMethod,customerID,productID,total,date"
for row in data:
  print >> f, row
f.close()