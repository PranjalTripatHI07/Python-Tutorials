from pathlib import Path

path = Path("PI_VALUE.txt")

Content = path.read_text()

lines = Content.splitlines()
print(lines)
pi_string = ""

for line in lines:
    pi_string += line. strip()
print(pi_string)


birthday = input(f"\n Enter your birthday in dd-mm-y")

if birthday in pi_string:
    print("Your birthday appears in the first millions digits of pi")
else:
    print("Your birthday does not appear in first million digits of pi")
