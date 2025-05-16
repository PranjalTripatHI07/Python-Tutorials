#if statement code

age = 27
if age >= 18:
    print("you can vote")
    print("have you voted ??")

# if-else statement

age = 15
if age >= 18:
    print("\n you can vote")
    print("\n have you voted")
else:
    print("\n sorry you can't vote")
    print("\n try next time")


# if-elif-else statement

age = 14

if age <= 4:
    print("Admission is free")
elif (age > 4) and (age <= 18):
    print("Admission fee is $25")
elif age > 18:
    print("Admission fee is $45")


age = 21

if age <= 4:
    price = 0
elif (age > 4) and (age <= 18):
    price = 25
elif (age > 18) and (age <= 30):
    price = 30
else:
    price = 45
print(f"Admission fee is ${price}")