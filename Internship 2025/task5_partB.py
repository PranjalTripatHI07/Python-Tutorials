'''
B. Calculate Area of a Triangle:
Write a function that takes the lengths of the three sides of a triangle as input and calculates the area using Heron's formula.

'''

import math

def calculate_area_of_triangle(length, breadth, hypotenuse):

    s = (length + breadth + hypotenuse) / 2
    area = math.sqrt(s * (s - length) * (s - breadth) * (s - hypotenuse))

    return area

length  = float(input("\n Enter the length of the first side: "))
breadth = float(input("\n Enter the length of the second side: "))
hypotenuse = float(input("\n Enter the length of the third side: "))

area = calculate_area_of_triangle(length, breadth, hypotenuse)

print(f"\n The area of the triangle is: {area}")