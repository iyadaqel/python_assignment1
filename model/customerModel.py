import sqlite3
class Customer(object):
    total=0
    customers={}


    def __init__(self, customerID=0, customerName=""):
        self.customerID=customerID
        self.customerName=customerName
        Customer.total+=1
        Customer.customers[customerID] = self
        Customer.insertIntoDB(self)


    def totalCustomers(self):
        return Customer.total

    def getId(self):
        return self.customerID

    def setId(self,new_id):
        self.customerID=new_id

    @staticmethod
    def getCustomerList():
        #return Customer.customers
        conn = sqlite3.connect('../pos.db')
        rows = conn.execute("SELECT * FROM CUSTOMER")
        return rows
        # #conn.execute("INSERT INTO CUSTOMER (customerID,customerName) VALUES ('" + str(self.customerID) + "', '" + self.customerName + "')")
        # print(conn.execute("SELECT * FROM CUSTOMER"))


    def searchCustomerByID(customerID):
        conn = sqlite3.connect('../pos.db')
        cursor = conn.cursor()
        query = "SELECT * FROM CUSTOMER WHERE customerID =" + str(customerID)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is None:
            return False
        else:
            return row

        # if(customerID in Customer.customers):
        #     return Customer.customers[customerID]
        # else:
        #     return False

    def insertIntoDB(self):
        conn = sqlite3.connect('../pos.db')
        conn.execute("INSERT INTO CUSTOMER (customerID,customerName) VALUES ('" + str(self.customerID) + "', '" + self.customerName + "')")
        conn.commit()
        conn.close()