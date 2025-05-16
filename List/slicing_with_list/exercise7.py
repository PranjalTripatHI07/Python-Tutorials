#DATE - 3/1/2025

guests = ["super-man", "iron-man", "bat-man", "thor", "hulk"]
print("First there items in the list :-")
print(guests[:3])

print("\n middle there items in the list :-")
print(guests[1:4])

print("\n last there items in the list :-")
print(guests[2:])


# 2 question 2 :- 

my_pizza = ["apple-pizza", "orange-pizza", "pepper-pizza", "volcano-pizza"]
print(f"\n My favorite pizza list :- {my_pizza}")

my_friend_pizza = my_pizza[:]

print(f"\n My friend favorite pizza list :- {my_friend_pizza}")

my_pizza.append("morita-pizza")
my_friend_pizza.append("cheese-pizza")

print(f"\n My favorite pizza list :- {my_pizza}")
print(f"\n My friend favorite pizza list:- {my_friend_pizza}")

print("\n My favorite pizza are :- ")
for pizza in my_pizza[0:]:
    print("\n", pizza)

print("\n My friend favorite pizza list :- ")
for pizza in my_friend_pizza[0:]:
    print("\n", pizza)
    
    
foods = ["pizza", "burger", "meggi", "cold-drink", "veg-rice-plate", "sabji-roti", "mango-shake", "lassi", "chole-rice-palte", "rajma-rice-plate"]

print("\n Food available for today menus :- ")
for food in foods[0:]:
    print("\n", food)

print("\n My food order is :- ")
my_order = foods[2:5]
for order in my_order[0:]:
    print("\n", order)