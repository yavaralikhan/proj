import numpy as np

numbers = {10, 20, 30, 40, 50}
print(numbers, type(numbers))

array = np.array([{"Name": "John", "Age": 21}, {"Name": "Yavar", "Age": 23}])
print(array, type(array))

for num in array:
    print(num)