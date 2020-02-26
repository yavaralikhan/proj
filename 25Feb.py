import pandas as pd
import numpy as np
numbers1 = [10, 20, 30, 40, 50]
numbers2 = np.arange(11, 51, 10)
series1 = pd.Series(numbers1)
print(series1)

series2 = pd.Series(numbers2)
print(series2)

number3 = {
    "name": "yavar",
    "roll no": 1829014,
    "class": "mca"
}
series3 = pd.Series(number3)
print(series3)


print(series1[2])
print(series2[3])
print(series3["name"])


print(series1[1:3])
print(series2[3:])
print(series3["name":"roll no"])

series1[1] = 254
print(series1)

del series1[2]
print(series1)


series1[5] = 42
print(series1)

series3["name"] = "yasir"
print(series3)
