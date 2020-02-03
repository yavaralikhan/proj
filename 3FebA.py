class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))

class PrimeCustomer(Customer):
    def __init__(self,Customer):
        Customer.prime = True
        Customer.Videos = True
        Customer.Music = True

    def showPrimeCustomer(self, Customer):
        print("PRIME FEATURES: VIDEOS: {} | MUSIC: {}".format(Customer.Videos, Customer.Music))
        Customer.showCustomerDetails()


ref1 = Customer("Yavar", 9888669707, "yavarkhan217@gmail.com")

primeref = PrimeCustomer (ref1)
print(primeref.__dict__)

primeref.showPrimeCustomer(ref1)