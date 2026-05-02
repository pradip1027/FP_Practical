import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")

print(f" TimeStamp {timestamp_str}")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]

months = [("January", 31),("February", 28),("March", 31),("April", 30),("May",31),("June", 30),("July", 31),("August", 31),("September", 30),("October",31),("November", 30),("December", 31)]

year = int(input("Enter a year : "))

start_day = int(input("Enter a day no for week days (i.e Monday=0) : "))

is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

if is_leap:
    months[1] = ("February", 29)
curnt_day = start_day

for month, days_in_month in months:
    print(f"1, {month} {year}, is {days[curnt_day]}")
    curnt_day = (curnt_day + days_in_month) % 7