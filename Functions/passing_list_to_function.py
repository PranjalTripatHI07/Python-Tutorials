#DATE - 5/2/2025

# Topic -  Passing a list to a function

# => We can pass list and dictionaries to a function
# => When we pass list and dictionaries to a function the function gets direct access to the items of list and dictionaries

# Example

#Note =>  In the below code  we pass list name usernames to the function parameter name as => names
# and inside the function we use for loop to loop through the list

#Note => So to pass a list and dictionary to a function we simply pass the name of the list and dictionary to the function argument

def greet_user(names):
    for name in names:
        print(f"\n Hello {name.title()}!")


usernames = ["iron-man", "Bruce-van", "willie-van", "super-man", "bat-man"]

greet_user(usernames)



# Topic => Modifying a list in a function

design_needto_print = ["phone case", "robot-pendent", "dodecahedron", "iron-man suit", "bat-man suit"]
design_printed = []

while design_needto_print:
    current_deisgn = design_needto_print.pop()

    design_printed.append(current_deisgn)

for designprinted in design_printed:
    print(designprinted)

# Note => When we pass a list to a function the can modify the list
# => Any changes made to the list inside function body are permanent
# => We can always call a function from another function

# Modifying a list by using functions:-

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_state = unprinted_designs.pop()
        print(f"\n printing model: {current_state}")
        completed_models.append(current_state)


def show_completed_models(completed_models):
    print("\n Below models are printed")
    for completed_model in completed_models:
        print(f" {completed_model}")


unprinted = ["phone case", "robot-pendent", "dodecahedron", "iron-man suit", "bat-man suit"]
completed = []

print_models(unprinted_designs=unprinted, completed_models=completed)
show_completed_models(completed_models=completed)



# Topic => Preventing a Function from Modifying a list
# For preventing the function to modify list we just simply create a copy of original list
# and all the changes are made in copy list not in original list
# so to do so
# the syntax is => name_of_function(name_of_list[:]) or  name_of_function(name_of_parameter = name_of_list[:]) # we do this when we call a function

# Note =>  we just simply add name_of_list[:] inside a function parameter and this creates a copy of original list
# Note => name_of_list is representing a list and The slice notation [:] makes a copy of the original list which is
# are passing as a parameter in the function

# Note =>  We do this if we don't want empty the original list

# Example


def print_designs(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_state = unprinted_designs.pop()

        print("\n List of unprinted designs {current_state}")

        completed_designs.append(current_state)


def show_completed_designs(completed_designs):
    for complete in completed_designs:
        print(complete)


unprinted = ["phone case", "robot-pendent", "dodecahedron", "iron-man suit", "bat-man suit"]

completed = []


# Here below we created copy of original list => this slice notation [:] makes a copy of original list and all the changes are
# going to made in the copy of that original list without affecting or making any changes in the original list
print_designs(unprinted_designs=unprinted[:], completed_designs=completed)

show_completed_designs(completed_designs=completed)



# another example

def salary(salary_unpaid, salary_paid):
    while salary_unpaid:
        current_status = salary_unpaid.pop()

        print(f"\n Name of employ who have not received their salary:- {current_status}")

        salary_paid.append(current_status)

def show_employ_received_salary(salary_paid):
    for salary_received in salary_paid:
        print(f"\n Name of Employ who have received salary:- {salary_received}")


unpaid_salary = ["bruce-van", "tony-stark", "hulk", "supper-man", "bat-man", "dr-strange"]
paid_salary = []

salary(salary_unpaid=unpaid_salary[:], salary_paid=paid_salary)
show_employ_received_salary(salary_paid=paid_salary)

