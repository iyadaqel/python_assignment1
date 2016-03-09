# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:07:33 2016

@author: begum
"""
from pylab import *

figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Credit Card', 'Cash'
fracs = [85, 15]
explode=(0, 0.05)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
               
title('Sales - Cash vs. Credit Card', bbox={'facecolor':'0.8', 'pad':5})

show()

