import numpy as np
import time

array1 = np.array(list(range(1,1001)))
print(array1)

timestamp1 = time.time()

for i in array1:
    print(i)

timestamp2 = time.time()
print(timestamp2-timestamp1)

numbers = list(range(1,1001))

timestamp3 = time.time()
for num in numbers:
    print(num)

print(timestamp3-timestamp2)