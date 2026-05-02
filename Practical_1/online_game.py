from datetime import datetime

now = datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

print("Welcome to the Online Game Registration Form!!")

name = input("Enter your name : ")
username = input("ENter your user name : ")
email = input("Enter your email id : ")
age = int(input("Enter you age : "))

if name is not None and username is not None and email is not None and age is not None:
    print("\n\tThanks for registration and Joining with Us !!")
    print("\nYou are now On-Board with your new Avatar as ")
    print(f"Username : {username}")
    print("\nYour other details are as below")
    print(f"name : {name}")
    print(f"email : {email}")
    print(f"age : {age}")

print(f"You are On-Board with US at {datetime.now().strftime("%d-%m-%y %H:%M:%S")}")
