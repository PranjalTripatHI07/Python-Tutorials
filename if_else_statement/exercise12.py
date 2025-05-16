#DATE - 10/1/2025

users = ["iron-man", "super-man", "spider-man", "thor", "hulk", "admin"]

for user in users:
    if user == "admin":
        print(f"Hello {user} would you like to see a status report")
    else:
        print(f"Hello {user} thankyou for login again")


# checking list is not empty
Users = []
if Users:
    for user in Users:
        print(f"Hello {user}")
else:
    print(f"\n we need to find some users")


# using multiple list
current_users = ["iron-man", "super-man", "spider-man", "thor", "hulk", "admin"]
new_users = ["bat-man", "admin", "odin", "thor", "iron-man"]

current_users = [user.lower() for user in current_users]

for user in new_users:
    if user in current_users:
        print(f"\n {user} is already taken enter other username")
    else:
        print(f"\n {user} is available")
print("\n thanks for login")


#ordinal number

ordinal_number = [number for number in range(1,11)]
for number in ordinal_number:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")