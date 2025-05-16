#DATE - 18/2/2025

#Number served

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def get_details(self):
        restaurant_info = f"\n Restaurant name = {self.restaurant_name} | Cuisine type = {self.cuisine_type} | Number of customer served = {self.number_served}"

        return restaurant_info.title()

    def set_number_served(self, number_served):
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("\n number_served cannot be less than 0")

    def increment_number_served(self, number_served):
        self.number_served += number_served





restaturent_1 = Restaurant("Sukiyabashi Jiro", "Japanese Cuisine")

print(restaturent_1.get_details())

restaturent_1.set_number_served(250000)

print(restaturent_1.get_details())

restaturent_1.increment_number_served(100)

print(restaturent_1.get_details())

restaturent_1.increment_number_served(600)

print(restaturent_1.get_details())


# Users

class Users:
    def __init__(self, first_name, lastname, userid):
        self.first_name = first_name
        self.last_name = lastname
        self.userid = userid
        self.login_attempts = 0

    def user_details(self):
        user_info = f"\n First Name = {self.first_name} | Last Name = {self.last_name} | UserID = {self.userid} | Login Attempts = {self.login_attempts}"
        return user_info.title()


    def increment_login(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = Users("willie", "van", "willi01")

print(user_1.user_details())

user_1.increment_login()

print(user_1.user_details())

user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()
user_1.increment_login()

print(user_1.user_details())

user_1.reset_login_attempts()

print(user_1.user_details())