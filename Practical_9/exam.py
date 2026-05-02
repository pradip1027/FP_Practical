import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import matplotlib.pyplot as plt

# Total students = 100
# Theory: 6 + x + 46 + 10 + 8 = 100 => x = 30
x = 100 - (6 + 46 + 10 + 8)
print(f"Theory missing value x = {x}")

# Practical: 10 + 28 + y + 15 + 32 = 100 => y = 15
y = 100 - (10 + 28 + 15 + 32)
print(f"Practical missing value y = {y}")

marks = ['0-20', '20-40', '40-60', '60-80', '80-100']
theory  = [6, x, 46, 10, 8]
practical = [10, 28, y, 15, 32]

# Bar chart - Theory
plt.figure(figsize=(7, 4))
plt.bar(marks, theory, color='skyblue')
plt.title('Theory Marks Distribution')
plt.xlabel('Theory Marks')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.show()

# Pie chart - Practical
plt.figure(figsize=(6, 6))
plt.pie(practical, labels=marks, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Practical Examination Result')
plt.tight_layout()
plt.show()