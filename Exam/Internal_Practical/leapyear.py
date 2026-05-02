def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)

year = int(input("Enter year :: "))

print(leap_year(year))

