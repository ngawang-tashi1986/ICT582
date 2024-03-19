year = int(input("Enter a year (YYYY) : "))

if year%400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year")
#elif year % 4 == 0 and year % 100 != 0:
#    print("The year is a leap year")
else:
    print("The year is not a leap year")