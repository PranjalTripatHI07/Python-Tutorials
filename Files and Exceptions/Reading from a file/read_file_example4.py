from pathlib import Path

file_location = Path("samplefile2.txt")
print(file_location.read_text().rstrip())