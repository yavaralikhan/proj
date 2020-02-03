class Order:
    id = 1
    def __init__(self, name, address, price):
        self.oid = Order.id
        self.name = name
        self.address = address
        self.price = price

        Order.id += 1

    def showOrderDetails(self):
        print("{}, {}, {}, {}".format(self.oid, self.name, self.address, self.price))

    def toCSV(self):
        return "{},{},{},{}\n".format(self.oid, self.name, self.address, self.price)

    def saveOrder(self):
        file = open("orders.csv", "a")
        orderData = self.toCSV()
        file.write(orderData)
        file.close()
        print(">> Order[{}] Saved :)".format(self.oid))


order1 = Order("Yavar", " Malerkotla", 8560)
order2 = Order("Gagan", "Ludhiana", 9631)
order3 = Order("Ahmed", "Chandigarh ", 7856)


order1.showOrderDetails()
order2.showOrderDetails()
order3.showOrderDetails()


order1.saveOrder()
order2.saveOrder()
order3.saveOrder()
