print("------------------")
print("App Started")
print("~~~~~~~~~~~~~~~~~~")

numbers = [10, 20, 56, 85, 103, 753, 563, 986, 1237, 8763]
idx = int(input("Enter the Number you chooose : "))

try:
    print("Congratulation!!... You won :", numbers[idx])
    print("Wanna play again?")

except Exception as e:
    print("Some Error Occured ", e)

finally:
    print("Thanks for playing :)")
