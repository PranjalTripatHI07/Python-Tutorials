#Here we test the function

from Testing_a_function import get_formatted_name

print("\n Enter end to end the program.")

while True:
    first_name = input("\n Enter your first name: ")
    if first_name == "end":
        break
    last_name = input("\n Enter your last name: ")
    if last_name == "end":
        break

    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\n {formatted_name}")