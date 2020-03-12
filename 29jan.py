class Restaurant:
    def __init__(self, name, phone, email, menu):
     self.name = name
     self.phone = phone
     self.email = email
     self.menu = menu

    def showRestaurant(self):
        print("{}".format(self.name))
        print("{}\n{}\n{}".format(self.phone,self.email,self.menu))
        self.menu.showMenu()

class Menu:
    def __init__(self, name, description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes

    def showMenu(self):
        print("{}".format(self.name))
        print("{}".format(self.description))
        print("{}".format(self.superhit))


class Dish:
    def __init__(self,name, price):
      self.name = name
      self.price = price

    def showMenu(self):
        print("{}".format(self.name))
        print("{}".format(self.price))

    dish = Dish("James", 500)

    menu.showMenu()