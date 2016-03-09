import matplotlib , numpy
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import *


def showPieChart():

        labels = 'Cash', 'Credit Card'
        sizes = [15, 85]
        colors = ['lightskyblue', 'lightcoral']
        explode = (0, 0.1)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)

        plt.axis('equal')
        plt.title("Hola")

        plt.show()
        return (plt)
root = Tk()


eti=Label(root, text="hola", font=("Helvetica", 30))
eti.grid(column=8,row=1, rowspan=20)
tartita=showPieChart()
tartita.grid(root)
#canvas = FigureCanvasTkAgg(tartita, master=root)
#canvas.show()

#canvas.get_tk_widget().grid(row=2, column=6)
root.mainloop()




