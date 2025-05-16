#DATE- 8/1/2025

#checking of special items
toppings = ["mango", "apple", "peperoni", "icecream"]

for topping in toppings:
    print(f"adding {topping}")

print(f"Pizza is ready")


#Checking of special item using if and for loop

toppings = ["green-paper", "mushroom", "peperoni", "extra-cheese" ]

for topping in toppings:
    if topping == "green-paper":
        print(f"{topping} is out of stock choose other options")
    else:
        print(f"Adding {topping}")
print("Pizza is ready")

#Checking list is not empty

toppings = []

if toppings:                        #besically for safe side we run for loop inside if statement so that if the list is empty we know it early
    for topping in toppings:
        print(f"Adding {topping}")
    print("\n Pizza is ready")
else:
    print("\n sorry topping is out of stock")


#using multiple list or working with multiple list

available_toppings = ["mushroom", "peperoni", "extra-cheese", "green-peper"]

requested_toppings = ["french-fries", "chocolate", "extra-cheese", "peperoni"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\n Adding {requested_topping}")
    else:
        print(f"\n sorry {requested_topping} is not available")
print("\n Pizza is ready")



