# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:07:33 2016

@author: begum
"""
from matplotlib import pyplot

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
labels = 'Credit Card', 'Cash'
fracs = [85, 15]
explode=(0, 0.05)

pie(fracs, explode=explode, labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90)
                # The default startangle is 0, which would start
                # the Frogs slice on the x-axis.  With startangle=90,
                # everything is rotated counter-clockwise by 90 degrees,
                # so the plotting starts on the positive y-axis.

title('Sales - Cash vs. Credit Card', bbox={'facecolor':'0.8', 'pad':5})

show()