# Now we write a program that greet user whose name has already been stored

from pathlib import Path
import json

file_path = Path("username.json")
file_content = file_path.read_text(encoding="utf-8")
username = json.loads(file_content)

print(f"\n Welcome back {username.title()} ")