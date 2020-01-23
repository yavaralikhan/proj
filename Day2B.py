name = "john watson"
print(name, type(name),hex(id(name)))

print("lenght of name",len(name))
print("max of name", max(name))
print("min of name", min(name))

print(name[1])
print(name[len(name)-1])

print(name[1:4])
print(name[1:-4])

#index have a range

print(name[::-1])
email = input("enter your email")
print("you entered", email)

if "@" in email and "." in email:
  print("valid")
else:
    print("unvalid")

    if len(email) < 15 and len(email) >10 :
        print("email is valid")
    else:
        print("unvalid")