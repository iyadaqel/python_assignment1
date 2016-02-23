# This file is the main engine of the program. It will take care of redirecting everything.
# For example: it will take the input tokenize it and direct it to the approrpiate method.

status = {}

def addCommand(userCommand):
    #This function will take a userCommand split it using splituserCommand() and then
    # redirect it to the appropriate class
    #and then return the result as a status dictionary to the view.
    commands = splitUserCommand(userCommand)

    firstCommand =  commands[0].lower()
    #if user choice == sale .. create a new sale with the values  provided. But first check the logic
    if ( firstCommand == 'sale'):
        #DO more magic and then create a sale.
    elif(firstCommand == 'customer'):
        #Do more magic and then create a customer.
    elif(firstCommand == 'report'):
        #Do more magic and then create a report.
    elif(firstCommand == 'crm'):
        #Do more magic and then create a report.
    elif(firstCommand == 'close'):
        status['action']  == 'close'
        status['message'] == 'Have a nice day'
    else:
        #i don't understand the command.
        status['message'] == 'Have a nice day'



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
