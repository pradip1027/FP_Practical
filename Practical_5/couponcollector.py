import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random

suits = ["heart","spade","diamond","club"]
cards = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
cardsdeck = [(card,suit) for suit in suits for card in cards]

count = 0
selectsuit = set()

while len(selectsuit) < 4:
    randomcard = random.choice(cardsdeck)
    print(f"Picked card :: {randomcard[0]} of {randomcard[1]}")
    count += 1
    selectsuit.add(randomcard[1])

print(f"Number is picks :: {count}")