from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

data = stats.linregress(X, Y)

print(data[0])
print(data[1])

maxX = np.max(X) + 10
minY = np.min(Y) - 10

print(maxX)
print(minY)

x = np.linspace(minY, maxX, 100)
print(x)

y = data[1] + data[0]*x

print(y)

plt.plot(x, y)
plt.scatter(X, Y)
plt.show()