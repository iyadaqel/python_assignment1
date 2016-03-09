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


#First time you load the program initate all these.
status = {}

#Still need to implement the Summary

def addSale(customerID , productSKU , cc , amount):
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


def addCustomer(customerID , name):
        result ={}
        Customer(customerID , name)
        result['error'] = False
        result['message'] = "Customer Added Successfuly. VIVAAA Pythunicorns"
        return result

def addProduct(SKU, name, price):
        result ={}
        SKU = int(SKU)

        Product(SKU , name , price)
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

    total = ccSales + cashSales
    cashSalesForPieChart = (cashSales / total) * 1000
    ccSalesForPieChart = (ccSales / total) * 1000
    return[cashSalesForPieChart ,ccSalesForPieChart ]

#STILL NEEDS FIXING
def generateCustomerReport():
    listOfSales = Sale.getSaleList()
    customersSales = {}
    keys = customersSales.keys()
    for sale in listOfSales:
        customerID = sale.customer.customerID
        if customerID in keys:
            customersSales[customerID] = customersSales[customerID] + sale.total
        else:
            customersSales[customerID] = 0 + sale.total

    for key, value in customersSales.items():
        print(Customer.searchCustomerByID(key).customerName, value)





def getSalesReports():
    numbers = Sale.getSalesReports()
    valueOfSales = numbers[0]
    print(numbers)