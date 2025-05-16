class Car:
    def __init__(self, make,model,year):
        self.make  = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer = {self.make} | Model = {self.model} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"
        return car_info

    def fill_tank(self):
        return f"\n This Car {self.model} model have gas tank"


class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        return f"\n This car has a {self.battery_size}kWh battery"

class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() #Imp Note => here we create an object attribute for class Electric car and assign a class Battery to self.battery attribute
        #Imp Note => self.battery = Battery() creates a composition relationship between Electric_car and Battery classes
    def fill_tank(self):
        return  f"\n This Car {self.model} model have no need of gas tank"


electric_car_1 = Electric_car("Audi", "AU4545", 2020)
print(electric_car_1.get_details())
print(electric_car_1.battery.describe_battery()) #Imp Note=> Call battery methods via =>  electric_car_1.battery.describe_battery()