import tkinter
mainWindow = tkinter.Tk()

mainFrame = tkinter.Frame(mainWindow, name = 'main-frame')
mainFrame.pack(fill = tkinter.BOTH) # fill both sides of the parent

nb = ttk.Notebook(mainFrame, name = 'nb')
nb.pack(fill = tkinter.BOTH, padx=2, pady=3) # fill "master" but pad sides

tab1Frame = tkinter.Frame(nb, name = 'sales')
tkinter.Label(tab1Frame, text = 'sales').pack(side = tkinter.LEFT)
nb.add(tab1Frame, text = 'sales')

tab2Frame = tkinter.Frame(nb, name = 'customer')
tkinter.Label(tab2Frame, text = 'customer').pack(side = tkinter.LEFT)
nb.add(tab2Frame, text = 'customer')

tab3Frame = tkinter.Frame(nb, name = 'products')
tkinter.Label(tab2Frame, text = 'products').pack(side = tkinter.LEFT)
nb.add(tab2Frame, text = 'products')

tab4Frame = tkinter.Frame(nb, name = 'report')
tkinter.Label(tab2Frame, text = 'report').pack(side = tkinter.LEFT)
nb.add(tab2Frame, text = 'report')

tab5Frame = tkinter.Frame(nb, name = 'report')
tkinter.Label(tab2Frame, text = 'report').pack(side = tkinter.LEFT)
nb.add(tab2Frame, text = 'report')

nb.select(tab2Frame) # <-- here's what you're looking for

mainWindow.mainloop()
