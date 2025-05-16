#DATE- 11/3/2025

#Topic => Working with multiple file

from pathlib import Path

def count_words(file_names):
    """Counts the number of words in a file."""
    try:
        file_content = file_names.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("\n File not found")
    else:
        file_content.split()
        file_content_length = len(file_content)
        print(f"\n The file {file_names} has about {file_content_length} words")

    # Now for multiple files
file_names = ["alicewonderland.txt", "camping.txt", "money_mind.txt", "today.txt"]
for file_name in file_names:
    file_path = Path(file_name)
    count_words(file_path)

