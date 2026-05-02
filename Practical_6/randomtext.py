import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random
import string

def generate_random_text(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def count_character(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

random_text = generate_random_text(100)
print("Random text:", random_text)

character_count = count_character(random_text)

# Display characters with their counts
count_line = ""
for char in random_text.lower():
    if char.isalpha() and character_count[char] > 1:
        count_line += f"{char} "

print(count_line)

# Display only characters that appear more than once
repeated_chars = " ".join([f"{char} {count}" for char, count in sorted(character_count.items()) if count > 1])
print(repeated_chars)