#Date - 27/12/2024
#This code print the names of person from a list of people

SuperHeroes = ["iron-man", "Thor", "Hulk", "Captain America", "Black Widow", "Hawkeye", "Spider-man", "Black Panther", "Doctor Strange", "Ant-man", "Wasp"]

print(SuperHeroes[0].title())
print(SuperHeroes[4].title())
print(SuperHeroes[1].title())
print(SuperHeroes[5].title())
print(SuperHeroes[-1].title()) 
print(SuperHeroes[-2].title())
print(SuperHeroes[-4].title())
print(SuperHeroes[-5].title())

print(f"Most powerful super hero is {SuperHeroes[1].title()}")

message = f"Most week superhero is {SuperHeroes[-1].title()}"
print(message)
