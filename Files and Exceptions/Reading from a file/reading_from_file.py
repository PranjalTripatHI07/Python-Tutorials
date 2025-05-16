#DATE - 27/2/2025

#Topic Reading from a file
#=> When we  want to work with the information in a text file the first step is
# to read the file into memory

#1. Reading the content of a file

from pathlib import Path  # Pathlib is a module in Python that provides an object-oriented interface for handling filesystem paths.
                          # It simplifies path manipulations and operations such as creating,
                          # deleting, moving, renaming, reading, writing, finding, or splitting files.

                          # And Path is the class inside pathlib module file

path = Path("samplefile.txt") # create a path object(instance) for class Path and pass the text file name which we created as argument of Path class
show_file_content = path.read_text() # Create a variable and call the path object(instance) and use the Path class function name read_text()
                                     # This read_text() function basically read the text present inside the file


print(show_file_content)# Here we simply print the content of the file by calling the variable inside the print statement
#or
print(path.read_text())




#Topic => Relative and absolute file path

# There are two main ways to specify paths in programming

#1. Relative file path
# Relative file paths looks for a given location relative to the directory where the current running program file is stored

#syntax => path = Path("text_file_folder_name/filename.txt")

#2. Absolute file path
# Absolute file path we tell python exactly where the file is on our computer

#-> we can use absolute file path if relative file path won't work

#syntax => path = Path("/home/user/data_folder/file_folder_name/filename.txt")

#-> Using absolute file path we can read file from any location on our system



#Topic => Accessing a file lines

#=> We can use splitlines() method to turn a long string into a set of lines and then use a for loop to examine each line
# from a file one at a time

#Syntax =>
from pathlib import Path

path = Path("sample_text_5.txt")

file_contents = path.read_text()

lines_in_content = file_contents.splitlines()

for line in lines_in_content:
    print(line)


#Topic => Working with a file content

from pathlib import Path
path = Path("samplefile2.txt")

content = path.read_text()

lines = content.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.lstrip() #lstrip used for removing left side whitespace
print(pi_string)
print(len(pi_string))


#Note => python reads from a text file it interprets all text in the file as string
#=> if we want to deal with numerical value than we have to convert it to an integer value using int() function
# or float using float() function

