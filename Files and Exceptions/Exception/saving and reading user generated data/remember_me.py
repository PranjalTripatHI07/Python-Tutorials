#DATE - 16/3/2025

from pathlib import Path
import json

file_path = Path("user_data.json")
if file_path.exists():             #here we use exists() method which one of the method of pathlib
                                   #In exists() method if file exist it return true and if file does note exists if return false
    file_content = file_path.read_text()
    user_data = json.loads(file_content)
    print(f"\n Welcome back, {user_data}")
else:
    user_data = input("\n Enter your username ")

    file_content = json.dumps(user_data)

    file_path.write_text(file_content)

    print(f"\n We will remember you when you come back, {user_data}")

