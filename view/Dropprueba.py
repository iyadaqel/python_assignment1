from tkinter import *
from matplotlib import pyplot as plt

root = Tk()


labels = 'Cash', 'Credit Card'
sizes = [15, 85]
colors = ['lightskyblue', 'lightcoral']
explode = (0, 0.1)

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')

plt.show()

root.mainloop()




