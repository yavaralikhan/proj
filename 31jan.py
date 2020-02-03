class Product:
    def __init__(self,pid,name,brand,):
        self.pid = pid
        self.name = name
        self.brand = brand

    def showProductDetails(self):
        print("{} | {} |{}".format(self.pid, self.name, self.brand))

class Shoe(Product):
    def __init__(self,pid,name,brand,Shoesize):
        Product.__init__(self,pid,name,brand)
        self.Shoesize = Shoesize
    def showShoeDetails(self):
        Product.showProductDetails(self)
        print("{}".format(self.Shoesize))
        print("---------------")

class Mobile(Product):
    def __init__(self,pid, name, brand, OS):
        Product.__init__(self, pid, name, brand)
        self.OS = OS

    def showMobileDetails(self):
        Product.showProductDetails(self)
        print("{}".format(self.OS))
        print("---------------")


sref = Shoe(101, "Bounce", "Nike", 8)
mref = Mobile(523, "iPhone", "Apple", "iOS")

sref.showShoeDetails()
mref.showMobileDetails()