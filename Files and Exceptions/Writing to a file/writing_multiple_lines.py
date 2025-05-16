from pathlib import Path

file_path = Path("writing_multiple_line.txt")

content = " Welcome To Esy Notebook"
content += "\n Hello User!"
content += "\n Here You can write anything"
content += "\n Enjoy and keep blogging your day"

print(file_path.write_text(content))

#Another Easy Way

from pathlib import Path

file_path = Path("writing_multiple_lines_easy_way.txt")

print(file_path.write_text(" Wellcome To Esy World \n Here we do things done very easily \n So do anything you want \n Hope you enjoy !"))