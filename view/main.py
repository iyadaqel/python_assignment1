from controller import pos

print("Welcome to Pythunicorns POS. Dominating the european markets since 1913  ")
while(True):
    userCommand = input("Please enter your command \nuse the following structure:\n For sale enter the following 'Sale #SKU:number #CC:number #ID:number \n"
                      "For adding new customers enter the following: 'Customer #ID:number ' \n For reports enter the following: 'report' or 'crm' \n for closing enter the following 'close' \n")

    status = pos.addCommand(userCommand)
    if(status['action']=='close'):
        print("Have a nice day")
        break
    else:
        print(status['message'])