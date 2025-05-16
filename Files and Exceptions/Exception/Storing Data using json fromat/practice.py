from pathlib import Path
import json

file_location = Path("practice.json")

dictionary_data = {"user":"willie van", "username":"@willie001", "userid":1, "email":"demo@email.com"}

json_data = json.dumps(dictionary_data)

print(file_location.write_text(json_data.title()))

file_content = file_location.read_text()

json_load_data = json.loads(file_content)
print(json_load_data)
