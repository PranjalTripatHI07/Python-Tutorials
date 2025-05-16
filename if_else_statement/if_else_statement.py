#DATE - 5/1/2025

# In this we learn about if conditional statement in python

cars = ["audi", "thar", "renault-duster", "bugatti", "bmw"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


#And or operators uses

Age_1 = 18
Age_2 = 22

if (Age_1 >= 18) and (Age_2 >= 22):
    print("condition true")
else:
    print("condition false")

age1 = 18
age2 = 25

if (age1 >= 18) or (age2 >= 27):
    print("condition true")
else:
    print("condition false")


# use of not in a list
bikes = ["honda", "apache", "pulsher", "bmw"]
bike = "tvs"
if bike in bikes:
    print("bike is present")
if bike not in bikes:
    print("bike is not present")