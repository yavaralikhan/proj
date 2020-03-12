import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
print(">> Firebase Configured and Initialized :)")

class Customer:

    def __init__(self):
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customers Email: ")

    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))


def main():
    customer = Customer()
    customer.showCustomerDetails()

    customerData = customer.__dict__
    print(customerData, type(customerData))

    db = firestore.client()
    db.collection("NewFile").document(customer.phone).set(customerData)
    print(">> CUSTOMER SAVED")

if __name__ == "__main__" :
  main()