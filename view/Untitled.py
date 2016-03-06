import ttk, tkinder

mainWindow = Tkinter.Tk()

mainFrame = Tkinter.Frame(mainWindow, name = 'main-frame')
mainFrame.pack(fill = Tkinter.BOTH) # fill both sides of the parent

nb = ttk.Notebook(mainFrame, name = 'nb')
nb.pack(fill = Tkinter.BOTH, padx=2, pady=3) # fill "master" but pad sides

tab1Frame = Tkinter.Frame(nb, name = 'tab1')
Tkinter.Label(tab1Frame, text = 'this is tab 1').pack(side = Tkinter.LEFT)
nb.add(tab1Frame, text = 'tab 1')

tab2Frame = Tkinter.Frame(nb, name = 'tab2')
Tkinter.Label(tab2Frame, text = 'this is tab 2').pack(side = Tkinter.LEFT)
nb.add(tab2Frame, text = 'tab 2')

nb.select(tab2Frame) # <-- here's what you're looking for

mainWindow.mainloop()
