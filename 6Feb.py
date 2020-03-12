import mysql.connector as lib

class Customer:
    def __init__(self, mode):
        if mode == 1:
            self.id = 0
            self.name = input("Enter name of the Customer :")
            self.phone = input("Enter mobile number of the Customer :")
            self.email = input("Enter email of the customer :")
        elif mode == 2:
            self.id = input("Enter id of the customer :")
            self.name = input("Enter name of the Customer :")
            self.phone = input("Enter mobile number of the Customer :")
            self.email = input("Enter email of the customer :")
        else:
            pass

    def showCustomerDetails(self):
        print("{} <> {} <> {} <> {}".format(self.id, self.name, self.phone, self.email))

def executeSQL(sql):
    con = lib.connect(user="root", password="", database="check", host="127.0.0.1", port="3306")
    print("~~Connection Created~~")
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

repeat = "yes"

while repeat == "yes":

    print("==Welcome to Customer Management App==")
    print("1. Register New Customer")
    print("2. Update Existing Customer")
    print("3. Delete Existing Customer")
    print("4. View All Customers")
    print("5. View Customer by ID")
    print("6. View Customer by Phone")

    choice = int(input("Enter your choice"))

    if choice == 1:
        customer = Customer(1)
        customer.showCustomerDetails()

        save = input("Do you want to save this customer? (yes/no)")

        save = input("Would you like to Save Customer? (yes/no): ")
        if save == "yes":
            sql = "insert into Customer values(null, '{}', '{}', '{}')".format(customer.name, customer.phone, customer.email)
            executeSQL(sql)
            print(">> CUSTOMER SAVED :)")



    elif choice ==2:
        customer = Customer(2)
        customer.showCustomerDetails()

        save = input("Would you like to update the customer? (yes/no)")

        if save == "yes":
                sql = "update Customer set name = '{}', phone='{}', email= '{}' where id = {}".format(customer.name, customer.phone, customer.email, customer.id)
                executeSQL(sql)
                print(">> CUSTOMER UPDATED :)")


    elif choice == 3:

        id = int(input("Enter Customer ID to be Deleted: "))
        delete = input("Would you like to Delete Customer? (yes/no): ")

        if delete == "yes":
            sql = "delete from Customer where id = {}".format(id)
            executeSQL(sql)
            print(">> CUSTOMER DELETED :)")




    elif choice == 4:


        sql = "select * from Customer"
        con = lib.connect(user="root", password="", database="check", host="127.0.0.1", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()


        for row in rows:
            customer = Customer(3)
            customer.id = row[0]
            customer.name = row[1]
            customer.phone = row[2]
            customer.email = row[3]

            customer.showCustomerDetails()


    elif choice == 5:
        id = int(input("Enter customer id to be searched"))
        sql = "select * from Customer where id = {}".format(id)
        con = lib.connect(user="root", password="", database="check", host="127.0.0.1", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        if row is not None:
            print(row)
        else:
            print("ID not found")

    elif choice == 6:
        phone = input("Enter Customer Phone to be Searched: ")
        sql = "select * from Customer where phone = '{}'".format(phone)
        con = lib.connect(user="root", password="", database="check", host="127.0.0.1", port="3306")
        cursor = con.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()

        if row is not None:
            print(row)
        else:
            print(">> Customer with Phone Number {} Not Found".format(phone))


    else:
        print("Enter a Valid Choice")

repeat = input("would you like to re use app? (yes/no)")