import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import matplotlib.pyplot as plt
import numpy as np

E1 = [20, 18, 30, 22, 15]
E2 = [19, 22, 33, 30, 19]

diff = np.abs(np.array(E1) - np.array(E2))
students = [1, 2, 3, 4, 5]

plt.bar(students, diff, color='skyblue')
plt.title('Difference in marks between E1 and E2')
plt.xlabel('Student')
plt.ylabel('Difference in Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()