class Dish:

    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type
        self.quantity = 0

    def showDish(self):
        print("===={}====".format(self.name))
        print("{}\t{}\t{}".format(self.price, self.type, self.quantity))

dish1 = Dish("Mutton", 500, "Non Veg")
dish2 = Dish("Chicken", 200, "Non Veg")
dish3 = Dish("Paneer", 120, "Indian Veg")
dish4 = Dish("Biryani", 200, "Non Veg")
dish5 = Dish("Dal Makhnni", 150, "Veg")


cart = []
totalDishes = 0

def addDishToCart(dish):
    global totalDishes
    cart.append(dish)
    totalDishes += 1

dish1.quantity = 2
dish3.quantity = 2
dish4.quantity = 1
dish5.quantity = 2

addDishToCart(dish1)
addDishToCart(dish3)
addDishToCart(dish4)
addDishToCart(dish5)

totalPrice = 0
totalItems = 0


for dish in cart:
    dish.showDish()
    totalPrice += (dish.price*dish.quantity)
    totalItems += dish.quantity

print("Total Price:\u20b9", totalPrice)
print("Total Items:", totalItems)
print("Total Dishes:", totalDishes)