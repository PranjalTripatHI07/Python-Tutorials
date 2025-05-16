#DATE - 4/2/2025
from Dictionary.nesting import full_name
from Functions.function import greet_user


#Topic => Using Function with While loop

# Example
'''
def greet_user(first_name, last_name):
    full_name = f"\n {first_name} {last_name}"
    return full_name.title()


while True:
    print("\n Pls Enter your name:- ")
    first = input("\n Enter first name")
    last = input("\n Enter last name")

greeting = greet_user(first_name = first, last_name = last)

print(f"\n Hello {greeting}")
'''

# more optimize way

def greet_users(first_name, last_name):
    full_names = f"\n {first_name} {last_name}"
    return full_names.title()

while True:
    print("\n Enter 'end' to stop")

    first = input("\n Enter first name:- ")
    if first == 'end':
        break
    last = input("\n Enter last name:- ")
    if last == 'end':
        break

    greeting_user = greet_users(first_name = first, last_name = last)
    print(f"\n Hello{greeting_user}")


