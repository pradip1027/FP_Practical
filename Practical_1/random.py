from datetime import datetime

now = datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random

number = random.randint(1, 1000)
summation = 0
print("Numder generated randomly is : ", number)
length = len(str(number))

for i in range(0, length):
    a = number % 10
    summation = summation + a
    number = number // 10

print(summation)
