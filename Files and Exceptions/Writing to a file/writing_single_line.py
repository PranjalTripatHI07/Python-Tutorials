#DATE - 3/3/2025

#Topic => Writing to a file

# Topic -> 1. Writing a single line

#Note => When the path is defined after that we can write to a file using the write_text()method

#syntax =>
from pathlib import Path
file_location = Path("writing_single_line.txt")
print(file_location.write_text("Welcome to Esy Notebook"))




#Another example
from pathlib import Path
file_path = Path("writing_single_line.txt")
storing_numerical_value = str(458740)
print(file_path.write_text(f"Welcome to Esy Notebook {storing_numerical_value} is your coupon"))
