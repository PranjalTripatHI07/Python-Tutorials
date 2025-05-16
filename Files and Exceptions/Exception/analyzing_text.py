from pathlib import Path

file_location = Path("demo_file.txt")

try:
    file_content = file_location.read_text()
except FileNotFoundError:
    print("\n File not found")

else:
    file_content.split()
    file_content_length = len(file_content)
    print(f"\n The file {file_location} has about {file_content_length} words")