###################################################
# Tabbed interface script
# www.sunjay-varma.com
###################################################

__doc__ = info = '''
This script was written by Sunjay Varma - www.sunjay-varma.com

This script has two main classes:
Tab - Basic tab used by TabBar for main functionality
TabBar - The tab bar that is placed above tab bodies (Tabs)

It uses a pretty basic structure:
root
-->TabBar(root, init_name) (For switching tabs)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
-->Tab    (Place holder for content)
	\t-->content (content of the tab; parent=Tab)
etc.
'''

from tkinter import *
from tkinter import ttk
BASE = RAISED
SELECTED = FLAT
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

# a base tab class
class Tab(Frame):
	def __init__(self, master, name):
		Frame.__init__(self, master)
		self.tab_name = name

# the bulk of the logic is in the actual tab bar
class TabBar(Frame):
	def __init__(self, master=None, init_name=None):
		Frame.__init__(self, master)
		self.tabs = {}
		self.buttons = {}
		self.current_tab = None
		self.init_name = init_name

	def show(self):
		self.pack(side=TOP, expand=YES, fill=X)
		self.switch_tab(self.init_name or self.tabs.keys()[-1])# switch the tab to the first tab

	def add(self, tab):
		tab.pack_forget()									# hide the tab on init

		self.tabs[tab.tab_name] = tab						# add it to the list of tabs
		b = Button(self, text=tab.tab_name, relief=BASE,	# basic button stuff
			command=(lambda name=tab.tab_name: self.switch_tab(name)))	# set the command to switch tabs
		b.pack(side=LEFT)												# pack the buttont to the left mose of self
		self.buttons[tab.tab_name] = b											# add it to the list of buttons

	def delete(self, tabname):

		if tabname == self.current_tab:
			self.current_tab = None
			self.tabs[tabname].pack_forget()
			del self.tabs[tabname]
			self.switch_tab(self.tabs.keys()[0])

		else: del self.tabs[tabname]

		self.buttons[tabname].pack_forget()
		del self.buttons[tabname]


	def switch_tab(self, name):
		if self.current_tab:
			self.buttons[self.current_tab].config(relief=BASE)
			self.tabs[self.current_tab].pack_forget()			# hide the current tab
		self.tabs[name].pack(side=BOTTOM)							# add the new tab to the display
		self.current_tab = name									# set the current tab to itself

		self.buttons[name].config(relief=SELECTED)					# set it to the selected style



if __name__ == '__main__':
    def write(x): print (x)

    root = Tk()
    #root.geometry('700x300')
    root.title("Pythunicors POS")
    bar = TabBar(root, "Sales")
    tab1= Tab(root , "Sales")

    '''
    #First tab
    label1tab1 = Label(tab1, text="Register a Sale:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)

    label2tab1 = Label(tab1, text="User ID: ", font=("Helvetica", 10), fg="black").pack()


    user_ID = Entry(tab1).pack()
    label2tab1 = Label(tab1, text="SKU/Price: ", font=("Helvetica", 10), fg="black").pack()

    SKUPrice = Entry(tab1).pack()
    label2tab1 = Label(tab1, text="Amount: ", font=("Helvetica", 10), fg="black").pack()

    Amount = Entry(tab1).pack()

    Checkbutton(tab1, text="cc").pack(side=LEFT)

    Button(tab1, text="Register", command=(lambda: write("Sale Registered"))).pack(side= RIGHT, expand=YES)
    '''
    tab1 = Tab(root, "Sales")
    RegSaleLabel = Label(tab1, text="Register a Sale: ", font=("Helvetica", 20))
    RegSaleFrame=Frame(tab1, bd=5, relief="groove")
    UserIdLabel = Label(RegSaleFrame, text="User ID:")
    UserIdEntry = Entry(RegSaleFrame, width=18)
    SKULabel = Label(RegSaleFrame, text="SKU/Price:")
    SKUEntry = Entry(RegSaleFrame, width=18)
    AmountLabel = Label(RegSaleFrame, text="Amount:")
    AmountEntry = Entry(RegSaleFrame, width=18)
    chButton=Checkbutton(RegSaleFrame, text="cc")
    RegistSale=Button(RegSaleFrame, text="Register", command=(lambda: write("Sale Registered")))

# Posicionamiento

    RegSaleLabel.grid(row=0, column=1, pady=5)
    RegSaleFrame.grid(padx=10, pady=10, row=1, column=1)
    UserIdLabel.grid(row=0, column=1)
    UserIdEntry.grid(row=0, column=2, padx=10)
    SKULabel.grid(row=1, column=1)
    SKUEntry.grid(row=1, column=2)
    AmountLabel.grid(row=2, column=1)
    AmountEntry.grid(row=2, column=2)
    RegistSale.grid(row=4, column=2, pady=8)
    chButton.grid(row=4, column=1)

    #Second Tab
    tab2 = Tab(root, "Customers")
    panes2 = PanedWindow(tab2)
    panes2.pack(fill="both", expand="yes")
    left2 = Label(panes2, text="Left Pane")
    left2.pack()
    right2 = Label(panes2, text="Right Pane")
    right2.pack()
    panes2.add(left2)
    panes2.add(right2)

    label0tab2 = Label(right2, text="List of customers:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    S = Scrollbar(right2)
    T = Text(right2, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = "  USER ID      NAME\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito """
    T.insert(END, quote)

    label1tab2 = Label(left2, text="Register a Customer:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    label2tab2 = Label(left2, text="Customer ID: ", font=("Helvetica", 10), fg="black").pack()
    user_ID = Entry(left2).pack()
    label3tab2 = Label(left2, text="Customer Name: ", font=("Helvetica", 10), fg="black").pack()
    customerName = Entry(left2).pack()
    Button(left2, text="Register new customer", command=(lambda: write("New Customer Registered"))).pack()

    '''
    Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
    txt = Text(tab2, width=25, height=10)
    txt.focus()
    txt.pack(side=LEFT, fill=X, expand=YES)
    Label(tab2, text="How are you??", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
    txt = Text(tab2, width=25, height=10)
    txt.focus()
    txt.pack(side=LEFT, fill=X, expand=YES)
    Button(tab2, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)
    '''
    #Third tab
    tab3 = Tab(root, "Product")
    panes3 = PanedWindow(tab3)
    panes3.pack(fill="both", expand="yes")
    left3 = Label(panes3, text="Left Pane")
    left3.pack()
    right3 = Label(panes3, text="Right Pane")
    right3.pack()
    panes3.add(left3)
    panes3.add(right3)

    label0tab3 = Label(right3, text="List of products:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    S3 = Scrollbar(right3)
    T3 = Text(right3, height=4, width=50)
    S3.pack(side=RIGHT, fill=Y)
    T3.pack(side=LEFT, fill=Y)
    S3.config(command=T3.yview)
    T3.config(yscrollcommand=S3.set)
    quote = "  USER ID      NAME\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito\n numerito    Nombrecito """
    T3.insert(END, quote)

    label1tab3 = Label(left3, text="Register new product:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    label2tab3 = Label(left3, text="SKU: ", font=("Helvetica", 10), fg="black").pack()
    SKU = Entry(left3).pack()
    label3tab3 = Label(left3, text="Price: ", font=("Helvetica", 10), fg="black").pack()
    Price = Entry(left3).pack()
    label4tab3 = Label(left3, text="Name: ", font=("Helvetica", 10), fg="black").pack()
    Price = Entry(left3).pack()
    Button(left3, text="Register new product", command=(lambda: write("New Product Registered"))).pack()

    #Cuarta tab
    tab4 = Tab(root, "Reports")
    MainLabel = Label(tab4, text="REPORTS ", font=("Helvetica", 30), fg='pink')


    CashFrame=Frame(tab4, bd=3, relief="groove")
    CashLabel = Label(CashFrame, text="Cash vs. CC")
    sep1=ttk.Separator(tab4,orient=VERTICAL)

    CustomerFrame=Frame(tab4, bd=3, relief="groove")
    CustomerLabel = Label(CustomerFrame, text="Customers")
    sep2=ttk.Separator(tab4,orient=VERTICAL)

    GSFrame=Frame(tab4, bd=3, relief="groove")
    GSLabel = Label(GSFrame, text="General Sales")
    sep3=ttk.Separator(tab4,orient=VERTICAL)


# Posicionamiento

    MainLabel.grid(row=0, column=6, pady=10)

    CashFrame.grid(padx=10, pady=10, row=1, column=2)
    CashLabel.grid(row=1, column=2)
    sep1.grid(column=4,row=1, rowspan=20, sticky="ns")

    CustomerFrame.grid(padx=10, pady=10, row=1, column=6)
    CustomerLabel.grid(row=1, column=6)
    sep2.grid(column=8,row=1, rowspan=20, sticky="ns")


    GSFrame.grid(padx=10, pady=10, row=1, column=10)
    GSLabel.grid(row=0, column=10)
    #sep3.grid(column=6,row=1, rowspan=20, sticky="ns")

    '''
    panes = PanedWindow(tab4)
    #ttk.Label(tab4, text='Heading Here').grid(row=1, column=3)
    ttk.Separator(tab4,orient=VERTICAL).grid(column=2, rowspan=20, sticky="ns")
   # ttk.Label(tab4, text='Heading Here').grid(row=3, column=1)
    ttk.Separator(tab4,orient=VERTICAL).grid(column=3, rowspan=20, sticky="ns")
    ttk.Label(tab4, text='Heading Here').grid(row=10, column=6)


    Label(tab4, text="CC vs. Cash", bg='black', fg='#3366ff').pack(side=TOP, fill=BOTH, expand=YES)
    txt = Text(tab4, width=50, height=20)
    txt.focus()
    txt.pack(side=LEFT, fill=X, expand=YES)
    Button(tab4, text="Get", command=(lambda: write(txt.get('1.0', END).strip()))).pack(side=BOTTOM, expand=YES, fill=BOTH)
    '''
    tab5 = Tab(root, "Settings")
    def askFolder():
        dirname = askdirectory()
        print(dirname)
      
    def askFile():
        filepath = askopenfilename()
        print(filepath)
    
    tab5label0 = Label(tab5, text="Back-up file: ", font=("Helvetica", 20))
    frametab5=Frame(tab5, bd=5, relief="groove")
    tab5label1 = Label(frametab5, text="Browse File")
    tab5label2 = Label(frametab5, text="Browse Folder")
    tab5label3 = Label(frametab5, text="Download the back-up file")
    tab5label4 = Label(frametab5, text="Change background theme")
    Button1=Button(frametab5, text="Browse File", command=askFile)
    Button2=Button(frametab5, text="Browse Folder", command=askFolder)
    Button3=Button(frametab5, text="Download")
    Button4=Button(frametab5, text="Change the Theme")
    tab5label0.grid(row=0, column=1, pady=5)
    frametab5.grid(padx=10, pady=10, row=1, column=1)
    tab5label1.grid(row=1, column=1)
    tab5label2.grid(row=2, column=1)
    tab5label3.grid(row=3, column=1)
    tab5label4.grid(row=4, column=1)
    Button1.grid(row=1, column=3)
    Button2.grid(row=2, column=3)
    Button3.grid(row=3, column=3)
    Button4.grid(row=4, column=3)
    
    bar.add(tab1)                   # add the tabs to the tab bar
    bar.add(tab2)
    bar.add(tab3)
    bar.add(tab4)
    bar.add(tab5)


    bar.show()
    root.mainloop()
