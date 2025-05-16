from pathlib import Path

file_path = Path("guest_book_exercise.txt")

guest_list = []

while True:
    guest_name = input("\n Enter guest name and to finish write finish ")
    if guest_name == "finish":
        break
    guest_list.append(guest_name)

file_content = ""
for guest_name in guest_list:
    file_content += f"\n -{guest_name.title()}"

file_path.write_text(file_content)

print("\n Guest name have been written to guest_book_exercise.txt")

