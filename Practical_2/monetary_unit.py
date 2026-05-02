from datetime import datetime
#this is the module used to print date and time stamp
now = datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

#function for money breakdown
def monetary(amt):
    dollar = amt // 100
    print(f"{dollar} Dollars")

    amt = amt % 100
    quarters = amt // 25
    print(f"{quarters} Quarters")

    amt = amt % 25
    dimes = amt // 10
    print(f"{dimes} Dimes")

    amt = amt % 10
    nickels = amt // 5
    print(f"{nickels} Nickels")

    amt = amt % 5
    pennies = round(amt)
    print(f"{pennies} Pennies")


print("===== This is monetrary calculation =====")
amount = float(input("Enter the amount : "))
monetary(amount*100 )