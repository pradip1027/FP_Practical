from datetime import datetime
#this module is used for printing the date and time stamp
now = datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random

#made a function for the number gusseing game
def number_guess():
    random_number = random.randint(10,99)
    #print(random_number)
    user_number = None

    #condition assigned for the > , < or = condition
    while random_number != user_number:
        user_number = int(input("Guess the random number : "))
        if random_number > user_number:
            print("Your guessed number is Lower !!")
        elif random_number < user_number:
            print("Your guessed number is Higher !!")
        else:
            print(f"You guessed the Right Number : {random_number}")

print("===== Welcome to the number guessing game =====")
number_guess()