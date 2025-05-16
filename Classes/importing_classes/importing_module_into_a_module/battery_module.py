class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size


    def battery_details(self):
        return f"\n This car has {self.battery_size}kwh battery"


