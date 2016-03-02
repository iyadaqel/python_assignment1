import tkinter as tk
from tkinter import ttk
from tkinter import *

root = Tk()
menubar = Menu(root)
v=tk.StringVar()
v.set("New Textlñefjks.zd,xv")
rootWindowlabel1 = ttk.Label(root , textvariable=v , font=("Helevetica",20), foreground="black")
rootWindowlabel1.grid()

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def hello():
   # root.quit()#NO funciona esta puta mierda

    win_root = tk.Tk()
    win_root.title("Python GUI")
    win_root.resizable(width=True , height=False)

    label1 = ttk.Label(win_root , text="Register a Sale:" , font=("Helevetica",20), foreground="black")
    label1.grid()

    # FIRST ROW
    labelSales = ttk.Label(win_root , text="Sales Amount:" , font=("Helevetica",10), foreground="black")
    labelSales.grid(column=0 , row=1)

    sale = tk.StringVar()
    salesAmount = ttk.Entry(win_root , textvariable = sale)
    salesAmount.grid(column=1 , row=1)



    # SECOND ROW
    labelSKU = ttk.Label(win_root , text="SKU Number:" , font=("Helevetica",10), foreground="black")
    labelSKU.grid(column=0 , row=2)

    sku = tk.StringVar()
    saleSKU = ttk.Entry(win_root , textvariable = sku)
    saleSKU.grid(column=1 , row=2)



    # THIRD ROW
    labelID = ttk.Label(win_root , text="SALE ID :" , font=("Helevetica",10), foreground="black")
    labelID.grid(column=0 , row=3)

    id = tk.StringVar()
    saleID = ttk.Entry(win_root , textvariable = id)
    saleID.grid(column=1, row=3)





    #forth ROW

    check = tk.IntVar()
    check1 = tk.Checkbutton(win_root, text="cc" , variable=check )
    check1.grid(column=0, row=4)

    # Adding a Button
    mensajito = " #ID: " + id.get() + " #SKU: " + sku.get() + " #Sales Amount: " + sale.get()

    action = ttk.Button(win_root, text="Regiester!" , command=msgBox(mensajito))
    action.grid(column=1 , row=4)

    win_root.mainlop()



def msgBox(strng):
        print("inside mensajito box")
        v.set(strng)
        #mBox.showinfo('Python Messagen Info Box', str(saleID))



#Cosa delplegable del primer boton del  menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Sale", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit (Iyad aguafiestas)", command=root.quit)

#First cosa del menu. Abrira el desplegable definido arriba
menubar.add_cascade(label="Sales", menu=filemenu)


#Cosa desplegable del segundo boton
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Show Customers", command=hello)
editmenu.add_command(label="Add New Customer", command=donothing)

#Second cosa del menu
menubar.add_cascade(label="Customers", menu=editmenu)

#Cosa desplegable del tercer boton
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Credit Card vs. Cash", command=donothing)
helpmenu.add_command(label="By User", command=donothing)

#Tercer boton
menubar.add_cascade(label="Report", menu=helpmenu)


#Cosa desplegable del cuartor boton
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Show products", command=donothing)

#Cuarto boton
menubar.add_cascade(label="SKU", menu=helpmenu)

#Cosa desplegable del quinto boton
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Save sales", command=donothing)

#Quinto boton
menubar.add_cascade(label="Back up", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()