#DATE - 31/1/2025

#Using While loop with lists and Dictionaries

#note for loop is effective for looping through list. But we cannot modify a list inside a for loop
# So to modify the list as you work through it we use While loop.

# Use or Method 1

# 1. Moving items from one list to another

#=> To do so One way is to => We use While loop to pull the items from one list and add them to a separate list

#Exmaple

unconfirmed_users = ["alice", "brain", "candace", "david"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"\n Verifying Unconfirmed users- {current_user.title()}")
    confirmed_users.append(current_user)

#displaying User that has been confirmed after verification
print(f"\n lIST OF CONFIRMED USER AFTER VERIFICATION:-")
for confirmed_user in confirmed_users:
    print(f"\n Confirmed users:- {confirmed_user.title()}")


# 2. Removing all instances of specific values from a list

#=> suppose we have a multiple items in a list but one item repeated multiple times in a list
# so to remove all the instances of that one item we use While loop and remove() function

#Example


pets = ["dog", "cat", "rabbit", "cat", "goldfish", "cat", "dog", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)


# 3. Filling a Dictionary with user input
# note=> we can prompt as much inputs as we need in each pass through a while loop

#Note => Syntax => For filling a dictionary with user input or input => name_of_dictionary[key] = value
responses = {}

polling_active = True #we created a flag

while polling_active:
    name = input("\n  Enter your name")
    response = input("\n  Which location you want to visit")

# Stores the response in the dictionary'
    responses[name] = response

    # find out anyone else is going to take poll

    repeat = input("\n Would you like to let another person response? yes/no")

    if repeat == 'no':
        polling_active = False

print("\n ----- Poll Result -----")

for name, response in responses.items():
    print(f" {name} = {response}")