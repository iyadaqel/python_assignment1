class Customer(object):
    total=0
    def __init__(self, customerID, customerName):
        self.__customerID=customerID
        self.__customerName=customerName
        Customer.total+=1
self.__customers=[]
    def totalCustomers(self):
        return Customer.total
    def getId(self):
        return self.__customerID
    def setId(self,new_id):
        self.__customerID=new_id
        self.__customers.append(customerName)
    def searchCustomer(self,customerID):
        if isinstance(self.__customerID,str)==True:
            searchval=1
        else:
            searchval=0
            print("Not valid user ID")
        return(searchval)
            
        
