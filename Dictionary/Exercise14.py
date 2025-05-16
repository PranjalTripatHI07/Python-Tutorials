user_details = {
    'first_name':'iron-man',
    'last_name':'Avenger',
    'age':150,
    'city':'new-york'
}

print(f"\n First-name :- {user_details['first_name']}")
print(f"\n Last-name :- {user_details['last_name']}")
print(f"\n Age of {user_details['first_name']} is :- {user_details['age']}")
print(f"\n City {user_details['first_name']} belongs to is :- {user_details['city']}")

#another way of doing it

print(f"\n First name is :- {user_details.get('first_name')}")
print(f"\n Last name is :- {user_details.get('last_name')}")
print(f"\n key:value pair which is note in dictionary :-  {user_details.get('country', 'value is not present')}")


# fav_number question ans:-

fav_num = {
    'iron-man':'1',
    'thor':'5',
    'hulk':'2',
    'super-man':'4',
    'bat-man':'6'
}

print(f"\n Favorite Number poll \n {fav_num}")

print(f"\n iron-man fav num is :- {fav_num.get('iron-man')}")
print(f"\n thor fav num is :- {fav_num.get('thor')}")
print(f"\n hulk fav num is :- {fav_num.get('hulk')}")
print(f"\n super-man fav num is :- {fav_num.get('super-man')}")
print(f"\n bat-man fav num is :- {fav_num.get('bat-man')}")


#glossary ans

glossary = {
    '.sort()':'.sort() is method in python used for shorting list item in list in alphabetical order',
    'sorted()':'sorted() is a function in python used for sorting list in alphabetical order',
    'range()':'range() is a function in python used for generating range of number in python',
    'sum()':'sum() is a function in python used for findig sum of values in list'
}

print(f"\n .sort() :- {glossary['.sort()']}")
print(f"\n sorted() :- {glossary['sorted()']}")
print(f"\n range():- {glossary['range()']}")
print(f"\n sum():- {glossary['sum()']}")