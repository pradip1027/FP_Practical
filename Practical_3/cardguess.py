import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random as random

random_suit = int(random.randint(1,4))
random_card = int(random.randint(1,13))

print(f"Suit : {random_suit}")
print(f"Card : {random_card}")


print("Instructions for Card Guessing")
print("For Suit :: Diamond = 1, Heart = 2, Spade = 3, Club = 4 ")
print("For Card :: Ace = 1, Jack = 11, King = 12, Queen = 13 ")

guessed_suit = int(input("Enter your guessed suit : "))
guessed_card = int(input("Enter your guessed card : "))

if(guessed_suit == random_suit):
    print("You guessed right Suit")

if(guessed_card == random_card):
    print("You guessed right Card")

if(guessed_card != random_card and guessed_suit != random_suit):
    print("Your full guessed is wrong")