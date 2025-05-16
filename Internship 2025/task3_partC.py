#Write a program that takes two numbers as input and prints whether the first number is greater, smaller, or equal to the second number.


print("Welcome to Number Comparison")

num_1 = int(input("\t\n Enter Number 1"))
num_2 = int(input("\t\n Enter number 2"))

if num_1 > num_2:
    message = "\t\n Number 1 is greater than Number 2"
elif num_1 < num_2:
    message = "\t\n Number 1 is Less than Number 2"
elif num_1 == num_2:
    message = "\t\n Number 1 is equal to Number 2"

print(message)