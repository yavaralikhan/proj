import mysql.connector as lib

class Customer:

    def __init__(self):
        self.id = 0
        self.name = input("Enter Customer Name: ")
        self.phone = input("Enter Customer Phone: ")
        self.email = input("Enter Customers Email: ")


    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))


print("==Welcome to Customer Management Software==")
print("1. Register New Customer")

choice = int(input("Enter Your Choice: "))
usage = "yes"
while usage == "yes":
    if choice == 1:
        customer = Customer()
        customer.showCustomerDetails()

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":

            sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
            con = lib.connect(user="root", password="", database="check", host="127.0.0.1", port="3306")
            print(">> Connection Created :)")
            cursor = con.cursor()
            cursor.execute(sql)
            con.commit()

            print(">> CUSTOMER SAVED :)")

            usage = input("Would You Like Use Software Further? (yes/no): ")