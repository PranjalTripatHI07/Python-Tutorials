#DATE - 12/2/2025

#Topic => Modules

# => Modules => Storing functions that performs a specific tasks in a separate file is called module

#=>  We can use that module file by importing thar module file into our main program

#=> An import statement tells python to make the code in module available in the currently running file

# Ways To import file 0r storing functions in module:-

# 1. Importing an Entire Module

#=>  To start importing functions we first need to create a module file
#=> Module file => Module file is a python file that contains code we want to import into other python programs files

#Note => When we make module and import that module we have to make sure that both the files are in same directory

#=> To call a function from an imported module => Syntax => Module_name.function_name(arguments)  #Here we first write the name of our module we imported and then a dot then name of function we want to use from that module

#Example

# Step1 => First we create a module file name (Make_pizza.py) Which performs a specific function

# => Inside Make_pizza.py file

def make_pizza(size, *toppings):
    print(f"\n Make a {size} pizza with the following toppings:- ")

    for topping in toppings:
        print(f"\n -{topping}")




# Step2 => Now we go to our main program file suppose the file name is (Pizza.py)

# => Inside that file We first import the module file (name => Make_pizza.py)

import Make_pizza

# After Importing that module file into our main program file we can use the functions of that module file

# for using that module after importing that file =>

# syntax => name_of_the module_file.name_of_the_function(arguments)

Make_pizza.make_pizza("large", "peperoni", "mushroom", "chilli-garlic", "capsicum")

#Note =>  The first approach to importing is you simple write import followed by the name_of_the_module , which makes every function
# from the module available in your main program file



#2 => Importing specific function from a module

# We can import specific function form a module
# Syntax => from name_of_module import name_of_function


# we can import as many functions we want from a module by separating each functions_name with comma
#synatx => from name_of_module import name_of_function1, name_of_function2 .....

# And for using those functions or calling those functions

#syntax => name_of_function(arguments)


#final syntax =>

# from name_of_module import name_of_function
# name_of_function(arguments)

#Example
from Module1 import make_pizza

make_pizza("large", "peperoni", "mushroom", "chilli-garlic", "capsicum")




#3. Using as To give a function an alias

#alias => alias is an alternate name or nickname for the function we use when the name of function we are importing might conflict with an existing name in our main program
#=> So basically we use (as) for giving a nickname to our module function which we are using in our main program

#syntax => from module_name import function_name as fun #=> so here fun is a nickname of function_name

#          fun(arguments)  # here we use that function

# Example

from Module1 import make_pizza as mp

mp("large", "peperoni", "mushroom", "chilli-garlic", "capsicum")




#4. Using as to give a module an alias

#=> We can also provide alias or nickname for a module name

#syntax => import module_name as module_nickname

#          module_nickname(arguments)

# Example

import Module1 as Mo

Mo.make_pizza("large", "peperoni", "mushroom", "chilli-garlic", "capsicum")



#5. Importing all function in a module
#=> We can import every function in a module by using the * sign

#syntax => from module_name import *
#          function_name(arguments)

# Note => The * sign in the import statement tells python to copy every function from the module into the main program file
#=> Because every functon is imported you can call each function by name without using the dot notation

#Example

from Module1 import *

make_pizza("large", "peperoni", "mushroom", "chilli-garlic", "capsicum")

