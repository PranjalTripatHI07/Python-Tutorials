#DATE - 16/3/2025
from pathlib import Path
import json
def greet_user():
    file_path = Path("user_details.json")
    if file_path.exists():
        file_content =  file_path.read_text()
        user_details = json.loads(file_content)
        print(f"\n Welcome back, {user_details} ")
    else:
        user_details = input("\n Enter username ")
        file_content = json.dumps(user_details)
        file_path.write_text(file_content)
        print(f"\n We will remember you {user_details} ")


greet_user()

