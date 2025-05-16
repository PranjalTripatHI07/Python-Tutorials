#DATE - 23/2/2025

#Topic => Importing Classes

#1. First we create a separate python module file
#2. Second we create another python file where we use the above module file
#3. To use the functionality of that module file into our program file we import that file
#4. Below is the syntax to import class module file
#5. syntax => from module_file_name import class_name   (Note => We import that class of which we want to use the functionality)

#Example
from car_class_module import Car

test2 = Car("Nishan", "NISHAN45", 2024)

print(test2.get_details())  #See Its working


#Topic => Storing Multiple class in a module

#=> We can store as many classes as we want in a single class module

# Steps

# 1. We have to create multiple classes inside the class module file

# 2. Syntax => from module_file_name import class_name

# => Then we import the class we want to use into our main program file from that module file


# Importing multiple classes from a module

# We can import as many classes as we want
#Steps =>
# 1. First We have to create a multiple classes inside module file

# 2. Then we can import multiple classes into our main program file

#syntax => from module_file_name import class_name1, class_name2, ......

#Note => We can import multiple classes from a module file by separating each class with a comma



# Topic => Importing an entire module

# => We can also import an entire module and then access the class we need using dot notation

#syntax => import module_file_name

#=>        object_name = module_name.class_name(arguments)




# Topic => Importing All classes from a module
#=> We can import every class from a module

#=> Syntax => from module_file_name import *



#Topic => Importing module into a module

#=> We can import module file into another module file
# and then we can import that module file into our main program file to use the functionality




# Topic => Using Aliases or nickname
#=> We can give class an aliases(nicknames)

#=> Syntax => from module_file_name import class_name as class_nickname

from car_class_module import Car as car_class

test5 = car_class("Audi", "AU", 2020)
print(test5.get_details())


#=> We can also give whole module file a  aliases(nickname)

#=> Syntax => import module_file_name as nickname_of_module_file

import  car_class_module as carclass_module

test6 = carclass_module.Car("Mustang", "MG", 2020)
print(test6.get_details())