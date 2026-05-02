import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

list = [91, 1, 56, 23, 78, 34, 12, 45, 67, 89]

print("Unsorted list :: ")
print(list)

print("Bubble Sort :: ")
for i in range(len(list)):
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

print("Selection sort")
for i in range(len(list)):
    min_index = i
    for j in range(i + 1, len(list)):
        if list[j] < list[min_index]:
            min_idx = j
    list[i], list[min_index] = list[min_index], list[i]
print(list)