#Function used to check if a string is numeric or not
#hola otra vez!
#tried to create a class for the customer
class Customer(object):
    def __init__(self, id, name, surname, contact, street, zipCode):
        self.id=id
        self.name=name
        self.surname=surname
        self.contact=contact
        self.street=street
        self.zipCode=zipCode
#just tried if I could make the user a class, not sure if it works
class User:
    pass
userDictionary=User()
userDictionary.id=name
"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
#define the function for creating a user
def create_user(userDictionary , id, name):
    #usersList = userDictionary.keys()
    #lastPos=len(usersList) -1
    #valor=int(usersList[lastPos]) + 1
    userDictionary[id]=name
    return userDictionary


#define the function for searching a user.
#If user id is valid searchval =1 and if it's not valid searchval = 0
def search_user(id1,user2):
    if is_number(id1)==True:
        id1=int(id1)
        if id1 in user2:
            searchval=1
        else:
            print("Not valid user ID")
            searchval=0
    else:
         print("Not valid user ID")
         searchval=0
    return(searchval)
