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
        result['error'] = True
        result['message'] = "Customer Added Successfuly. VIVAAA Pythunicorns"
        return result


def getAllCustomersNames():
    customerNames = {}
    customers = Customer.getCustomerList()
    for key in customers:
        customerNames[key] = customers[key].customerName
    return customerNames


def getAllProductsNames():
    productNames = {}
    products = Product.getProductList()
    for key in products:
        productNames[key] = products[key].name
    return productNames



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



def splitUserCommand(userCommand):
    #All the logic for splitting should happen here
    #This function return a dictionary with the found attribute and most importantly action:sale or action:crm ..etc

    userChoice=userCommand.split(" ")
    return userChoice
   # userInputWithoutFirstCommand= " ".join(userInput.split(" ")[1:])





'''
    userChoice=userCommand.split(" ")[0].lower()
    userInputWithoutFirstCommand= " ".join(userCommand.split(" ")[1:])
    if(userChoice == 'sale'):
        sale = Sales.extractCommandos(userInputWithoutFirstCommand , userss)
        dailySales.append(sale)
        print("You successfully regiestered a sale")
    elif(userChoice=='customer'):
        custom erName = input("Please enter customer name ")
        id = userInput.split(" ")[1].split(":")[1];
        print(customer.create_user(userss ,id , customerName))
    elif(userChoice=='report'):
        report = report.build_cash_report(dailySales)
        print("Cash Sales for today are: " + str(report['cash_sales']))
        print("Credit Card Sales for today are " + str(report['cc_sales']))
    elif(userChoice=='crm'):
        crm = report.build_customer_report(dailySales)
        for k,v in crm.items():
                print(" Sales for Customer ID:" + k + " are  " + str(v))
    elif(userChoice=="close"):
        break;
    else:
        print("Command not found. Please input the correct command")
'''
