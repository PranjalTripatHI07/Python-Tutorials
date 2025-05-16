glossary = {
    '.sort()':'.sort() is method in python used for shorting list item in list in alphabetical order',
    'sorted()':'sorted() is a function in python used for sorting list in alphabetical order',
    'range()':'range() is a function in python used for generating range of number in python',
    'sum()':'sum() is a function in python used for findig sum of values in list',
    '.items()':'.items() is a method used for returning series of key:value pairs in dictionary',
    '.keys()':'.keys() is a method used for returning all the keys in dictionary',
    '.values()':'.values() is a method used for returning all the values in dictionary',
    'set()':'set() function is a collection of values in which each value must be unique',
    'set()':'set() function is used to avoid repetition of values we use set() function'

}

for python_built_in_keyword, working in glossary.items():
    print(f"{python_built_in_keyword} :- {working}")


country_river = {
    'USA':'Mississippi River',
    'russia':'Volga River',
    'uk':'Thames River',
    'Netherland':'Rhine River',
    'south-koria':'Han River'
}

for country,river in country_river.items():
    print(f"\n {river} runs in {country}")

print("\n name of rivers present in dictionary")

for river in country_river.values():
    print(f"\n {river}")

print("\n name of country present in dictionary ")

for country in country_river.keys():
    print(f"\n {country}")

# fav lang exercise

lang =  {
    'peter-parker':'python',
    'bruce-vane':'ai/ml',
    'steafen-strange':'java',
    'tony-stark':'ai/ml',
    'steve-roger':'java'
}

participants = ["bruce-banner", "peter-parker", "bruce-vane", "tony-stark"]

for key in participants:
    if key in lang.keys():
        print(f"\n Thankyou {key} for participating")
    elif key not in lang.keys():
        print(f"\n Hello {key} please fill the poll")



users = {
    'joy':'Reference no 1',
    'iron-man':'Reference no 2',
    'Hulk':'Reference no 4',
    'toy-stark':'Reference no 5',
    'bruce-van':'Reference no 6'
}

accounts = ['joy', 'bruce-van', 'steve-roger','peter-parker', 'iron-man', 'steafan-strange']

for account in accounts:
    if account in users.keys():
        print(f"\n  Hello {account} ")
    elif account not in users.keys():
        print(f"\n Sorry {account} first you have to create account")