from pathlib import Path

file_path = Path("handling_file_not_found_exception.txt")

try:
    content = file_path.read_text()
except FileNotFoundError:
    print(f"\n Sorry file path -{file_path} not found")