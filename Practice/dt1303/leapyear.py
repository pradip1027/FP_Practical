def leapyearcheck(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input("Enter the year to check the leap : "))
check  = leapyearcheck(year)
print(check)