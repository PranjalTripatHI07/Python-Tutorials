print("Welcome to Grade Calculator")
score = int(input("\t\n Enter your score"))


if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'

print(f"\t\n Your score is:- {score}")
print(f"\t\n Your grade is:- {grade}")
