from car_module import Car
from battery_module import Battery

# So here above we imported module into module file

class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()
