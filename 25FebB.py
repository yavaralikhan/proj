import pandas as pd
num1 = [10, 20, 30, 40, 50]
num2 = [11, 22, 33, 44, 55]
emp1 = {"name": "fiona", "Age": 25, "salary": 52000}
emp2 = {"name": "john", "Age": 28, "salary": 102000}

frame1 = pd.DataFrame([num1, num2])
frame2 = pd.DataFrame([emp1, emp2])

print(frame1)
print("----------------")
print(frame2)
print("~~~~~~~~~~~")
print(frame1[0])
print("============")
print(frame2["name"])
print("<><><><><><><><><><><><>")
print(frame1[1][1])
print(frame2["salary"][1])

print("SLICING")
print(frame1[0:2])
print(frame2[0:1])

print("DELETION")

del frame1[0]
print(frame1)
frame3 = frame2.drop(0, axis=0)
print(frame3)

print("UPDATION")

frame1[1][1] = 45
print(frame1)
