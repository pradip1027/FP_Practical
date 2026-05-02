import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

sentence = """Hello Everyone, this is a sample text file used as a sample for file handling 
            in python programming using text extension"""

with open("sample1.txt", "w") as file:
    file.write(sentence)

with open("sample1.txt", "r") as file:
    words = file.read()

print(words)

stopwords = ['.', ',', '?', '&', '!']

for sw in stopwords:
    words = words.replace(sw, "")

print(words)

words = words.lower().split()

word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(word, ":", count)