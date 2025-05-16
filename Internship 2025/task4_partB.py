'''
B. Ticket Price:
 Write a program that takes a person's age as input and prints the cost of a movie ticket based on the following criteria:
Age 0-5: Free
Age 6-12: $5
Age 13-17: $8
Age 18-59: $12
Age 60 and above: $6

'''
print("\n Welcome to movieBuzz")
person_age = int(input("\n Enter your age"))

if person_age <= 5:
    Entry = "Entry is free"
elif (person_age > 5) and (person_age <= 12):
    Entry = "Entry Fee is:- $5"
elif (person_age > 12 ) and (person_age <= 17):
    Entry = "Entry Fee is:- $8"
elif (person_age > 17) and (person_age <= 59):
    Entry = "Entry Fee is:- $12"
elif person_age > 59:
    Entry = "Entry Fee is:- $6"

print(f"\n {Entry}")