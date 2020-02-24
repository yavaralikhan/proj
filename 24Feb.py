import numpy as np
a1 = np.array(list(range(10, 21)))
a2 = np.arange(10, 21)
a3 = np.arange(10, 21, 3)

print(a1)
print(a2)
print(a3)

a4 = np.ones((3, 3, 3), dtype=np.int)
print(a4)

a5 = np.linspace(0, 21, 4)
print(a5)