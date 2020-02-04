class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {} | Phone: {} | Email: {}".format(self.name, self.phone, self.email))


class Driver(Customer):

    def __init__(self, name, phone, email, licenseNumber):
        Customer.__init__(self, name, phone, email)
        self.licenseNumber = licenseNumber

    def showDriverDetails(self):
        print("DRIVER DETAILS:")
        self.showCustomerDetails()
        print("LicenseNumber:", self.licenseNumber)


class Cab:

    def __init__(self, regNumber, basePrice):
        self.regNumber = regNumber
        self.basePrice = basePrice

    def showCabDetails(self):
        print("CAB DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class Uber(Cab):

    def showCabDetails(self):
        print("Uber DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class Ola(Cab):

    def showCabDetails(self):
        print("Ola DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class Rapido(Cab):

    def showCabDetails(self):
        print("Rapido DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class Ride:
    rideNumber = 1

    def __init__(self, customer):
        self.ride = Ride.rideNumber
        self.customer = customer
        Ride.rideNumber += 1

    def selectSourceAndDestination(self):
        self.source = input("Enter Source: ")
        self.destination = input("Enter Destination: ")
        print("Ride shall be Booked From {} to {}".format(self.source, self.destination))

    def selectCab(self):
        self.cab = None
        print("Select a Cab:")
        print("(Uber) | (Ola) | (Rapido)")
        choice = input("Select Type of Cab: ")

        if choice == "Uber":
            self.cab = Uber("PB10A7512", 600)
        elif choice == "Ola":
            self.cab = Ola("PB13D7869", 700)
        else:
            self.cab = Rapido("PB28R1236", 50)

    def attachDriver(self, driver):
        self.driver = driver

    def showRideDetails(self):
        print("Ride Booked From {} to {}".format(self.source, self.destination))
        print("Ride Number:", self.ride)
        self.cab.showCabDetails()
        self.driver.showDriverDetails()
        self.customer.showCustomerDetails()


customer = Customer("Yavar", "+91 98886 69707", "yavar@admin.com")
driver = Driver("Mike", "+91 98657 56320", "wazoski@icloud.com", "PB28R1236")

ride = Ride(customer)
ride.selectSourceAndDestination()
ride.selectCab()
ride.attachDriver(driver)
ride.showRideDetails()