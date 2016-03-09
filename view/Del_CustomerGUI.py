import tkinter as tk
from tkinter import ttk

win_root = tk.Tk()
win_root.title("Add a new customer")
win_root.resizable(width=True , height=False)

#Name
labelName = ttk.Label(win_root , text="Name:" , font=("Helevetica",10), foreground="black")
labelName.grid(column=0 , row=1)

name = tk.StringVar()
nameCustomer = ttk.Entry(win_root , textvariable = name)
nameCustomer.grid(column=1 , row=1)


#ID
labelID = ttk.Label(win_root , text="ID:" , font=("Helevetica",10), foreground="black")
labelID.grid(column=0 , row=2)

id = tk.StringVar()
idCustomer = ttk.Entry(win_root , textvariable = id)
idCustomer.grid(column=1 , row=2)

#Adding a Button
action = ttk.Button(win_root, text="Add")
action.grid(column=1, row=3)
action = ttk.Button(win_root, text="Cancel")
action.grid(column=2 , row=3)

#Message box for checking existing users before adding new one
def _msgBox():
    print(mBox.showinfo("Successfully added!"))
def _warningBox():
    print(mBox.askyesno('The customer already exists!'))




win_root.mainloop()
