'''
Calculate Hypotenuse:
Write a Python program that takes the lengths of the two sides of a right-angled triangle as input and calculates
the length of the hypotenuse using the math.hypot function.

'''

import math

print("\n Welcome to Hypotenuse Calculator:- ")

length = int(input("\n Enter length of a right-angle triangle:- "))
Breadth = int(input("\n Enter breadth of a right-angle triangle:- "))

calculate_hypotenuse = math.hypot(length, Breadth)

print(f"\n The length of the hypotenuse is: {calculate_hypotenuse}")