import matplotlib, numpy, sys
matplotlib.use('TkAgg')
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from view.Tab import Tab
from view.Tab import TabBar
from controller import pos as pos
from controller import initialise as i

i.intialize()
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pylab import pie, figure, axes


if __name__ == '__main__':
    def write(x): print (x)


    def addSale():
        #Don't forget to check for the values before you submit

        customerID = customerNamesVar.get()
        SKU = varSKU.get()
        amount = AmountEntry.get()
        cc = ccButtonValue.get()
        result = pos.addSale(customerID ,SKU , cc , amount)
        if(result['error']==True):
            resultLabel.configure(fg="red" , text=result['message'])
        else:
            resultLabel.configure(fg="green" , text=result['message'])

    def addCustomer():
        customerID = customerIDTab2.get()
        name = customerNameTab2.get()
        result = pos.addCustomer(customerID,name)
        if(result['error']==True):
            customerResultLabel.configure(fg="red" , text=result['message'])
        else:
            customerResultLabel.configure(fg="green" , text=result['message'])
            quote = pos.getAllCustomersNames()
            T.delete('1.0', END)
            T.insert(END,quote)

    def addProduct():
        SKU = SKUEntryThirdTab.get()
        name= productNameEntryThirdTab.get()
        price =priceEntryThirdTab.get()
        result = pos.addProduct(SKU, name , price)
        if(result['error']==True):
            productResultLabel.configure(fg="red" , text=result['message'])
        else:
            productResultLabel.configure(fg="green" , text=result['message'])
            quote = pos.getAllProductsNames()
            T3.delete('1.0', END)
            T3.insert(END,quote)



    #Defining the window and the Sale
    root = Tk()
    root.title("PYTHUNICORNS POS")
    #root.configure(background='pink')
    bar = TabBar(root, "Sales")
    tab1 = Tab(root, "Sales")
    tab1.grid(row=0, column=3, columnspan=2,sticky=N+S+E+W)



    #First Tab
    RegSaleLabel = Label(tab1, text="Register a Sale: ", font=("Helvetica", 20))
    RegSaleFrame=Frame(tab1, bd=5, relief="groove", width=1000, height=1000)
    #RegSaleFrame.config(bg="red")
    UserIdLabel = Label(RegSaleFrame, text="User ID:")
    #Drop down list for users
    customerNamesVar = StringVar()
    choices = pos.getOnlyCustomersNames()
    customerNamesVar.set(choices[0])
    option = OptionMenu(RegSaleFrame, customerNamesVar, *choices)
    option.grid(row=0, column=2, sticky=N+S+E+W)

    SKULabel = Label(RegSaleFrame, text="SKU:")
    #Drop down list for SKU
    varSKU = StringVar(tab1)
    # initial value
    choicesSKU = pos.getOnlyProductsNamesAndSKU()
    varSKU.set(choicesSKU[0])
    optionSKU = OptionMenu(RegSaleFrame, varSKU, *choicesSKU)
    optionSKU.grid(row=1, column=2, sticky=N+S+E+W)

    AmountLabel = Label(RegSaleFrame, text="Amount(x):")
    AmountEntry = Entry(RegSaleFrame, width=18)
    resultLabel = Label(RegSaleFrame, text="")
    ccButtonValue = IntVar()
    chButton=Checkbutton(RegSaleFrame, text="cc" , variable=ccButtonValue)
    RegistSale=Button(RegSaleFrame, text="Register", command=addSale)

# Positions of the First Tab
    RegSaleLabel.grid(row=0, column=0, columnspan=2,sticky=N+S+E+W)
    RegSaleFrame.grid(row=1, column=1, sticky=N+S+E+W)
    UserIdLabel.grid(row=0, column=1, sticky=N+S+E+W)
    #UserIdEntry.grid(row=0, column=2, sticky=N+S+E+W)
    SKULabel.grid(row=1, column=1, sticky=N+S+E+W)
    #SKUEntry.grid(row=1, column=2, sticky=N+S+E+W)
    AmountLabel.grid(row=2, column=1, sticky=N+S+E+W)
    AmountEntry.grid(row=2, column=2, sticky=N+S+E+W)
    resultLabel.grid(row=4 , column=1, sticky=N+S+E+W)
    RegistSale.grid(row=5, column=2, sticky=N+S+E+W)
    chButton.grid(row=5, column=1, sticky=N+S+E+W)


    #SECOND TAB
    tab2 = Tab(root, "Customers")

    frame1t2=Frame(tab2, bd=3, relief="groove")
    label0tab2 = Label(frame1t2, text="List of customers:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    S = Scrollbar(frame1t2)
    T = Text(frame1t2, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = pos.getAllCustomersNames()
    T.insert(END, quote)
    sep1t2=ttk.Separator(tab2,orient=VERTICAL)

    frame2t2=Frame(tab2, bd=3, relief="groove")
    label1tab2 = Label(frame2t2, text="Register a Customer:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    label2tab2 = Label(frame2t2, text="Customer ID: ", font=("Helvetica", 10), fg="black").pack()
    customerIDTab2 = Entry(frame2t2 , text="")
    customerIDTab2.pack()
    label3tab2 = Label(frame2t2, text="Customer Name: ", font=("Helvetica", 10), fg="black")
    customerNameTab2 = Entry(frame2t2)
    label3tab2.pack()
    customerNameTab2.pack()
    customerResultLabel = Label(frame2t2, text="")
    customerResultLabel.pack()
    Button(frame2t2, text="Register new customer", command=addCustomer).pack()


# Position

    frame1t2.grid(row=1, column=2)
    #label0tab2.grid(row=1, column=2)
    #When it works position rest of elements
    sep1t2.grid(column=4,row=1, rowspan=20)

    frame2t2.grid(padx=10, row=1, column=6)
    #customerName.grid(row=1,column=2)
    #label1tab2.grid(row=1, column=6)
    #when it works position rest of elements


    #Third tab
    tab3 = Tab(root, "Product")

    frame1t3=Frame(tab3, bd=3, relief="groove")
    label0tab3 = Label(frame1t3, text="List of products:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    S3 = Scrollbar(frame1t3)
    T3 = Text(frame1t3, height=4, width=50)
    S3.pack(side=RIGHT, fill=Y)
    T3.pack(side=LEFT, fill=Y)
    S3.config(command=T3.yview)
    T3.config(yscrollcommand=S.set)
    quote = pos.getAllProductsNames()
    T3.insert(END, quote)
    sep1t3=ttk.Separator(tab3,orient=VERTICAL)

    frame2t3=Frame(tab3, bd=3, relief="groove")
    label1tab3 = Label(frame2t3, text="Register new product:", font=("Helvetica", 20), fg="black").pack(side=TOP, expand=YES, fill=BOTH)
    label2tab3 = Label(frame2t3, text="SKU: ", font=("Helvetica", 10), fg="black").pack()
    SKUEntryThirdTab = Entry(frame2t3)
    SKUEntryThirdTab.pack()
    label3tab3 = Label(frame2t3, text="Name: ", font=("Helvetica", 10), fg="black").pack()
    productNameEntryThirdTab = Entry(frame2t3)
    productNameEntryThirdTab.pack()
    label4tab3 = Label(frame2t3, text="Price: ", font=("Helvetica", 10), fg="black").pack()
    priceEntryThirdTab = Entry(frame2t3)
    priceEntryThirdTab.pack()

    productResultLabel = Label(frame2t3, text="")
    productResultLabel.pack()
    Button(frame2t3, text="Register new product", command=addProduct).pack()


# Position

    frame1t3.grid( row=1, column=2)
    #label0tab2.grid(row=1, column=2)
    #When it works position rest of elements
    sep1t3.grid(column=4,row=1, rowspan=20 )

    frame2t3.grid(row=1, column=6)
    #label1tab2.grid(row=1, column=6)
    #when it works position rest of elements


    #Cuarta tab
    tab4 = Tab(root, "Reports")
    MainLabel = Label(tab4, text="REPORTS ", font=("Helvetica", 30), fg='deepskyblue4')


    CashFrame=Frame(tab4, bd=3, relief="groove")
    CashLabel = Label(CashFrame, text="Cash vs. CC")
    sep1=ttk.Separator(tab4,orient=VERTICAL)

    CustomerFrame=Frame(tab4, bd=3, relief="groove")
    CustomerLabel = Label(CustomerFrame, text="Customers")
    sep2=ttk.Separator(tab4,orient=VERTICAL)

    GSFrame=Frame(tab4, bd=3, relief="groove")
    GSLabel = Label(GSFrame, text="General Sales")
    sep3=ttk.Separator(tab4,orient=VERTICAL)

    #Create the second plot
    f = Figure(figsize=(3,2), dpi=100, facecolor="white")
    ax = f.add_subplot(111)

    data = (20, 35, 30, 35, 27)

    ind = numpy.arange(5)  # the x locations for the groups
    width = .5

    rects1 = ax.bar(ind, data, width)

    canvas = FigureCanvasTkAgg(f, master=tab4)
    canvas.show()

    #Create the first plot

    tartita=figure(1, figsize=(3,2))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Cash', 'Credit Card'
    fracs = [15, 85]
    explode=(0, 0.1)

    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.

    #title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

    canvas = FigureCanvasTkAgg(tartita, master=tab4)
    canvas.show()

# Posicionamiento

    MainLabel.grid(row=0, column=6, pady=10)

    CashFrame.grid(padx=10, pady=10, row=1, column=2)
    CashLabel.grid(row=1, column=2)
    canvas.get_tk_widget().grid(row=2, column=2)
    sep1.grid(column=4,row=1, rowspan=20, sticky="ns")

    CustomerFrame.grid(padx=10, pady=10, row=1, column=6)
    CustomerLabel.grid(row=1, column=6)
    canvas.get_tk_widget().grid(row=2, column=6)
    sep2.grid(column=8,row=1, rowspan=20, sticky="ns")


    GSFrame.grid(padx=10, pady=10, row=1, column=10)
    GSLabel.grid(row=0, column=10)
    #sep3.grid(column=6,row=1, rowspan=20, sticky="ns")


    tab5 = Tab(root, "Settings")
    def askFolder():
        dirname = askdirectory()
        print(dirname)
      
    def askFile():
        filepath = askopenfilename()
        print(filepath)

    def saveFile():
        filename = asksaveasfilename()
        return open(filename, 'w')
    
    tab5label0 = Label(tab5, text="SETTING: ", font=("Helvetica", 20))
    frametab5=Frame(tab5, bd=5, relief="groove")
    tab5label3 = Label(frametab5, text="Download All Data")
    tab5label4 = Label(frametab5, text="Change background theme")
    Button3=Button(frametab5, text="Download", command=pos.downloadCSVfile)
    Button4=Button(frametab5, text="Change the Theme")
    tab5label0.grid(row=0, column=1, pady=5)
    frametab5.grid(padx=10, pady=10, row=1, column=1)
    tab5label3.grid(row=1, column=1)
    tab5label4.grid(row=2, column=1)
    Button3.grid(row=1, column=3)
    Button4.grid(row=2, column=3)

    bar.add(tab1)                   # add the tabs to the tab bar
    bar.add(tab2)
    bar.add(tab3)
    bar.add(tab4)
    bar.add(tab5)

    root.grid_columnconfigure(0,weight=1)
    root.grid_columnconfigure(1,weight=1)
    root.grid_rowconfigure(0,weight=1)
    root.grid_rowconfigure(1,weight=1)
    root.grid_rowconfigure(2,weight=1)
    root.grid_rowconfigure(3,weight=1)
    root.grid_rowconfigure(4,weight=1)


    bar.show()
    root.mainloop()
