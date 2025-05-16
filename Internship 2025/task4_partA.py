print("\t\n Welcome to BMI Calculator")
weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi < 24.9:
    category = "normal weight"
elif 25 <= bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is: {bmi}")
print(f"You are categorized as: {category}")