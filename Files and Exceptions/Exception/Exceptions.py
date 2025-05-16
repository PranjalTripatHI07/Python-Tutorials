#DATE - 8/3/2025

#Topic => Exceptions

#=> Python Uses special object called Exceptions to manage error that arise during a program execution
#=> In Python Exceptions are handled with => try except blocks

#=> try except blocks => try except blocks tells python what to do if an exception is raised


#1. Handling The ZeroDivisionError Exception

#print(5/0) #=> This shows ZeroDivisionError Exception

#Now to handle this we use try-except block

#syntex =>  try:
#              do something
#           except name_of_exception:
#              do something

try:
    print(5/0)
except ZeroDivisionError:
    print("You can not divide by zero")


#Note => If we don't know the name of Exception then in that case we simply use Exception Keyword

#like this
try:
    print(5/0)
except Exception:
    print("You can not divide by zero")



#Topic => Using Exception to Prevent crash

# For that we use else block

#syntax => try:
#            do something
#          except Exception:
#            do something 
#          else:
#            do something

# Let's create a simple calculator

print("\n Give me two numbers and i will divide them")
print("\n Enter finish to end the calculation")

while True:
    num_1 = input("\n Enter first number ")
    if num_1 == "finish":
        break
    num_2 = input("\n Enter Second Number ")
    if num_2 == "finish":
        break

    try:
        division = int(num_1)/int(num_2)
    except Exception:
        print("\n You cannot divide by 0")
    else:
        print(f"\n Division of your {num_1} and {num_2} is {division} ")


#Note => Any code written inside or depends on the try block when the try block code executed successfully it added to the else block
#like in the above example
#=> if the division operation written inside try block executed successfully we use else block to print the result
#Note => The only code that should go in a try block is code that might cause exception




#Topic=> Handling The FileNotFound Error Exception

#=> To handle this we use Try Except block

#syntax and example

from pathlib import Path

file_location = Path("handling_file_not_found_exception.txt")

try:
    content = file_location.read_text()
except FileNotFoundError:
    print("\n Sorry File Not Found")

# Analyzing Text

from pathlib import Path

file_location = Path("demo_file.txt")

try:
    file_content = file_location.read_text()
except FileNotFoundError:
    print("\n Sorry File Not Found")

else:
    file_content.split()
    line_length = len(file_content)
    print(f"\n The file {file_location} has about {line_length} lines")



#Topic => Working with multiple files
#=> We can add multiple files

#syntax and Example

from pathlib import Path

def count_word(filenames):
    try:
        file_content = filenames.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("\n Sorry File Not Found")

    else:
        file_content_length = len(file_content)
        print(f"\n The file {filenames} has about {file_content_length} words")

filenames = ["alicewonderland.txt", "camping.txt","money_mind", "trending.txt"]
for filename in filenames:
    file_location = Path(filename)
    count_word(file_location)



#Topic => Failing Silently

# We can handle error silently by simply passing except block (means we use pass keyword inside except block)

#syntax =>   try:
#              do something
#            except Name_of_Error:
#              pass
#            else:
#              do something

#Note => To make a program fail silently we write a try block as usual, but we explicitly tell Python to do nothing in except block
# Python has a Pass Statement that tells it to do nothing in a block


# example

from pathlib import Path

def count_words(filenames):
    try:
        file_content = filenames.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        file_location = Path(filenames)
        file_content_length = len(file_content)
        print(f"\n The file {filenames} has about {file_content_length} words")

filenames = ["alicewonderland.txt", "camping.txt", "money_mind.txt", "trending.txt"]
for filename in filenames:
    file_location = Path(filename)
    count_words(file_location)



#Topic => Storing Data

#=> We can store data using JSON module

#Note => JSON(JavaScript Object Notation) Module allows us to convert simple python data structures into JSON formatted
# Strings and load data from that file the next time the program runs

#=> We can also use JSON to share data between different python programs


#1. Using json.dumps() and json.loads()

#=> json.dumps() function used to store a set of information

#=> json.dumps() function take one argument :-> A piece of data that should be converted to the json format

#=> Basically json.dumps() function in python coverts a python object into a json formated string

#=>  it is majorly used for feeding information to API which required printed data

#syntax => json.dumps(data)

#example

from pathlib import Path
import json

number = [1,2,5,8,24,14]
path = Path("numbers.json")
content = json.dumps(number)
print(path.write_text(content))


