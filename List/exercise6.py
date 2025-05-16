#DATE - 2/1/2025

for number in range(1,21):
    print(number)
    
users = []
for user in range(1, 1000000):
    users.append(user)
print(users)

users = [user for user in range(1, 1000000)]
print(users)
print(min(users))
print(max(users))
print(sum(users))

odd_number = [odd for odd in range(1,21,2)]
print(odd_number)

for odd_number in range(1,21,2):
    print(odd_number)
    
users = [user*3 for user in range(1,31)]
print(users)

users=[]
for user in range(1,31):
    multiple_of_three = user*3
    users.append(multiple_of_three)
print(users)

numbers = [number**3 for number in range(1,11)]
print(numbers)

numbers = []
for number in range(1,11):
    cube = number**3
    numbers.append(cube)
print(numbers)