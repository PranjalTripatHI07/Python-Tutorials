from Functions.Function_with_whileloop import first


def greet(persson_name):
    print(f"\n Hello {persson_name.title()} how are you")

greet('iron-man')
greet('bruce-van')



def greet_user(first_name, last_name, middle_name = ""):
    full_name = f"\n {first_name} {middle_name} {last_name} "
    return full_name.title()

while True:
    first = input("\n Enter Your first name")
    if first == "end":
        break
    middle = input("\n Enter Your middle name")
    if middle == "end":
        break
    last = input("\n Enter your last name")
    if last == "end":
        break

    greet = greet_user(first_name=first, last_name=last, middle_name=middle)
    print(f"\n Hello {greet}")




# passing list to a function

def print_design(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_state = unprinted_designs.pop()

        print(f"\n List of Unprinted designs:- \n {current_state}")

        completed_designs.append(current_state)


def print_completed_designs(completed_designs):
    for completed_design in completed_designs:
        print(f" {completed_design}")


unprinteds = ["phone case", "robot-pendent", "dodecahedron", "iron-man suit", "bat-man suit"]
completeds = []

print_design(unprinted_designs=unprinteds, completed_designs=completeds)
print_completed_designs(completed_designs=completeds)