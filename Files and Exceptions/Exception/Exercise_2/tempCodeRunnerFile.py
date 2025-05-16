from pathlib import Path
import json

file_path = Path("favorite_number.json")

def store_fav_number():
    fav_number = input("\n Enter the favorite number: ")
    file_contents = json.dumps(fav_number)
    file_path.write_text(file_contents)
    print(f"\n The favorite number is: {fav_number}")



def load_fav_number():
    file_contents = file_path.read_text(encoding="utf-8")
    fav_number = json.loads(file_contents)
    print(f"\n I know the favorite number is: {fav_number}")


store_fav_number()

load_fav_number()