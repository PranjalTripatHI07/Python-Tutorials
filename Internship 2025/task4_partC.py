'''
Write a program that takes a month (1-12) and day (1-31) as input and prints the season
(Spring, Summer, Fall, or Winter) based on the date.
'''

print("\n Welcome to Season Identifier:- ")

month = int(input("\n Enter the month (1-12): "))

day = int(input("\n Enter the day (1-31): "))

if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
    season = "Winter"
elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
    season = "Spring"
elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
    season = "Summer"
elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day < 21):
    season = "Fall"
else:
    season = "Invalid date"

print(f"\n The season is: {season}")