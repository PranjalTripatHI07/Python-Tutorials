#DATE - 12/3/2025

#Cats and Doges

from pathlib import Path

def read_file_content(filenames):
    try:
        file_content = filenames.read_text()
        print(f"\n File content: {file_content}")
    except FileNotFoundError:
        print("\n Sorry file not found")


filenames = ["dog.txt", "cat.txt"]
for filename in filenames:
    file_path = Path(filename)
    read_file_content(file_path)
