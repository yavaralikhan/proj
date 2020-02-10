def LoginwithFacebook():
    print("1. Login with Facebook")

def LoginwithGoogle():
    print("Login with Google")

def LoginwithYahoo():
    print("Login with Yahoo")

def login(type):
    type()

print("~~~~~~~~~~~~~~")
print(">> 1. Login with Facebook Account")
print("~~~~~~~~~~~~~~")
print(">> 2. Login with Google Account")
print("~~~~~~~~~~~~~~")
print(">> 3. Login with Yahoo Account")

choice = int(input("Enter a Number to go on with : "))
if choice == 1:
    login(LoginwithFacebook)
elif choice == 2:
    login(LoginwithGoogle)
elif choice == 3:
    login(LoginwithYahoo)

else:
    print("Choose a valid Option")
