#DATE - 20/3/2025

#Favorite Number Remembered


from pathlib import Path
import json

def remembered_fav_number():
    file_path = Path("remembered_fav_number.json")
    if file_path.exists():
        file_content = file_path.read_text(encoding="utf-8")
        fav_number = json.loads(file_content)
        print(f"\n I know the favorite number is: {fav_number}")
    else:
        fav_number = input("\n Enter favorite number: ")
        file_content = json.dumps(fav_number)
        file_path.write_text(file_content)
        print("\n Favorite number is stored.")

remembered_fav_number()