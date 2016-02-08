#Import all the modules




#Show the user a menu to choose what he wants
# print("Welcome to Pythunicorns POS. Dominating the european markets since 1913  ")
userchoice = input("Please enter your option \n 1. for Sales \n 2. For reports \n 3. To close the day \n 4. To quit \n")
while(int(userchoice) != 4):
    #Do somestuff
    print("The sales process goes here")
    moreSales = input("More sales? Y/N")
    if(moreSales=="Y"):
        continue
    elif(moreSales=="N"):
        break
print("Have a nice day")

