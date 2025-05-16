#DATE - 12/3/2025

#Silent Cats and Doges

from pathlib import Path

def read_file_content(filenames):
    try:
        file_content = filenames.read_text()
        print(f"\n File content:\n {file_content}")

    except FileNotFoundError:
        pass

filenames = ["dog.txt", "cat.txt"]
for filename in filenames:
    file_path = Path(filename)
    read_file_content(file_path)