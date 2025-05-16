from Classes.classes import car_1


class Users:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.userid = 1

    def user_details(self):
        user_info = f"\n First Name = {self.first_name} | Last Name = {self.last_name} | Username = {self.username} | Userid = {self.userid}"
        return user_info.title()


    def update_userid(self, userid):
        self.userid = userid




user_1 = Users("willie", "van", "willivan")

print(user_1.user_details())

user_1.update_userid(2)
print(user_1.user_details())



# Inheritance

# Example

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model} | year = {self.year} | Odometer Reading = {self.odometer_reading}"
        return car_info.title()

    def update_odometer(self, odometer_reading):
        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading

        else:
             print("\n Odometer reading cannot roll back")


    def increment_odometer(self, miles):
        self.odometer_reading += miles



class Electric_car(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)




car_1 = Electric_car("Nishan", "NIHAN44", 2020)


print(car_1.get_details())

car_1.update_odometer(250000)

print(car_1.get_details())

car_1.increment_odometer(1000)

print(car_1.get_details())



# another example


