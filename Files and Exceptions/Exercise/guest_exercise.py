#DATE - 6/3/2025

#Guest

from pathlib import Path

file_location = Path("guest_exercise.txt")

guest = input("Enter your name")

print(file_location.write_text(f"Hello {guest} how are you"))