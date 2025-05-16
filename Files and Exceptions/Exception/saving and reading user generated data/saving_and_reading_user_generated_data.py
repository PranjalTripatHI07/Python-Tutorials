#DATE - 16/3/2025

#Topic - Saving and Reading User generated Data

#We can save and read data in json formatted string

#syntax and example

from pathlib import Path
import json

file_path = Path("username.json")

username = input("\n Enter Username: ")

file_content = json.dumps(username.title())  #json.dumps() function convert python data into json formated string

file_path.write_text(file_content)

print(f"\n We will remember you when you come back, {username.title()}")


# Now we write a program that greet user whose name has already been stored

from pathlib import Path
import json

file_path = Path("username.json")
file_content = file_path.read_text(encoding="utf-8")
username = json.loads(file_content)

print(f"\n Welcome back {username.title()} ")