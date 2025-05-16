#DATE - 3/1/2025

#Copying a list through slicing :- 

my_fav_food = ["dall rice", "masala dosa", "pizza", "aappe", "idali shabhar"]
print("my favorite food is :-") 
print(my_fav_food)

my_friendfav_food = my_fav_food[:]

print("\nmy friend favorite food is :-")
print(my_friendfav_food)

# now adding new food to both lists :-

my_fav_food.append("ice-cream")

my_friendfav_food.append("Chocolate-cream")

print(f"\n my  favorite food is :- {my_fav_food}")
print(f"\n my friend favorite food is :- {my_friendfav_food}")

#Note - when ever you want to copy a list use slice method to copy list 
