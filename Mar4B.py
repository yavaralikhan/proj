import pandas as pd
import numpy as np

oddnumbers = np.arange(1, 100, 2)
evennumbers = np.arange(0, 100, 2)

numbers = {"oddNumbers": oddnumbers, "evenNumbers": evennumbers}
table = pd.DataFrame(numbers)
print(table)
