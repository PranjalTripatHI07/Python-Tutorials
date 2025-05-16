#DATE - 10/2/2025
from Dictionary.Exercise15 import country
from Dictionary.nesting import user_info, location


# Topic => Passing an Arbitrary Number of arguments

# => Python allows function to collect an arbitrary number of arguments from the calling function statement

# => In Python Arbitrary number of arguments are handled by two ways
#    1. *args => (for Positional Arguments) => arguments are collected into tuples
#    2. **kwargs => (for Keyword Arguments) => arguments are collected ito dictionary

#Note =>  In short => Arbitrary number of arguments helps us to pass multiple number of arguments for a specific parameter

#   1. Using Arbitrary positional Argument:-

#Note => While defining a function => for Positional argument we use single *(star) before parameter
# syntax =>  def name_of_function(*name_of_parameter):
#                     do something
#            name_of_function(multiple_value,multiple_value,multiple_value,multiple_value,multiple_value)  # => Here we calling the argument with multiple values


#Example

def make_pizza(*toppings):
    print("\n Print the list of toppings that have been requested")
    print(f"\n {toppings}")


make_pizza('peperoni')
make_pizza('mushrooms', 'etra-cheese', 'onion-peperoni', 'chilli-onion', 'capsicum')


# Now using loop

def make_pizza(*toppings):
    print(f"\n Make a pizza with the following toppings:- ")

    for topping in toppings:
        print(f"\n - {topping.title()}")


make_pizza('peperoni')
make_pizza('garlic-peperoni', 'mushrooms', 'cilli-garlic-peperoni', 'capsicum', 'extra-cheese')



#Note => If you want a function to accept different kinds of arguments the parameter that accepts an arbitrary number of arguments must be
# placed last in the function definition

# example => if the function needs to take in a size for the pizza, that parameter must come before the parameter *topping

# syntax => def name_of_function(parameter1, *parameter2): => like this => here we write parameter1 first and *parameter2(arbitrary parameter) last

# Example

def make_pizza(size, *toppings):
    print(f"\n Making a {size.title()} pizza with the following toppings:- ")

    for topping in toppings:
        print(f"\n -{topping.title()}")


make_pizza('small', 'peperoni')
make_pizza('large', 'peperoni', 'mushrooms', 'garlic-peperoni', 'extra-cheese', 'chilli-mix-peperoni')


#Topic =>  2. Using Arbitrary Keyword Argument:-

#Note => While defining a function => for Keyword argument we use double **(double star) before parameter

#Syntax => def name_of_function(**parameter):
#                     do something
#          name_of_function(name_of_parameter = "multiple values", "multiple values", "multiple values", "multiple values","multiple values")    # => Here we calling the argument with multiple values


# Example

def build_profile(first_name, last_name, **user_info):
    print("\n  Displaying user profile information:- ")

    user_info['firstname'] = first_name
    user_info['lastname'] = last_name
    return  user_info


user_profile = build_profile("Willie", "van", Country = "usa", city = "new-york")

print(user_profile)

# Another Example

def build_user_profile(**user_info):
    print("\n Display user profile information: -")

    return user_info

user_profile = build_user_profile(first_name = "Willie", last_name = "van", country = "Usa", city = "new-york", username ="willieVan")

print(user_profile)


# Note => **asterisk before the parameter tells python to create a dictionary called name_of_parameter with **asterisk which contains
# all the extra name-value pairs the function receives

#Note =>  The function will work no matter how many additional key-value pairs are provided in the function call

#Note =>  We can mix positional, keyword and arbitrary values in many different ways

#Note =>  The parameter name **Kwargs used to collect non-specific keyword arguments



