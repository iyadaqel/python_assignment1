# This file is the main engine of the program. It will take care of redirecting everything.
# For example: it will take the input tokenize it and direct it to the approrpiate method.
from model import customerModel
from model.customerModel import Customer
from model.productModel import  Product
from model.saleModel import Sale


#First time you load the program initate all these.
status = {}

#Still need to implement the Summary

def addSale(customerID , productSKU , cc):
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
        product = Product.getProductBySKU(productSKU)
        if(product != False):
            total = product.price
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
        quote = quote + str(row[0]) + "    " + row[1] +"\n"
    return quote


def getAllProductsNames():
    products = Product.getProductList()
    quote ="Product SKU      NAME\n"
    for row in products:
        quote = quote + str(row[0]) + "    " + row[1] +"\n"
        #quote = quote + str(key) + "    " + products[key].name + "\n"
    return quote



def generateCCReport():
    listOfSales = Sale.getSaleList()
    ccSales = 0
    cashSales = 0
    for sale in listOfSales:
        if(sale.paymethod == "Cash"):
            cashSales += sale.total
        else:
            ccSales += sale.total

    print("Cash Sales: " + str(cashSales) + " ccSales: " + str(ccSales))

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
