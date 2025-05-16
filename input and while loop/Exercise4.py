#DATE - 1/2/2025
# 1
sandwich_order = ["veg sandwich", "ver grill sandwich", "veg cheese sandwich", "veg cheese grill sandwich", "corn sandwich", "corn cheese sandwich"]
finished_sandwich = []


while sandwich_order:
    current_order = sandwich_order.pop()

    print(f"\n I made your:- {current_order} ")

    finished_sandwich.append(current_order)

print("\n ---------- List of Finished Sandwiches ----------")

for sandwich in finished_sandwich:
    print(sandwich)

# 2
sandwich_order = ["veg sandwich", "ver grill sandwich", "pastrami", "veg cheese grill sandwich", "corn sandwich",
                  "pastrami"]

finished_sandwich = []

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')
print("\n we have no pastrami")

while sandwich_order:
    current_order = sandwich_order.pop()

    print(f"\n I made your:- {current_order} ")

    finished_sandwich.append(current_order)

print("\n ---------- List of Finished Sandwiches ----------")

for sandwich in finished_sandwich:
    print(sandwich)

# 4

dream_vacations = {}

dream_active = True

while dream_active:
    name = input("\n Enter your name :- ")
    dream_vacation = input("\n Enter your dream destination :- ")

    dream_vacations[name] = dream_vacation

    exit_poll = input("Would you like to exit poll? yes/no")

    if exit_poll == 'yes':
        dream_active = False

print("\n ------- Poll Result ---------")

for name,dream_vacation in dream_vacations.items():
    print(f"\n {name} = {dream_vacation}")