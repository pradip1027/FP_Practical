import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import numpy as np

# a. All 8 plants in a single row
plants = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("Plants:", plants)

# b. Split equally on both sides of entrance
split = np.split(plants, 2)
print("Plants:", split)

# c. Two plants destroyed (e.g., index 0 and 1), replaced with 2 new plants (9, 10)
plants = np.delete(plants, [0, 1])
plants = np.append(plants, [9, 10])
print("Plants:", plants)

# Final state
print("Plants:", plants)