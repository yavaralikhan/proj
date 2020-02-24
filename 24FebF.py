import numpy as np
X = np.array([(1, 2, 3), (4, 5, 6)])
Y = np.array([(1, 2, 3), (4, 5, 6)])
print(np.vstack((X, Y)))
print(np.hstack((X, Y)))

Z = np.arange(1, 101, 10)
print(np.log10(Z))
print(np.sin(Z))
print(np.tan(Z))