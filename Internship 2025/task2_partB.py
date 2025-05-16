import math

a = float(input("\t\n Enter the coefficient a: "))
b = float(input("\t\n Enter the coefficient b: "))
c = float(input("\t\n Enter the coefficient c: "))


discriminant = b**2 - 4*a*c


if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"\t\n The roots are real and different: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"\t\n The root is real and the same: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-discriminant) / (2 * a)
    print(f"\t\n The roots are complex: {real_part} ± {imaginary_part}i")