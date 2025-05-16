#DATE - 29/1/2025
'''

# While loop => While loop runs as long as certain condition is true.

current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
'''

# Example => letting user choose when to end game
'''
prompt = "\n Tell me something and I will repeat it back to you: "
prompt += "\n Enter 'end' to end the program"

message = ""
while message != 'end':
    message = input(prompt)
    if message != 'end':
        print(message)
'''

#Using Flag
#Flag => Flag is a concept which act as a signal to check whether a entire program is active or not

#Example
'''
prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\n Enter 'end' to end the program"

active = True # Here active is a variable which act as Flag or we can say active is Flag

while active:
    message = input(prompt)
    if message == 'end':
        active = False
    else:
        print(message)
'''

# Using Break to exit the loop

# Break => Break statement is used to control the flow or program it basically used to control which line of code is executed and which are not

#Example
'''
prompt = "\n Enter the name of city you want to visit: "
prompt += "\n (Enter 'end' if you want to end this interaction)"

while True:
    city = input(prompt)
    if city == 'end':
        break
    else:
        print(city)

'''

# Using Continue in a loop

#Example Printing only odd number

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue    # Continue statement basically skip the if condition part.

    else:
        print(number)


