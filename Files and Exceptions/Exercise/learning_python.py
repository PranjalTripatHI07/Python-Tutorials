from pathlib import Path

file_location = Path("learning_python.txt")

contents = file_location.read_text()
print(contents)

lines = contents.splitlines()

for line in lines:
    print(line.replace("python","c++"))


#Another way

from pathlib import Path

file_address = Path("learning_python.txt")

file_content = file_address.read_text()
print(file_content)


for line in file_content.splitlines():
    print(line.replace("python", "c++"))