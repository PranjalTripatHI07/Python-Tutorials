#DATE - 20/3/2025

#Verify User

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

def verify_username():
    file_path = Path("user_full_details.json")
    if file_path.exists():
        file_contents = file_path.read_text(encoding="utf-8")
        user_verification = json.loads(file_contents)
        userinput = input(f"\n Above user details are correct: Y/N ")
        if userinput.lower() == "y":
            print("\n User details verified")
        else:
            print("\n User details not verified")
    else:
        print("\n User details not found")


user_data()
load_user_details()
verify_username()