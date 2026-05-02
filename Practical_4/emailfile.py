import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import requests
import re

url = "https://ict.guni.ac.in/people/category/faculty"

output = requests.get(url)

wordtext = output.text

pattern = r"[a-zA-Z0-9.-]+@ganpatuniversity\.ac\.in"

all_email = re.findall(pattern, wordtext)

unique_email = list(set(all_email))

with open("emaillist.txt", "w") as file:
    for i, email in enumerate(unique_email, start=1):
        line = f"Email {i}: {email}"
        file.write(line + "\n")
        print(line)