#This is a car class module that represent a car class and its functionality

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer Name = {self.manufacturer} | Model Name = {self.model} | Year of manufacturing = {self.year} | Initial Odometer Reading = {self.odometer_reading}"

        return car_info.title()

    def odometer_details(self):
        return f"\n This car has {self.odometer_reading} miles on it"

    def update_odometer(self, odometer_reading):
        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print("\n You can not roll back odometer")


    def increment_odometer(self, odometer):
        self.odometer_reading += odometer



class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def get_details(self):
        battery_info = f"\n This Car has a {self.battery_size}kwh battery"
        return battery_info

    def battery_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 200

        print(f"\n This car can go {range} miles on a full charge battery")

    def increment_battery_size(self):
        if self.battery_size != 65:
            self.battery_size = 65

        self.battery_range()


class Electric_car(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)

        self.battery = Battery()


