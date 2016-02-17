'''Ask for the command
FORMAT: The order is not relevant, but every piece if information has to start with
#SKU:     (for the SKU number)
#CC:       (for the CC numer)
#ID:         (for the user ID)
if there is no SKU and it's just price, for instance 10 euro, it has to be like this:  #10

Examples of commands  (most of them dont make sense because they have SKU and price or two customerID's but it's just to test the code)
#SKU:00001 #ID:Customer123 #CC:123ABC #876
#SKU:123 #ID:Customer123 #CC:123ABC #ID:Customer123654
#5656 #wefsc #CC:348965
'''
import customer
#Example of a SKU-price dictionary:
products={"00001": 10, "00002": 15, "00003": 20, "00004": 25}


#Module to ask if the product has SKU or not. Returns SKU_Numb that keeps the price or the SKU and casoStock that keeps if the SKU or the price is provided
def guessPrice(SKU_Numb , products):
    if products.get(SKU_Numb)==None:
        precioproducto=0
        SKU_Numb=0
    else:
        precioproducto=products.get(SKU_Numb)
    return precioproducto
        
#Function used to check if a string is numeric or not
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def extractCommandos(cadena , userss):
    users=list(userss.keys())

    comandos=cadena.split(" ")
    dict={}
    SKU1=0
    CC1=0
    ID1=0
    price=0
    asku=0
    acc=0
    aID=0
    aprice=0
    for m in range (0, len(comandos)):
                   ayud=comandos[m].upper()
                   if ayud.find("#SKU:")== 0:#Si ya hay un precio
                       if price!=0 and asku==0:#Primer sku que se da habiendo ya precio
                           print("You already provided a price for the product. The SKU is not going to be used")
                           asku+=1
                       elif price!=0:#segundo o mas sku que se da ya habiendo precio
                           asku+=1
                       else:
                           if SKU1!=0 and asku==0:#Si ya se ha dado SKU, y es primera vez que repito
                               print("You are providing more than one SKU, only the first one is going to be used.")
                               asku+=asku
                           elif SKU1!=0:#Si repito por segunda vez o mas ya no aviso
                               asku+=1
                           else:
                                SKU1=ayud.split(":")[1]
                                if guessPrice(SKU1, products)==0 and asku==0:
                                    print("SKU number not valid.")
                                    asku+=1
                                    SKU=0
                                elif guessPrice(SKU1, products)==0:
                                    asku+=1
                                    SKU=0
                                else:
                                    dict['SKU'] = SKU1
                                    
                                

                   elif ayud.find("#CC:")== 0:
                       if CC1!=0 and acc==0:
                           print("You are providing more than one #CC, only the first one is going to be used.")
                           acc+=1
                       elif CC1!=0:
                           acc+=1
                       else:
                            CC1=ayud.split(":")[1]
                            dict['CC'] = CC1
                   elif ayud.find("#ID:")== 0:
                       if ID1!=0 and aID==0:
                           print("You are providing more than one #ID, only the first one is going to be used.")
                           aID+=1
                       elif ID1!=0:
                           aID+=1
                       else:
                           ID1=ayud.split(":")[1]
                           if customer.search_user(ID1,users)==1:
                                dict['customerID'] = ID1
                           else:
                                dict['customerID'] = 0
                                ID1=0
                                    
                   else:
                                  le=len(comandos[m])-1
                                  restos=comandos[m][1:le]
                                  if is_number(restos)==True:
                                      if price!=0 and aprice==0:#Segunda vez que se da precio
                                          print("You are providing more than one price for the product. Only the first one is going to be used")
                                          aprice+=1
                                      elif price!=0:#Tercera vez o mas que se da precio
                                          aprice+=1
                                      elif SKU1!=0 and aprice==0:#Das el precio pero ya habia un SKU
                                          print("You already provided a SKU number, the price info is not going to be used")
                                          aprice+=1
                                      elif SKU1!=0:
                                          aprice+=1
                                      else:
                                          if float(restos)<0:
                                              print("The price has to be a positive value")
                                          else:
                                            price=restos
                                  else:
                                                 print("The substring ", comandos[m], "does not correspond to any useful information" )

    #Option to create a new user if Customer ID is not provided
    ask_Create=0

    if SKU1==0 and price==0:
         print("#SKU or price must be provided")
    if CC1==0:
        dict['Cash'] =1
        Cash1=1
    '''
    if ID1==0:
        while ask_Create!="Y" and ask_Create!="N":
            ask_Create=input("Do you want to register this new customer?  [Y/N]  ")
            ask_Create=ask_Create.upper()
            if ask_Create=="Y":
                userito=customer.create_user(users)
                ID1=userito[0]
                name=userito[1]
                dict['customerID'] = ID1
                userss[str(ID1)]=name
                users.append(ID1)
            elif ask_Create=="N":
                ID1=0
                dict['customerID'] = ID1
            else:
                ask_Create=input("Do you want to register this new customer?  [Y/N]  ")
                ask_Create=ask_Create.upper()

    '''
     #Establecemos el precio usando la variable SKU or price, la que sea !=0
    if SKU1==0:
        priceprod=price
    else:
        priceprod=guessPrice(SKU1 , products)

    dict['price']= priceprod
    return (dict)


