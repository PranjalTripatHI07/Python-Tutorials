from electric_car_module import Electric_car
from electric_car_module import Car

test1 = Electric_car("Audi", "AU", 2020)

print(test1.get_details())
print(test1.battery.battery_details())

test2 = Car("Nishan", "NISHAN45", 2020)
print(test2.get_details())