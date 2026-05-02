import datetime

now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")


from datetime import datetime
import calendar

dob = "05-06-1947"
today = datetime.now()
today_string = today.strftime("%d-%m-%y")

grandfather_dob = datetime.strptime(dob, "%d-%m-%Y")

datediff = today - grandfather_dob
age = datediff.days // 365.25

print(f"\nBirth Date :: {grandfather_dob.strftime('%d-%m-%Y')}")
print(f"Current Date :: {today_string}")

year = int(datediff.days // 365.25)
month = int((datediff.days % 365.25) // 30)
day = int(datediff.days % 30)
print(f"Shyam's Grandfater age is {(year)} year, {month} month and {day} days old.")


print(calendar.month(grandfather_dob.year, grandfather_dob.month))
