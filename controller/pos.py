##TO DO LIST :
# Implement generateSaleReport()
# FIX GenerateCustomerReport()
# Enhance the graphic of the graphs [ Add legend to the graph - connect the line chart to daily customers]
# Apply the settings
# Check all possible wrong cases
# Dropdown menu for CUSTOMERS and SKU
# Plug Numbers
#Should we allow the user to enter a price only without SKU?





# This file is the main engine of the program. It will take care of redirecting everything.
# For example: it will take the input tokenize it and direct it to the approrpiate method.
from model import customerModel
from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale
from controller import csv_file

#First time you load the program initate all these.
status = {}

#Still need to implement the Summary

def addSale(customerID , productSKU , cc , amount):
        customerID = str(customerID).split(' ', 1)[0]
        productSKU = str(productSKU).split(' ' ,1)[0]
        #Do some logic here and then send it to Sale(Product,PayMethod,Customer , total)
        result = {}
        result['error'] = False
        result['message'] = ""

        #Get the customer
        customer = Customer.searchCustomerByID(customerID)
        if(customer == False):
             customer = Customer.searchCustomerByID(0)

        #Get the product
        productSKU = int(productSKU)



        #pass the product row to the Sale module
        product = Product.getProductBySKU(productSKU)
        if(product != False):
            total = int(amount) * product[2]
        else:
            result['error'] = True
            result['message'] = " Wrong SKU "

        if(cc==1):
            payMethod = "Credit Card"
        else:
            payMethod = "Cash"

        #Create the Sale object
        if(result['error'] != True):
            Sale(product , payMethod , customer , total)
            result['message'] = "Sale Added Successfuly. VIVAAA Pythunicorns"
            return result
        else:
            return result
def getOnlyCustomersID():
    customersID = []
    customers = Customer.getCustomerList()
    for row in customers:
        customersID.append (row[0])
       # quote = quote + str(key) + "    " + products[key].name + "\n"
    return customersID

def addCustomer(customerID , name):
        result ={}
        #Check if the new SKU is already used
        IDList = getOnlyCustomersID()
        if customerID in IDList:
            result['error'] = True
            result['message'] = "The ID belongs to an existing user"
        else:
            Customer(customerID, name)
            result['error'] = False
            result['message'] = "Customer Added Successfuly. VIVAAA Pythunicorns"
        return result

def getOnlyProductsSKU():
    productSKU = []
    products = Product.getProductList()
    for row in products:
        productSKU.append (row[0])
       # quote = quote + str(key) + "    " + products[key].name + "\n"
    return productSKU

def addProduct(SKU, name, price):
        result ={}
        #Check if the new SKU is already used
        SKUList = getOnlyProductsSKU()
        if SKU in SKUList:
            result['error'] = True
            result['message'] = "The SKU is already in the product database"
        else:
            Product(SKU, name, price)
            result['error'] = False
            result['message'] = "Product Added Successfuly. VIVAAA Pythunicorns"

        return result


def getAllCustomersNames():
    customerNames = {}
    customers = Customer.getCustomerList()
    quote ="USER ID      NAME\n"
    for row in customers:
        quote = quote + row[0] + "    " +  row[1] +  "\n"
        #quote = quote + str(key) + "    " +  customers[key].customerName +  "\n"
    return quote


def getAllProductsNames():
    productNames = {}
    products = Product.getProductList()
    quote ="Product SKU      NAME\n"
    for row in products:
        quote = quote + row[0] + "    " +  row[1] + "\n"
       # quote = quote + str(key) + "    " + products[key].name + "\n"
    return quote

def getOnlyProductsNamesAndSKU():
    productNamesAndSKU = []
    products = Product.getProductList()
    for row in products:
        productNamesAndSKU.append (row[0]+ " " + row[1])
       # quote = quote + str(key) + "    " + products[key].name + "\n"
    return productNamesAndSKU

def getOnlyCustomersNames():
    customersNames = []
    customers = Customer.getCustomerList()
    for row in customers:
        customersNames.append (row[0]+ " " + row[1])
       # quote = quote + str(key) + "    " + products[key].name + "\n"
    return customersNames

def generateCCReport():
    listOfSales = Sale.getSaleList()
    ccSales = 0
    cashSales = 0
    for sale in listOfSales:
        if(sale[1] == "Cash"):
            cashSales += sale[4]
        else:
            ccSales += sale[4]

    return[cashSales ,ccSales ]



def generateCustomerReport():
    listOfSales = Sale.getCustomerSales()
    customerList = []
    salesList = []
    for sale in listOfSales:
        customerList.append(sale[0])
        salesList.append(sale[1])
    return(customerList , salesList)



def getSalesReports():
    numbers = Sale.getSalesReports()
    valueOfSales = numbers[0]
    numberOfSales = numbers[1]
    todaySales = numbers[2]
    weeklySales = numbers[3]
    return(numbers)


def downloadCSVfile():
    csv_file.downloadAllFiles()




def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct


def getLastDaysSales():
    last5DaysSales = Sale.getLast5DaysReport()
    dateList = []
    salesList = []
    i = 1
    for sale in last5DaysSales:
        dateList.append(i)
        salesList.append(sale[1])
        i+=1

    print(dateList )
    print(salesList)
    return(dateList , salesList)

