#DATE - 16/3/2025

from pathlib import Path
import json

def get_stored_username(filepath):
    """Get stored username from filepath"""
    if filepath.exists():
        file_content = filepath.read_text()
        username = json.loads(file_content)
        return username
    else:
        return None

def greet_user():
    """Greet the user"""
    filepath = Path("username1.json")
    username = get_stored_username(filepath)
    if username:
        print(f"\n Welcome back, {username}")
    else:
        username = get_new_username(filepath)
        print(f"\n We will remember you when you come back, {username}")


def get_new_username(filepath):
    """Get new username from filepath"""
    username = input("Please enter your username: ")
    file_content = json.dumps(username)
    filepath.write_text(file_content)
    return username



greet_user()
