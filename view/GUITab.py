from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from view.Tab import Tab
from view.Tab import TabBar
from controller import pos as pos
from controller import initialise as i

i.intialize()


if __name__ == '__main__':
    def write(x): print (x)

    def addSale():
        #Don't forget to check for the values before you submit

        customerID = UserIdEntry.get()
        SKU = SKUEntry.get()
        amount = AmountEntry.get()
        cc = ccButtonValue.get()
        result = pos.addSale(customerID ,SKU , cc)
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
    #root.geometry('700x300')
    root = Tk()
    root.title("PYTHUNICORNS POS")
    bar = TabBar(root, "Sales")
    tab1 = Tab(root, "Sales")


    #First Tab
    RegSaleLabel = Label(tab1, text="Register a Sale: ", font=("Helvetica", 20))
    RegSaleFrame=Frame(tab1, bd=5, relief="groove")
    UserIdLabel = Label(RegSaleFrame, text="User ID:")
    UserIdEntry = Entry(RegSaleFrame, width=18)
    SKULabel = Label(RegSaleFrame, text="SKU/Price:")
    SKUEntry = Entry(RegSaleFrame, width=18)
    AmountLabel = Label(RegSaleFrame, text="Amount:")
    AmountEntry = Entry(RegSaleFrame, width=18)
    resultLabel = Label(RegSaleFrame, text="")
    ccButtonValue = IntVar()
    chButton=Checkbutton(RegSaleFrame, text="cc" , variable=ccButtonValue)
    RegistSale=Button(RegSaleFrame, text="Register", command=addSale)

# Positions of the First Tab
    RegSaleLabel.grid(row=0, column=1, pady=5)
    RegSaleFrame.grid(padx=10, pady=10, row=1, column=1)
    UserIdLabel.grid(row=0, column=1)
    UserIdEntry.grid(row=0, column=2, padx=10)
    SKULabel.grid(row=1, column=1)
    SKUEntry.grid(row=1, column=2)
    AmountLabel.grid(row=2, column=1)
    AmountEntry.grid(row=2, column=2)
    resultLabel.grid(row=4 , column=1)
    RegistSale.grid(row=5, column=2, pady=8)
    chButton.grid(row=5, column=1)


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

    frame1t2.grid(padx=10, pady=10, row=1, column=2)
    #label0tab2.grid(row=1, column=2)
    #When it works position rest of elements
    sep1t2.grid(column=4,row=1, rowspan=20, sticky="ns")

    frame2t2.grid(padx=10, pady=10, row=1, column=6)
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

    productResultLabel = Label(frame2t2, text="")
    productResultLabel.pack()
    Button(frame2t3, text="Register new product", command=addProduct).pack()


# Position

    frame1t3.grid(padx=10, pady=10, row=1, column=2)
    #label0tab2.grid(row=1, column=2)
    #When it works position rest of elements
    sep1t3.grid(column=4,row=1, rowspan=20, sticky="ns")

    frame2t3.grid(padx=10, pady=10, row=1, column=6)
    #label1tab2.grid(row=1, column=6)
    #when it works position rest of elements


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
