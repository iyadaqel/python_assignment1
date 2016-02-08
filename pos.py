#Import all the modules




#Show the user a menu to choose what he wants
print("Welcome to Pythunicorns POS. Dominating the european markets since 1913  ")
moreOperations= True
while(moreOperations==True ):
    userChoice = input("Please enter your option \n 1. for Sales \n 2. For reports \n 3. To close the day \n")
    if(int(userChoice)==1):
        print("Sales")
    elif(int(userChoice)==2):
        print("Reports")
    elif(int(userChoice)==3):
        print("Close")
        moreOperations = False
print("Have a nice day")