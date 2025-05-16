#DATE - 12/3/2025

# Addition Calculator

def addition_calculator():
    while True:
        try:
            num1 = int(input("\n Enter the first number: "))
            num2 = int(input("\n Enter the second number: "))
            result = num1 + num2
            print(f"\n The sum of {num1} and {num2} is {result}")
        except ValueError:
            print("\n The value entered is not a integer. Please try again.")


addition_calculator()

