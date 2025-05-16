# Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n -> Name of Restaurant is {self.restaurant_name.title()} and This Restaurant cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n -> {self.restaurant_name} is open Mon - Sun Timing 9am to 10pm")




restaurant_1 = Restaurant("Sukiyabashi Jiro", "Japanese Cuisine")
restaurant_2 = Restaurant("L'Opera", "French Cuisine:")


#accessing attributes
print(f"\n {restaurant_1.restaurant_name.title()} is a Japanese Restaurant")
print(f"\n {restaurant_2.restaurant_name.title()} is French Restaurant")

#calling methods(functions)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()





# Four Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n {self.restaurant_name.title()} is serving {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\n {self.restaurant_name.title()} is open Mon to Sun and The opening and closing time is 9am to 10pm")


restaurant1 = Restaurant("Sukiyabashi Jiro", "Japanese Cuisine")
restaurant2 = Restaurant("L'Opera", "French Cuisine")
restaurant3 = Restaurant("Sammy Sosa and Sancho's", "Mexican Cuisine")
restaurant4 = Restaurant("Casa de Sol", "Spanish Cuisine")


print(f"\n {restaurant1.restaurant_name.title()} is a Japanese Restaurant")
print(f"\n {restaurant2.restaurant_name.title()} is French Restaurant")
print(f"\n {restaurant3.restaurant_name.title()} is a Mexican Restaurant")
print(f"\n {restaurant4.restaurant_name.title()} is Spanish Restaurant")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()


restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()
restaurant4.open_restaurant()



# Users

class Users:
    def __init__(self, first_name, last_name, age, userid,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.userid = userid

    def describe_user(self):
        print(f"\n  Name = {self.first_name.title()} {self.last_name.title()} | age = {self.age} | userid = {self.userid}")


    def greet_user(self):
        print(f"\n    Hello {self.first_name.title()} {self.last_name.title()} Thank you for creating account! Your userid is {self.userid} welcome to codeworld")




user_1 = Users("Willie", "van", 20, 10020405)
user_2 = Users("bruce", "van", 45, 12100450)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()






