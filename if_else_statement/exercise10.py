alien_color = "green"

if alien_color == "green":
    print("you have earned 5 points")

if alien_color == "red":
    print("you have earned no points")

#if-else use

alien_color = "red"
if alien_color == "green":
    print("you have earned 5 points")
else:
    print("you have earned no points")

#if-elif-else use

alien_color = "yellow"
if alien_color == "green":
    print("you have earned 5 points")
elif alien_color == "yellow":
    print("you have earned 10 points")
else:
    print("you have earned 15 points")



# stages of life

age = 20
if age < 2:
    stage = "baby"
elif (age == 2) and (age < 4):
    stage = "toddler"
elif (age == 4) and (age < 13):
    stage = "kid"
elif (age == 13) and (age < 20):
    stage = "teenager"
elif (age == 20) and (age < 65):
    stage = "adult"
elif (age == 65) and (age > 65):
    stage = "old"

print(f"\n person is {stage}")
