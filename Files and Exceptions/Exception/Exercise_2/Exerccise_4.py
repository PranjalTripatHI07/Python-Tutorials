#DATE - 20/3/2025

#User Dictionary
from pathlib import Path
import json

def user_data():
    file_path = Path("user_full_details.json")

    first_name = input("\n Enter first name: ")
    last_name = input("\n Enter last name: ")
    email = input("\n Enter email: ")
    username = input("\n Enter username: ")
    password = input("\n Enter password: ")

    file_contents = json.dumps({first_name: first_name, last_name: last_name, email: email, username: username, password: password})
    file_path.write_text(file_contents)
    print(f"\n User details saved in: {file_path}")

def load_user_details():
    file_path = Path("user_full_details.json")
    file_contents = file_path.read_text(encoding="utf-8")
    userdata_details = json.loads(file_contents)
    print(f"\n Bellow is user details: \n -{userdata_details}")


user_data()
load_user_details()


#Another way
from pathlib import Path
import json

def user_data():
    file_path = Path("user_full_details.json")

    data = {
        "first_name": input("\n Enter first name: "),
        "last_name": input("\n Enter last name: "),
        "email": input("\n Enter email: "),
        "username": input("\n Enter username: "),
        "password": input("\n Enter password: "),
    }
    file_contents = json.dumps(data)
    file_path.write_text(file_contents, encoding="utf-8")
    print(f"\n User details saved in: {file_path}")

def load_user_details():
    file_path = Path("user_full_details.json")
    file_contents = file_path.read_text(encoding="utf-8")
    userdata_details = json.loads(file_contents)
    print(f"\n Bellow is user details: \n -{userdata_details}")

