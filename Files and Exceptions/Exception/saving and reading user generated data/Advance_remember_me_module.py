#DATE - 16/3/2025
from pathlib import Path
import json

def get_stored_username(file_path):

    if file_path.exists():
        file_content = file_path.read_text()
        user_details = json.loads(file_content)
        return user_details
    else:
        return None

def greet_user():
    file_path = Path("user_details.json")

    user_details = get_stored_username(file_path)

    if user_details:
        print(f"\n Welcome Back, {user_details}")
    else:
        user_details = greet_new_user(file_path)
        print(f"\n We will remember your username: {user_details}")


def greet_new_user(file_path):
    user_details = input("\n Enter your username: ")
    file_content = json.dumps(user_details)
    file_path.write_text(file_content)
    return user_details


greet_user()

