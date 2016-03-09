import matplotlib , numpy
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pylab import pie, figure, axes
from tkinter import *


def creografico():
    # make a square figure and axes
    p=figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Cash', 'Credit Card'
    fracs = [15, 85]
    explode=(0, 0.1)

    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90, colors= ["#E13F29", "#D69A80"])
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.

    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})


    return p

tab4 = Tk()

eti=Label(tab4, text="hola", font=("Helvetica", 30))
eti.grid(column=8,row=1, rowspan=20)
tartita=creografico()
canvas = FigureCanvasTkAgg(tartita, master=tab4)
canvas.show()

canvas.get_tk_widget().grid(row=2, column=6)
tab4.mainloop()