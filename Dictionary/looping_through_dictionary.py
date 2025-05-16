#DATE - 12/1/2025
from Dictionary.Dictionary import fav_programming_lang

#TOPIC -  Looping through dictionary
# There are different ways or methods  of looping in dictionary

#1. method1 => looping through all key:value pairs
#syntax => for key,value in name_of_dictionary.items():
#                    do something

#note => .items() is a method used for returning series of key:value pairs in dictionary
#note => we can give any name to key,value like we simply write => for k,v in name_of_dictionary.item():

#Example

users = {
    'username':'ironman@11',
    'first_name':'iron-man',
    'age':150,
    'city':'new-york',
    'country':'usa'
}

for user, value in users.items():
    print(f"\n key:- {user} \n value:- {value}")



#example 2

fav_language = {
    'iron-man':'python',
    'thor':'python',
    'hulk':'c/c++',
    'super-man':'java',
    'bat-man':'python',
    'drStrange':'python'
}

for user, programming_lang in fav_language.items():
    print(f"\n {user} favorite programming language is :- {programming_lang}")


#method2 => looping through all keys in dictionary

#syntax => for key in name_of_dictionary.keys():
#                   do something

#note => .keys() is a method used for returning all the keys in dictionary
#note => we can give any name to key like we simply write => for k in name_of_dictionary.keys():

#example

fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic'
}

for name in fav_sub.keys():
    print(f"\n Hi {name}")


#example 2

fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic'
}

myFriend = ['iron-man', 'thor']

for name in fav_sub.keys():
    if name in myFriend:
        print(f"\n Hi {name.title()} how are you")
    else:
        print(f"\n Hi {name.title()}")

#example 3
#this code print name and subject they like
fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic'
}
myFriend = ['iron-man', 'thor']
for name in fav_sub.keys():
    if name in myFriend:
        subject = fav_sub[name].title()
        print(f"\n Hi {name} your fav subject is {subject}")
    else:
        print(f"\n Hi {name.title()} how are you")


#method 3 => Looping through a dictionary key in a particular order

#syntax => For this we use sorted() function to loop through a dictionary in a particular order
#note => we can give any name to key like we simply write => for k in name_of_dictionary.keys():
#syntax=> for key in sorted(name_of_dictionary.keys()):
#               do something

#exmaple
#This will print output in alphabetical order because we use sorted() function to sort the output in an alphabetical order
fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic'
}

for name in sorted(fav_sub.keys()):
    print(f"\n Hi {name.title()}")

#method 4 => Looping through all values in a dictionary

#syntax => for value in name_of_dictionary.values():
#                    do something

#note =>  .values() method is used for returning all the values in dictionary
#note => we can give any name to value like we simply write => for v in name_of_dictionary.values():

#note=> To avoid repetition of values we use Set() function
#=> set() function is used to avoid the repetition of values
#=> Or set() function is collection of values in which each value must be unique
#syntax => syntax for using set() function => for value in set(name_of_dictionary.values()):

#Example

fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic'
}

for sub in fav_sub.values():
    print(f"\n Hi Your fav subject is {sub}")


#Example =>  avoiding repetition of values

fav_sub = {
    'iron-man':'ai/ml',
    'thor':'geography',
    'hulk':'biology',
    'super-man':'computer-science',
    'bat-man':'ml',
    'drStrange':'magic',
    'spider-man':'ai/ml'
}

for sub in set(fav_sub.values()):
    print(f"\n Hi Your fav subject is :- {sub}")