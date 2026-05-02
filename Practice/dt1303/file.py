with open("file1.txt", "r") as f1:
    lines = f1.readlines()

with open("file2.txt", "w") as f2:
    for line in lines[::-1]:
        f2.write(line)