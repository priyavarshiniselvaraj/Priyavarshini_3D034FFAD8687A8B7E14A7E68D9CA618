# Prompt the user for input
year = int(input("Enter a year: "))

# Check if the year is divisible by 4
if (year % 4 == 0):
    # Leap years are usually divisible by 4, but not by 100, unless they are divisible by 400
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
      