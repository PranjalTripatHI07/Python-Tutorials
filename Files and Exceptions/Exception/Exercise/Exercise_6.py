#DATE - 12/3/2025

#Common word

from pathlib import Path

def count_words(filenames, word):
    try:
        file_content = filenames.read_text(encoding="utf-8")
        print(f"\n --------------File Content-----------------")
        print(file_content)
    except FileNotFoundError:
        print("\n Sorry file not found")
    else:
        file_content_length = file_content.lower().count(f" {word} ")
        print(f"\n File Name - {filenames}")
        print(f"\n Word - {word}")
        print(f"\n Word Repeat - {file_content_length}")

filenames = ["book.txt"]
word = input("\n Enter a word you want to check is repeating: ")
for filename in filenames:
    file_path = Path(filename)
    count_words(file_path, word)


#Another Solution
'''
from pathlib import Path
import re  # Import regular expressions

def count_words(filename, word):
    """Reads, prints, and counts occurrences of a word in a text file."""
    try:
        file_content = filename.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nSorry, the file '{filename}' was not found.")
        return

    # Print file content (limit to 1000 characters for preview)
    print(f"\n--- File Content: {filename} ---\n")
    print(file_content[:1000])  # Adjust this limit if needed
    print("\n--- End of Preview ---\n")

    # Convert to lowercase for case-insensitive search
    file_content_lower = file_content.lower()

    # Counting occurrences using regex for accurate word matching
    general_count = file_content_lower.count(word)  # Counts any appearance
    precise_count = len(re.findall(rf"\b{word}\b", file_content_lower))  # Accurate word count

    print(f"File Name: {filename}")
    print(f"Word: {word}")
    print(f"General Word Count: {general_count}")
    print(f"Precise Word Count (excluding substrings): {precise_count}")

# File list
filenames = ["book.txt"]
word = input("\nEnter a word you want to count: ").strip().lower()

# Process each file
for filename in filenames:
    file_path = Path(filename)
    count_words(file_path, word)
'''

