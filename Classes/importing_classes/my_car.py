#syntax for importing class module
#from module_name import class_name

from car_class_module import Car
from car_class_module import Electric_car
from car_class_module import Car, Electric_car



test1 = Car("Audi", "AU45450", 2020)

print(test1.get_details())
print(test1.odometer_details())
test1.update_odometer(2500)
print(test1.get_details())
test1.increment_odometer(200)
print(test1.get_details())



# Topic => Storing multiple classes in a module

test2 = Electric_car("Nishan", "NISHAN45", 2020)

print(test2.get_details())
print(test2.odometer_details())
test2.update_odometer(2700)
print(test2.get_details())
print(test2.increment_odometer(100))
print(test2.get_details())

print(test2.battery.get_details())
print(test2.battery.battery_range())
print(test2.battery.increment_battery_size())


# => Topic =>Importing entire module
import car_class_module

test4 = car_class_module.Car("Audi", "AU", 2020)
print(test4.get_details())

test4 = car_class_module.Electric_car("Nishan", "NI", "2020")
print(test4.get_details())