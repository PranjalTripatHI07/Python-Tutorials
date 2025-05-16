#DATE - 21/2/2025
from Classes.classes import electric_car1
from Dictionary.nesting import user_info


#Ice Cream stand

class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.flavours =  ["Mango,", "valina", "strawberry", "chocolate"]


    def restaurant_details(self):
        restaurant_info = f"\n Restaurant Name = {self.restaurant_name} | Restaurant Type = {self.restaurant_type}"
        return restaurant_info.title()

    def flavour_list(self):
        print("\n List of flavour available :-")
        for flavour in self.flavours:
            print(f" -{flavour}")


class Ice_Cream_stand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type):
        super().__init__(restaurant_name,restaurant_type)


ice1 = Ice_Cream_stand("IceWala", "Ice-cream Stand")

print(ice1.restaurant_details())
ice1.flavour_list()


# Another Solution
class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def restaurant_details(self):
        restaurant_info = f"\n Restaurant Name = {self.restaurant_name} | Restaurant Type = {self.restaurant_type}"
        return restaurant_info.title()



class Ice_Cream_stand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type = Ice_Cream_stand):
        super().__init__(restaurant_name,restaurant_type)

        self.flavour_list = []


    def add_flavour(self, flavour):
        self.flavour_list.append(flavour)


    def show_flavour(self):
        print("\n List of flavour")
        for flavour in self.flavour_list:
            print(f"-{flavour}")


ice1 = Ice_Cream_stand("IceWala", "Ice-cream Stand")

print(ice1.restaurant_details())

ice1.add_flavour("mango")
ice1.add_flavour("strawberry")
ice1.add_flavour("valina")
ice1.add_flavour("American Nuts")
ice1.add_flavour("chocolate")


ice1.show_flavour()




#Admin

class Users:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.privileges = ["can add post", "can delete post", "can ban users", "can update users info"]


    def show_privileges(self):
        print("\n list Admin Privileges:-")
        for privileges in self.privileges:
            print(f"-{privileges}")



class Admin(Users):
    def __init__(self, first, last):
        super().__init__(first, last)



admin1 = Admin("Willie", "van")

admin1.show_privileges()


# Another solution

class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_details(self):
        user_info = f"\n First Name = {self.first_name} | Last Name = {self.last_name}"
        return user_info.title()

    def greet_user(self):
        return f"\n Hello {self.first_name} {self.last_name}! Welcome to codebuddy"


class Admin(Users):
    def __init__(self, first_name, last_name, *privileges): #Note Here we initialize child class parameter and parent class parameter
        super().__init__(first_name, last_name)  #Note Here we call or use parent class attributes(parameters) so that we can use parent class methods(functions)

        self.privileges = privileges

    def show_privileges(self):
        print("\n List of privileges:- ")
        for privilege in self.privileges:
            print(f"-{privilege}")


admin1 = Admin("Willie", "van", "can ban users", "can delete users", "can add user", "can update user info")

admin1.show_privileges()
print(admin1.user_details())
print(admin1.greet_user())
admin1.show_privileges()




#Privileges

class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_details(self):
        user_info = f"\n First Name = {self.first_name} | Last Name = {self.last_name}"
        return user_info.title()

    def greet_user(self):
        return f"\n Hello {self.first_name} {self.last_name}! Welcome to codebuddy"


class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("\n List of privileges:-")
        for privileges in self.privileges:
            print(f"-{privileges}")


class Admin(Users):
    def __init__(self, first_name, last_name, *privileges): #Note Here we initialize child class parameter and parent class parameter
        super().__init__(first_name, last_name) #Note Here we call or use parent class attributes(parameters) so that we can use parent class methods(functions)

        self.privileges = Privileges(*privileges)



admin1 = Admin("Willie", "van","can ban users", "can delete users", "can add user", "can update user info")


print(admin1.user_details())
print(admin1.greet_user())
admin1.privileges.show_privileges()



# Electric car

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_details(self):
        car_info = f"\n Make = {self.make} | Model = {self.model} | Year = {self.year}"
        return car_info.title()


class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def battery_details(self):
        return f"\n This car has a {self.battery_size}kwh battery"

    def get_battery_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 200

        print(f"\n This car can go about {range} miles on a full charge")


    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        self.get_battery_range()






class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()



electric_car1 = Electric_car("Audi", "AU", 2020)

electric_car1.battery.upgrade_battery()