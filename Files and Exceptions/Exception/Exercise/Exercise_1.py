#DATE - 12/3/2025

#Addition

def Addition():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"\n The sum of {num1} and {num2} is {result}")
    except ValueError:
        print(f"\n The value entered is not a integer. Please try again.")

Addition()

