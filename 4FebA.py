class Product:

    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity
        self.nextProduct = None
        self.prevProduct = None

    def showProductDetails(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{}\t{}\t{}".format(self.pid, self.name, self.price))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

class Queue:

    size = 0
    items = 0
    price = 0

    def __init__(self):
        print(">> queue Created")
        print(self)
        self.head = None
        self.current = None

    def add(self, product):
        print(product)
        Queue.size += 1
        Queue.items += product.quantity
        Queue.price += (product.quantity * product.price)

        if self.head == None:
            self.head = product
            self.current = product
        else:
            product.prevProduct = self.current
            self.current.nextProduct = product

            self.current = product
            product.nextProduct = self.head
            self.head.prevProduct = self.current

    def iterate(self):

        temp = self.current

        while temp.prevProduct != self.current:
            temp.showProductDetails()
            temp = temp.prevProduct
            print(">> temp is:", temp)

        temp.showProductDetails()


    def poll(self):

        self.current = self.current.prevProduct
        self.current.nextProduct = self.head
        self.head.prevProduct = self.current



shoppingCart = Queue()


shoppingCart.add(Product(101, "1. iPhoneX", 70000, 1))
shoppingCart.add(Product(301, "2. AlphaBounce", 8000, 2))
shoppingCart.add(Product(701, "3. Samsung LED", 40000, 1))
shoppingCart.add(Product(401, "4. Samsung M10", 1000, 3))

shoppingCart.iterate()

print("#####################")

shoppingCart.poll()
shoppingCart.poll()

shoppingCart.iterate()