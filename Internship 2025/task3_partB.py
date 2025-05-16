current_hour = int(input("\t\n Enter the current hour"))

if 0 <= current_hour < 12:
    greeting = "\t\n Good Morning"
elif 12 <= current_hour < 18:
    greeting = "\t\n Good Afternoon"
elif 18 <= current_hour < 24:
    greeting = "\t\n Good Evening"
else:
    greeting = "\t\n Invalid hour"

print(greeting)