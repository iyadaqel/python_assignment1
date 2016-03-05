class Customer(object):
    total=0
    customers={}


    def __init__(self, customerID=0, customerName=""):
        self.customerID=customerID
        self.customerName=customerName
        Customer.total+=1
        Customer.customers[customerID] = self
      #  Customer.customers.append(self)


    def totalCustomers(self):
        return Customer.total

    def getId(self):
        return self.customerID

    def setId(self,new_id):
        self.customerID=new_id

    def searchCustomerByID(customerID):
        if(customerID in Customer.customers):
            return Customer.customers[customerID]
        else:
            return False