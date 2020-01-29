class Restaurant:

    def __init__(self, name, phone, email, address, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.menu = menu

    def showRestaurant(self):
        print("{}".format(self.name))
        print("{}\n{}\n{}".format(self.phone, self.email, self.address,))

        self.menu.showMenu()

class Menu:

    def __init__(self, name, description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes

    def showMenu(self):
        print("{}".format(self.name))
        print(self.description)

        for dish in self.dishes:
            dish.showDish()


class Dish:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def showDish(self):
        print("===={}====".format(self.name))
        print("{}".format(self.price))


restaurant = Restaurant("Khan's Restaurant", "+91 9875642362",
                        "Khan@khan.com", "Malerkotla",
                        Menu("Main Menu", "Non-Veg Special",
                             [
                                 Dish("Mutton", 500),
                                 Dish("Chicken", 300),
                                 Dish("Biryani", 250),
                                 Dish("Gravy", 100),
                                 Dish("kabab", 150)
                             ]
                             )
                        )
restaurant.showRestaurant()
