# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to check if a given number is a factorial
def is_factorial(number):
    i = 0
    while True:
        i += 1
        if factorial(i) == number:
            return True
        elif factorial(i) > number:
            return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is a factorial
if is_factorial(num):
    print(f"{num} is a factorial number.")
else:
    print(f"{num} is not a factorial number.")
      