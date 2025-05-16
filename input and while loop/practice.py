# 1. Moving items from one list to another

#=> To do so One way is to => We use While loop to pull the items from one list and add them to a separate list

''''
UnVerified_users = ["iron-man", "bat-man", "super-man", "hulk", "bruce-avn", "tony-stark", "Dr-Strange", "spider-man"]

Verified_users = []

while UnVerified_users:
    current_user = UnVerified_users.pop()
    print(f"\n Verifying UnVerified users:- {current_user.title()}")

    Verified_users.append(current_user)

#Displaying Verified users

print("\n List of verified users:-")

for Verified_user in Verified_users:
    print(f"\n Verified Users:- {Verified_user.title()}")

'''

'''
unverified_users = ["alice", "brain"]

verified_users = []

while unverified_users:
    user = unverified_users.pop()

    print(f"verifying users:- {user}")

    verified_users.append(user)

print(f"List of verified user")
for verified_user in verified_users:
    print(verified_user)




pets = ["dog", "cat", "rabbit", "cat", "goldfish", "cat", "dog", "cat"]

while 'cat' in pets:
    pets.remove('cat')
print(pets)

'''

# Pooling Result

result = {}

active = True

while active:
    vaoter_name = input("\n Enter your voter id name:- ")
    votting_done = input("\n Voting Done? Yes/No")

    result[vaoter_name] = votting_done

    Exit = input("\n would you like to exit? yes/no")

    if Exit == 'yes':
        active = False

print("\n ------ Poll Result ------")

for vaoter_name, votting_done in result.items():
    print(f"\n {vaoter_name} = {votting_done}")
