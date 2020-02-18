import numpy as np
array1 = np.ones(8)
array2 = np.zeros(8)
numbers = [1, 1, 1, 1, 1, 1, 1]
array3 = np.array(numbers)
print(array1)
print(array2)
print(array3)
print(array3.shape)

array = array1.reshape(2, 2, 2)
print(array)