class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_details(self):
        car_info = f"\n Make = {self.make} | Model = {self.model} | Year = {self.year}"
        return car_info.title()


