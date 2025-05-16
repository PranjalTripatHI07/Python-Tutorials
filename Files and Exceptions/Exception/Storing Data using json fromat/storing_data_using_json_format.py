#DATE - 13/3/2025

#Topic => Storing Data

#=> We can store data using JSON module

#Note => JSON(JavaScript Object Notation) Module allows us to convert simple python data structures into JSON formatted
# Strings and load data from that file the next time the program runs

#=> We can also use JSON to share data between different python programs


#1. Using json.dumps() and json.loads()

#=> json.dumps() function used to store a set of information

#=> json.dumps() function take one argument :-> A piece of data that should be converted to the json format

#=> Basically json.dumps() function in python coverts a python object or data into a json formated string

#=>  it is majorly used for feeding information to API which required printed data

#syntax => name_of_variable = json.dumps(name_of_data_variable)

#example

from pathlib import Path
import json

data = [1,4,8,14,20,24]

file_path = Path("numbers.json")

file_content = json.dumps(data)

print(file_path.write_text(file_content))

#another example

my_dictionary = {"name":"willie van", "age":24}

json_data = json.dumps(my_dictionary)
print(json_data)

# another example

from pathlib import Path
import json

file_path = Path("numbers.json")
dictionary_data = {"name":"willie van", "age":24}
my_json_data = json.dumps(dictionary_data)

print(file_path.write_text(my_json_data.title()))



#2. json.loads() function
#=> json.loads() function converts json formatted string into a python object or python dictionary
#=> Basically json.loads() function is opposite  of json.dumps() function

#=> syntax => name_of_variable = json.loads(name_of_variable)
#or
#=>  name_of_variable = json.loads(name_of_data_variable)

from pathlib import Path
import json

file_path = Path("numbers.json")

file_content = file_path.read_text()

json_data_content = json.loads(file_content)
