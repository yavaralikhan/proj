cart = []
choice = "yes"
while choice == "yes" :
    item = input("Enter the item")
    cart.append(item)
    choice = input("would you like something else?")
else:
    print(cart)
    print("your cart:", cart)

if item in cart > 4 :
    print("add more items")
else:
    print("cart")