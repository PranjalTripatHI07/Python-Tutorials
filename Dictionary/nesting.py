# DATE - 16/1/2025
from Dictionary.Dictionary import alien

# Topic Nesting => Nesting is a process of placing a loop or conditional statement inside another loop
# or conditional statement


#1. A list of Dictionaries

# => Storing multiple dictionaries in a list => This method or concept helps in storing large data.
# like user data and product data


alien_1 = {
    'color':'blue',
    'points':10
}
alien_2 = {
    'color':'yellow',
    'points':5
}

alien_4 = {
    'color':'orange',
    'points':2
}

alien_5 = {
    'color':'white',
    'points':1
}

alien_6 = {
    'color':'red',
    'points':6
}

list_of_alien = [alien_1, alien_2, alien_4, alien_5, alien_6]

for alien in list_of_alien:
    print(alien)




brick_1 = {
    'color':'blue',
    'points':'10'
}

brick_2 = {
    'color':'yellow',
    'points':'5'
}

brick_3 = {
    'color':'orange',
    'points':'2'
}

brick_4 = {
    'color':'red',
    'points':'1'
}

bricks = [brick_1, brick_2, brick_3, brick_4]

for brick in bricks:
    print(f"\n {brick}")




# making of more than n no of dictionaries using list

#example

bricks = []

for brick in range(50):
    new_brick = {
        'color': 'blue',
        'points': '10'
    }
    bricks.append(new_brick)

for brick in bricks[:10]:
    print(f"\n {brick}")

#more practice

fruits = []

for fruit in range(100):
    fruit_basket = {
        'mango': 100,
        'apple': 80,
        'banana': 40,
        'guava': 60,
        'orange': 50
    }
    fruits.append(fruit_basket)

for fruit in fruits[:85]:
    print(f"\n {fruit}")
print("....")

print(f"\n total no of fruits {len(fruits)}")


# changing the property of object we use for loop and if statement

#example

bricks =[]

for brick in range(40):
    new_brick = {
        'color':'blue',
        'speed':'medium',
        'point':5
    }
    bricks.append(new_brick)

for brick in bricks[:5]:
    if brick['color'] == 'blue':
        brick['color'] = 'yellow'
        brick['speed'] = 'fast'
        brick['point'] = 10


for brick in bricks[:10]:
    print(f"\n {brick}")



#another example

bricks = []

for brick in range(40):
    new_brick = {
        'color': 'blue',
        'speed': 'medium',
        'point': 5
    }

    bricks.append(new_brick)

for brick in bricks[:5]:
    if brick['color'] == 'blue':
        brick['color'] = 'yellow'
        brick['speed'] = 'fast'
        brick['point'] = 10

    elif brick['color'] == 'yellow':
        brick['color'] = 'red'
        brick['speed'] = 'super fast'
        brick['point'] = 40

for brick in bricks[:10]:
    print(f"\n {brick}")




#2. list in a Dictionary  => using Means list inside dictionary
#syntax =>
# name_of_dictionary = {
#            'key':'value',
#            'key': ['value1', value2', 'value3', 'value4', 'value5']
#}

# for key in name_of_dictionary['keys']:
#        do something


#example

pizza = {
    'crust':'thick',
    'toppings': ['mushroom', 'cheese', 'peperoni', 'garlic']
}

print(f"\n your order {pizza['crust']}- crust - pizza and bellow is the list of toppings:-")

for topping in pizza['toppings']:
    print(f"\n choose any one {topping}")


#nesting example

polls  = {
    'iron-man':['python', 'ai/ml'],
    'bruce-van':['c', 'c++'],
    'hulk':['java'],
    'bat-man':['python', 'r'],
    'super-man':['python', 'ai/ml', 'r', 'html']
}

for name,subjects in polls.items():
    print(f"\n Hi {name} your fav subject is:-")
    for subject in subjects:
        print(f"\n {subject}")


# using if statement for applying condition for more than one subject

polls = {
    'iron-man':['python', 'ai/ml'],
    'bruce-van':['c', 'c++'],
    'hulk':['java'],
    'bat-man':['python', 'r'],
    'super-man':['python', 'ai/ml', 'r', 'html']
}

for name,subjects in polls.items():
    if len(subjects) > 1:
        print(f"\n Hi {name.title()} your fav subjects are:-")
    elif len(subjects) <= 1:
        print(f"\n Hi {name.title()} your fav subject is:-")

    for subject in subjects:
        print(f"\n {subject}")



#3 Dictionary in a Dictionary => means Dictionary inside Dictionary
# example

users = {
    'username1':{
        'first_name':'tony',
        'last_name':'stark',
        'location':'new-york'
    },
    'username2':{
        'first_name':'Bruce',
        'last_name':'van',
        'location':'new-york'
    }
}

for username,user_info in users.items():
    print(f"\n username :- {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"

    location =f"{user_info['location']}"

    print(f"\n Full name:- {full_name.title()}")
    print(f"\n location:- {location.title()}")
