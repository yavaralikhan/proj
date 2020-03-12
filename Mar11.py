import numpy as np


class LinearRegressionModel:

    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.mse = 0

    def fit(self, X, Y):
        self.X = X
        self.Y = Y
        self.b1 = np.sum((self.X-np.mean(self.X))*(self.Y-np.mean(self.Y)))/np.sum(np.square((self.X - np.mean(self.X))))
        self.b0 = np.mean(self.Y) - (self.b1 * np.mean(self.X))
        print("B1 is : {}". format(self.b1))
        print("B0 is : {}". format(self.b0))

    def predict(self, X):
        Y = self.b0 + self.b1 * X
        return Y


X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

# Model Creation
model = LinearRegressionModel()

# Model Training
model.fit(X, Y)

predictedOutput = model.predict(6)
print(">> Predicted Output for 6 is:", predictedOutput)