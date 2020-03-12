from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd

table = pd.read_csv("advertising.csv")
print(table)

X = table.TV.values
Y = table.Sales.values

print(X, X.shape)
print(Y, Y.shape)

X = X.reshape(len(X), 1)
Y = Y.reshape(len(Y), 1)

model = LinearRegression()
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_

print(b0)
print(b1)

Y1 = model.predict(X)
print(Y1, Y1.reshape)

score = r2_score(Y, Y1)
print(score)