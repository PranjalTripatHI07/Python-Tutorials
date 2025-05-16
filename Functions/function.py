#DATE - 1/2/2025

#Topic -> Function

# Functions => Function is a block of code used for doing specific task
# => We can call function multiple times throughout the program

#Syntax => def name_of_function():
#               do something

#Example

def greeting():       # Here we define a function
    """Greeting others"""   # """""" => this is docstring which used to write text and which basically describes what function actually does
    print("\n Hello")

greeting()           # Here we call that function



# Passing information to a function
# 1. parameter
# 2. argument

# 1. Passing parameter and argument to function
#syntax => def name_of_function(parameter):  # Defining a function
#              do something
#          name_of_function(argument)   # calling a function

# Parameter => Parameter is a piece of information that function needs to do its task.

# Argument => Argument is a piece of information which is passed when we call a function to execute a task

# Note =>  We can pass multiple Parameter and multiple argument

# Example

def greet_user(username):  # Here username is a parameter
    print(f"\n Hello {username}")

greet_user("Bruce Van") # Here Bruce van is a argument # note => argument basically assign value to parameter
greet_user("Iron man")
greet_user("super-man")
greet_user("Hulk")


# Topic -  Passing argument

# => In function we can pass multiple Parameters so calling a function we may need multiple argument

# We can pass argument in the below ways:-
# 1. Position argument
# 2. Keyword argument

# Position argument => Position argument are passed in  same order as the Parameter is written

#synatx => def name_of_function(parameter1, parameter2):
#                     do something
#          name_of_function(argument1, argument2) #Here argument1 is aligned with parameter1 and argument2 is aligned with parameter2
# so in position argument order of argument passed is important

# Example

def pet(pet_name, pet_type):
    print(f" Hello My Pet name is {pet_name} and its a {pet_type}")

pet("iron-man", "dog")
pet("willie", "cat")  #multiple function calls

# Keyword argument => Keyword argument are passed in which each argument consists of a variable name and its value


#=> In keyword argument we directly associate the name and the value within the argument

#=> In keyword argument order is not imp

#syntax => def name_of_function(parameter1, parameter2):
#                    do something
#          name_of_function(parameter1 = argument1, parameter2 = argument2)

# In keyword argument we explicitly tell python which parameter each argument should be matched with
# In keyword argument order is not important

#Note => When we use keyword argument be sure to use the exact name of the parameter in function definition

# Example

def pets(pets_name, pets_type):
    print(f"\n Hello My pet name is {pets_name} and its a {pets_type}")

pets(pets_name= "willie", pets_type="dog") # Here In keyword argument  we assign a value or argument directly to parameter


# Topic => Default Values

#Default value =>  Default value is a default value which assign in Parameter

# So we can define a default value for each parameter
# if an argument for a parameter is provided in the function call, python uses the argument
# value if not it uses the parameter default value

#syntax =>  def name_of_function(parameter1, parameter2 = argument):
#                      do something
#           name_of_function(parameter1=argument1)
# or
#           name_of_function(argument1)


#Example

def pets(pets_name, pets_type = "dog"):
    print(f"Hello My pet name is {pets_name} and its a {pets_type}")

pets(pets_name="iron man")
#or
pets("willie")



# Topic  => Return Value

# => Return Value is the value the function returns is called Return value

# Syntax =>   def name_of_function(parameter):
#                    do something
#                    return name_of_variable  # Here we use return keyword to return the value of variable we want to return

#             random_variable_name = name_of_function(argument)
#             print(randon_variable_name)


#Example

def fullName_generator(first_name, last_name):
    full_name = f"\n {first_name} {last_name}"
    return full_name.title()

generator = fullName_generator(first_name="willie", last_name="iron")
print(generator)


# Making an Argument optional

#=> To make an Argument Optional we use default value

# Example

def full_name_generator(first_name, last_name, middle_name= ""):
    full_name = f"\n {first_name} {middle_name} {last_name}"

    return full_name.title()

generate_full_name = full_name_generator(first_name="willie", last_name="man")
print(generate_full_name)
generate_full_name = full_name_generator(first_name="Iron", last_name="man", middle_name="tony")
print(generate_full_name)


# or

def full_name_generator(first_name, last_name, middle_name= ""):
    if middle_name:
        full_name = f"\n {first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n {first_name} {last_name}"

    return full_name.title()

generate_full_name = full_name_generator(first_name="willie", last_name="man")
print(generate_full_name)
generate_full_name = full_name_generator(first_name="Iron", last_name="man", middle_name="tony")
print(generate_full_name)


