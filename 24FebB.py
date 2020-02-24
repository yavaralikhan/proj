import numpy as np
a1 = np.arange(10, 88, 5)
a2 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
print(a1)
print(type(a1))
print(a1.shape)
print(a1.ndim)
print(a1.size)
print("~~~~~~~~~~~~~~")
print(a2)
print(type(a2))
print(a2.shape)
print(a2.ndim)
print(a2.size)

print("====Slicing======")
print(a1[:3])
print(a1[5:])
print(a1[5:8])

print(a2[0:2])

print("=======INDEXING=========")

print(a1[1])
print(a1[-1])
print(a2[0][1])
print(a2[0, 2])

print("=====SLICING AND INDEXING")

print(a2[0:2, 0:2])