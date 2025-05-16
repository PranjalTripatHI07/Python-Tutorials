from pathlib import Path

path = Path("sample_text_5.txt")

content = path.read_text()


lines = content.splitlines()

for line in lines:
    print(line)

