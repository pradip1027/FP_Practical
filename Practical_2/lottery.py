from datetime import datetime
#this is the module used to print date and time stamp
now = datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import random

def lottery_number():
    #to generate the random number in b/w 10 - 99 (2 digit nunmber)
    random_number = random.randint(10,99)
    print(random_number)
    #usr input number
    user_number = input("Try your luck by inputting any number : ")
    user_string = str(user_number)

    if int(user_number) == random_number:
        print("Congratulation !! You won $10,000.")

    #conerting interger datatype into string type

    #comparing the str type of random_number to the reverse string type of user_number
    elif user_string[::-1] == str(random_number):
        print("You won $5,000")

    #use of "in" operration for value matching in the collection
    elif user_string[0] in str(random_number) or user_string[1] in str(random_number):
        print("You won $2,000")

print("===== Welcome to the Lottery =====")
lottery_number()