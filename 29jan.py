class Restaurant:
    def __init__(self, name, phone, email, menu):
     self.name = name
     self.phone = phone
     self.email = email
     self.menu = menu

    def showRestaurant(self):
        print("{}".format(self.name))
        print("{}\n{}\n{}".format(self.phone,self.email,self.menu))
          self.menu.showmenu()
class menu:
    def __init__(self, name, description, dishes):
        self.name = name
        self.description = description
        self.dishes = dishes

        def showmenu(self):
         print("{}".format(self.name))
        print("{}".format(self.description))
        print("{}".format(self.superhit))


class actor:
    def __init__(self,name, age):
        self.name = name
        self.age = age

       def showactor(self):
        print("{}".format(self.name))
        print("{}".format(self.age))

        movie = Movie("James Bond", "January","3 crore",
                      Verdict(superhit), Daniel Craig
                      )
        movie.showMovie()