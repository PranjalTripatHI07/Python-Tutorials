#DATE - 30/1/2025
'''
pizza_topping = "\n Enter Your Pizza Topping"

pizza_topping += "\n Enter 'end' to end the topping list"

active = True

while active:
    topping = input(pizza_topping)

    if topping == 'end':
        active = False
        break
    else:
        print(f"\n We will add:- {topping.title()}")

   '''
from List.Name import message

# Movie Ticket
'''
age = int(input("Enter your age"))

while age:
    if age <= 3:
        print("Your ticket is free")
    elif age <= 12:
        print("Your ticket charge is 5$")

    elif age > 12:
        print("Your Ticket charge is 15$")

    break
'''

# Three Exit

# In this code we use conditional test directly in while loop to exit the task
'''
pizza_prompt = "\nEnter the name of topping you want"
pizza_prompt += "\nEnter 'end' to end task: "

msg = ""  # Initialize message variable
while msg != 'end':  # Continue loop until 'end' is entered
    msg = input(pizza_prompt)
    if msg != 'end':  # Only print if not 'end'
        print(f"I'll add {msg} to your pizza!")

'''


# In this code we use Flag to control or exit the task
'''
pizza_topping = "\n Enter the name of topping you want"
pizza_topping += "\n Enter 'end' to end the task"

active = True

while active:
    msg = input(pizza_topping).lower()
    if msg == 'end':
        active = False
    else:
        print(f"I will add {msg} to your pizza!")
'''


# In this code we use break statement to exit the loop when user enter end value

pizza_topping = "\n Enter the name of topping you want"
pizza_topping += "\n Enter 'end' to end the task"

msg = ""

while msg != 'end':
    msg = input(pizza_topping)
    if msg == 'end':
        break
    else:
        print(f"I will add {msg} to your pizza!")
