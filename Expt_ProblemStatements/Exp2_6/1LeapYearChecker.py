def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

# Ask user to input the year
year = int(input("Enter a year: "))

# Check if the year is a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")