#Import all the modules
import Sales
import report
import customer

dailySales = []
userss={0:"NonRegistered",1:"Monica",2:"Begum",3:"Iyad",4:"Carmen"}


#Show the user a menu to choose what he wants
print("Welcome to Pythunicorns POS. Dominating the european markets since 1913  ")
while(True):
    userInput = input("Please enter your command \nuse the following structure:\n For sale enter the following 'Sale #SKU:number #CC:number #ID:number \n"
                      "For adding new customers enter the following: 'Customer #ID:number ' \n For reports enter the following: 'report' or 'crm' \n for closing enter the following 'close' \n")
    userChoice=userInput.split(" ")[0].lower()
    userInputWithoutFirstCommand= " ".join(userInput.split(" ")[1:])
    if(userChoice == 'sale'):
        sale = Sales.extractCommandos(userInputWithoutFirstCommand , userss)
        dailySales.append(sale)
        print("You successfully regiestered a sale")
    elif(userChoice=='customer'):
        customerName = input("Please enter customer name ")
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

print("Have a nice day")
