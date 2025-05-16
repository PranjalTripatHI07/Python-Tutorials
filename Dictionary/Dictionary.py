#DATE - 11/1/2025

#Dictionary
#-> Dictionary in python is a collection of key:value pairs

#syntax->

#name_of_dictionary = {'key':'value', 'key':'value', 'key':'value', 'key':'value'}
#print(name_of_dictionary['key'])
#print(name_of_dictionary['key'])
#print(name_of_dictionary)


#example

alien = {'color':'blue', 'points':10}
print(alien['color'])
print(alien['points'])
print(alien)

#Accessing value in Dictionary

alien = {'color':'blue', 'points':10}
print(alien['points'])
#or
points_earned = alien['points']
print(f"you have earned {points_earned} points")

#note for accessing dictionary value we use => name_of_dictionary['key'] => we use this syntax for accessing dictionary
#value

#Adding new key:value pair in Dictionary

alien = {'color':'blue', 'points':10,}

print(alien['color'])
print(alien['points'])

#now adding new key value pairs

alien['x-axis'] = 5
alien['y-axis'] = 10

print(alien)

#Starting with empty dictionary

alien = {} #=> empty dictionary
alien['color'] = 'blue'
alien['points'] = 10
alien['x-position'] = 0
alien['y-position'] = 5
alien['z-position'] = 2

print(alien)

#modifying values in Dictionary

alien = {'color':'blue', 'points':10}

alien['color'] = 'yellow' #modifyining value of dictionary

print(alien)


#another example
#In this example we track the position of alien that can move at different speed

alien = {'x-position':0, 'y-position':25, 'speed':'medium'}
print(f"\n Alien current position is {alien['x-position']}")

#alien['speed'] = 'fast'

if alien['speed'] == 'slow':
    x_increment = 1
elif  alien['speed'] == 'medium':
    x_increment = 2
elif alien['speed'] == 'fast':
    x_increment = 4

alien['speed'] = 'fast'

alien['x-position'] = alien['x-position'] + x_increment

print(f"\n Alien New position is {alien['x-position']}")

#removing key:value pairs from dictionary

#For this We use => del function
#syntax =>  del name_of_dictionary['key']

#example

alien = {'color':'blue', 'points':10}
print(alien)

del alien['points']
print(alien)

#see now key:value pair is deleted or removed from the dictionary
#note => the deleted key:value pair is removed permanently


#Dictionary of similar object

fav_programming_lang = {
    'thor':'c++',
    'iron-man':'c#',
    'supper-man':'go',
    'hulk':'python',
    'bat-man':'python',
}

fav_lang = fav_programming_lang['bat-man'].title()
print(f"\n Favorite programming lang of bat-man is: {fav_lang}")


#using get() method to access the value in dictionary

alien = {'color':'blue', 'speed':'medium'}

missing_value = alien.get('points', 'No value found')

print(f"\n  missing key:value pair : - {missing_value}") #use1 of get method in dictionary

print(f"\n Using get method to access the value and here value of color is:- {alien.get('color')}") #use2 of get method in dictionary
