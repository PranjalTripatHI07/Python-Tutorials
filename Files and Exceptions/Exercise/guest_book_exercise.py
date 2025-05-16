#DATE - 6/3/2025

#Guest Book

from pathlib import Path

file_location = Path("guest_book_exercise.txt")

guest_names = []

while True:
    guest_name = input("Enter Guest name (and to end guest list type finish) ")
    if guest_name.lower() == "finish":
        break
    guest_names.append(guest_name)

content = ""

for guest_name in guest_names:
    content += f"\n -{guest_name.title()}"

print(file_location.write_text(content))

print(f"Guest names have been written to {file_location}")
