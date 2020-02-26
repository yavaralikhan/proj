import matplotlib.pyplot as plt
"""
Y = [0, 1, 2, 3, 4, 5]
plt.plot(Y)
plt.show()
"""

X = list(range(1, 11))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]
print(Y1)
print(Y2)
print(Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.grid(True)
plt.legend()
plt.show()
