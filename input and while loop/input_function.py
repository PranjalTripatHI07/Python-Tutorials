#Date - 23/1/2025

# Use of input function
# syntax => name_of_variable = input("Enter message")
# Note => When you use input() function python thinks everything the user enters is sting.
# to deal with this we use the concept of type casting means we convert the string to other like int, float etc


# Example =>

message = input("Enter your name")

print(f"Hello {message.title()} How are you")



repeat_message = input("Enter some thing and i will repeat it")
print(repeat_message)

# Example

message_2 = int(input("\n How old are you : "))  # here to avoid error we use int() function to tell python that value
# is not string its integer

print(message_2)