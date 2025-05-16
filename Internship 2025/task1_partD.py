print("Welcome to BMI Calculator")
weight = float(input("\t\n Enter your weight in kilograms: "))

height = float(input("\t\n Enter your height in meters: "))


bmi = weight / (height * height)

print(f"\t\n Your BMI is: {bmi}")