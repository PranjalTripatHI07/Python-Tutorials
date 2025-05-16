print("\t\n Welcome to vowel or consonant checker")
char = input("Enter a single character: ").lower()

if len(char) == 1 and char.isalpha():

    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")