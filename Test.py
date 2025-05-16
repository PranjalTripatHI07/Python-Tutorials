cars = []

#methods used for adding elements to the table
#1. append() - adds the element at the end of the list
#2. insert() - adds the element at any index position
cars.append("Honda")
cars.append("Toyota")
cars.append("Tata")
cars.append("Ford")
cars.append("Maruti Suzuki")
cars.append("Hyundai")
cars.append("Kia")
cars.append("Nissan")
cars.append("Chevrolet")
cars.append("Volkswagen")
cars.append("Renault")
cars.append("Audi")
cars.append("BMW")
cars.append("Mercedes")
cars.append("Ferrari")
cars.append("Lamborghini")
cars.insert(-2, "Bugatti")
cars.insert(1, "Mercedes")

#method used for removing elements from the list
#1. del - used for removing  elements at any index position
#2. pop() - removes the last element from the list
#3. remove() - removes the element by its value

del cars[1]
del cars[-1]

cars.pop()
cars.pop()
cars.pop(0) # we can pop or remove any element from the using index value 
# In pop method we remove the elements from the list but after removing the element we still use that element
# so that is why use pop method basically pop method is used to remove those elements from the list
# which we want to use in future

pop_car = cars.pop()
print(f"{pop_car} is very expensive car")

cars.remove("Mercedes")
cars.remove("Renault")

remove_car = cars.remove("Mercedes")
print(f"{remove_car} is very popular car")

print(cars)