#DATE - 15/2/2025

# Topic => Classes

# Object-oriented programming => In oops we write classes that represents real world things and situations and we create object
# based on these classes

# => In class we describe the general behaviour that a whole category of object can have

# => Making an Object from a class is called instantiation

# => Instances of classes means object of classes

#Topic => Creating and using class

#Syntax => class name_of_class:
#             do something

# example

class Dog:
    def __init__(self, name, age):
        '''Here we initialize name and age attributes'''

        self.name = name
        self.age = age

    def bark(self):
        '''Here we are creating a function or we can say method describing the behaviour of dog'''
        print(f"\n {self.name.title()} is barking his age is{self.age}")
    def rolling(self):
        '''Here we are creating a function or we can say method describing the behaviour of dog'''
        print(f"\n {self.name.title()} is rolling his age is {self.age} ")


# Note
# 1. The __init__() method => __init__() is a special method that python runs automatically whenever we create a new instance(object) based on that class
# In short __init__() is a special method used for initialization of instance or object based on that class

# 2. __init__(self, other_parameters): =>
#  __init__(self, other_parameters) => The self parameter is required in the method or function definition and it comes first before other parameter

# (The self parameter is important for calling a instance of an object)

#=> The self parameter act as a reference to the instance or object itself

#=> The self parameter represent the object or instance of a class
#or => we can say that => The self parameter represent the object created from that class

#=> When we say instance of a class it means object is created from that class

# => Basically self allows us to access the attributes of the class within the class definition

# very imp
# => Parameters are variables in method or function definitions (like name, age in __init__)
# => Attributes are variables bound to class/instance(object) (like self.name, self.age, school_name)
# => Parameters are temporary during method execution
# => Attributes persist as part of the object's state

# Very Imp
# => Parameter are variables that are used in function definition
# => Attributes are variables that belongs to that class or object created from that class

# Example (This example is very important)

class Dog:
    def __init__(self, name, age): # => # Note -> (Here name and age are parameters) and (self is a parameter represent the object created from that class(Dog Class)

        # self.name and self.age are instance(object) attributes
        # self.name and self.age are instance(object) attributes

        self.name = name # parameter assigned to attribute (it means name is a parameter which assign to self.name attribute)
        self.age = age   # # parameter assigned to attribute (it means age is a parameter which assign to self.age attribute)



# Another very imp example

class Student:
    # school_name is a class attribute
    school_name = "Python High"

    def __init__(self, name, age):
        # name and age are parameters
        # self.name and self.age are instance attributes
        self.name = name  # parameter assigned to attribute (it means name is a parameter which assign to self.name attribute)
        self.age = age    # parameter assigned to attribute (it means age is a parameter which assign to self.age attribute)
        self.grade = None # attribute with no parameter

# Usage example
student1 = Student("Alice", 15)
student2 = Student("Bob", 16)

print(student1.name)  # Access attribute: Alice
print(Student.school_name)  # Access class attribute: Python High



# Topic => Making an Instance(object) from a class

# => Think of class as a set of instructions for how to make instance(object)

#Synatx =>   class name_of_class:
#               def __init__(self, parameters):
#                    self.parameters = parameters

#               do something

#            object_name = name_of_class(arguments)


#Note => Object_name refers to a single instance(object) created from a class

# Example

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"\n {self.name.title()} is sitting and his age is {self.age}")

    def roll_over(self):
        print(f"\n {self.name.title()} is rolling and his age is {self.age}")




dog_1 = Dog("willie", 14)
dog_2 = Dog("bruno", 15)


print(f"\n Name = {dog_1.name.title()} Age = {dog_1.age} ")
print(f"\n Name = {dog_2.name.title()} Age =  {dog_2.age}")
print(dog_1.sit())
print(dog_2.roll_over())

#Another Example

class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sit(self):
        return f"\n Now {self.name.title()} is {self.breed.title()} and {self.age} year old and he is going to sit"

    def roll_over(self):
        return f"\n Now {self.name.title()} is {self.breed.title()} and {self.age} year old and he is going to roll over"


cat_1 = Cat("willie", 14, "siberian-cat")
cat_2 = Cat("bruno", 15, "asian-cat")

print(f"\n {cat_1.name.title()} is {cat_1.breed} and {cat_1.age} year old")
print(f"\n {cat_1.sit()}")
print(f"\n {cat_2.sit()}")
print(f"\n {cat_1.roll_over()}")
print(f"\n {cat_2.roll_over()}")


# Topic => 1. Accessing Attributes

# => For accessing attributes of object created from that class we use dot notation

# syntax => object_name.attribute_name

# Note =>  Taking above examples

# dog_1 is the object name and .name is the parameter(whom we assign to attribute)

#In short => object_name.attribute_name and self.attribute_name these two things are represent each other
# So when we want to access the attribute we write :- syntax => object_name.attribute_name


# Topic => 2. Calling method(functions) in class

#=> When we create an object(instance) from the class we use dot notation to call any method(function) of that class

# Syntax => object_name.function_name()

# => To call a method(function) give the name of the instance(object) and the method(function) you want to  call, separated by a dot.


# Topic => 3. Creating Multiple Instances(objects)

# => We can create multiple instances(objects) from a class

# Example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"\n {self.name.title()} sitting down")


# Here we are Creating Multiple Instances(objects)
my_dog = Dog("willie", 14)
your_dog = Dog("bruno", 15)

# Here we are Accessing Attributes
print(f"\n My dog name is {my_dog.name.title()}.")
print(f"\n My dog is {my_dog.age} year old")

# Here we are Calling method(functions) in class
my_dog.sit()

# Here we are Accessing Attributes
print(f"\n Your dog name is {your_dog.name.title()}")
print(f"\n Your dog age is {your_dog.age} year old")

# Here we are Calling method(functions) in class
your_dog.sit()



#Topic => Working with classes and Instances(objects)

# 1. Modifying The attribute

# => We can modify the attributes associated with a particular instance(object)

# => We can modify the attributes of an instance(object) directly or writing methods(functions) that updates attributes in specific ways

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def get_description(self):
        car_info = f"\n Manufacturer = {self.manufacturer.title()} | Model = {self.model} | Year = {self.year}"

        return car_info



car_1 = Car("BMW", "BNMSF40", "2040")
cat_2 = Car("Audi", "AU10045", "2050")

print(car_1.get_description())
print(cat_2.get_description())


# Topic =>  Setting a default value for an attribute

#Note => Also when an instance(object) is created, attributes can be defined without being passed in as parameters
#Note => These attributes can be defined in the __init__() method(function) where they assigned a default value

class Car:
    def __init__(self, manufacture, model, year):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.odometer_reading = 0  #This is object attribute having default value

    def get_description(self):
        car_info = f"\n Manufacture_name = {self.manufacture} | Model = {self.model} | Year = {self.year}"
        return car_info.title()

    def read_odometer(self):
        print(f"\n Odometer Reading => {self.odometer_reading}")


car_1 = Car("BMW", "BM4050WT", "2024")

print(car_1.get_description())
print(car_1.read_odometer())

# or

class Car:
    def __init__(self, manufacture, model, year):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.odometer_reading = 0  # This is object attribute having default value

    def get_description(self):
        car_info = f"\n Manufacture_name = {self.manufacture} | Model = {self.model} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"
        return car_info.title()


car_1 = Car("BMW", "BM4050WT", "2024")

print(car_1.get_description())



#Topic => Modifying Attribute values

#=> We can modify or change an attribute value in 2 ways:-
# 1. We can change the value directly through an instance(object)
# 2. we can set the value through method(function) or increment the value(add a certain amount to it) through a method(function)


# 1. Modifying an attributes value directly

# Example

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        car_info = f"\n Manufacturer => {self.manufacturer} | Model => {self.model} | Year => {self.year} | Odometer Reading => {self.odometer_reading}"
        return car_info.title()


car_1 = Car("BMW","BMWWT4050", 2024)
car_1.odometer_reading = 24 # Here we modify or change the default value of self.odometer_reading (this is the direct way of modifying attributes value)

print(car_1.get_description())

 # Note =>  The simplest way to modify the value of an attribute is to access the attribute directly through an instance(object)



 # 2. Modifying an attributes value through a method(function)

 # => we can set the value through method(function) or increment the value(add a certain amount to it) through a method(function)

 #Example

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0



    def get_description(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model} | Year = {self.year} | Odometer Reading = {self.odometer_reading}"
        return car_info.title()


    #Note -> important
    def update_odometer(self, odometer_reading):  # Here we create a method(function) to modify the attribute value
        self.odometer_reading = odometer_reading  # Also note =>To modify the attributes value through method(function) =>
                                                  # 1. We First define a function using self and then pass a parameter
                                                  # 2. Then we assign that parameter to object(instance) attribute(like this => self.attribute_name = parameter_name)


car_1 = Car("Audi", "AUDI4040H", 2024)

print(car_1.get_description())

car_1.update_odometer(28)  #Here we update the attribute value through calling method(function) which basically update or modify the attribute value

print(car_1.get_description())



# Another modified version

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model} | Year = {self.year} | Odometer Reading = {self.odometer_reading}"

        return car_info.title()

    def update_odometer(self, odometer_reading):

        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print("\n You cannot roll back an odometer")



car_1 = Car("Audi", "AUDI4040H", 2024)

print(car_1.get_description())

car_1.update_odometer(24)

print(car_1.get_description())

car_1.update_odometer(42)  #Here we update the attribute value through calling method(function)

print(car_1.get_description())


#Topic => Incrementing an attribute value through a method

# => We can increment an attributes value using method(function)

#Example =>

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Here we set default object attribute value


    def get_description(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model} | Year = {self.year} | Odometer Reading = {self.odometer_reading}"

        return car_info.title()

    def update_odometer_value(self, odometer_reading):

        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading

        else:
            print("\n Odometer reading can't roll back")



    def increment_odometer_value(self, miles_cover):
        '''Here we are incrementing the object attribute'''
        self.odometer_reading += miles_cover



car_1 = Car("Audi", "AUDI45450", 2024)

print(car_1.get_description())

car_1.update_odometer_value(25000)

print(car_1.get_description())

car_1.increment_odometer_value(2500)

print(car_1.get_description())


# Topic => Inheritance

# Inheritance => When one class inherits the attributes and methods(functions) of another class that is called inheritance
# In Inheritance we have original class which is called parent class and the new class is called child class
# The child class can inherit any or all the attributes and methods(functions) of its parent class
# and it also free to define new attributes and methods(functions) of its own

# Topic => 1. The __init__() method for child class

#Note => when we write a new class based on existing class we have to call the __init__() method from the parent class because
# this will help us to initialize any attributes that were define in the parent __init__() method and make them available in the child class

#Example

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n  Manufacturer = {self.manufacturer} | Model = {self.model} | Year = {self.year} | Odometer Reading = {self.odometer_reading}"
        return car_info.title()

    def update_odometer(self, odometer_reading):
        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print("\n we can not roll back odometer reading")

    def increment_miles(self, miles):
        self.odometer_reading += miles




class Electric_car(Car): #Note => # Here we are mention which parent class attributes and methods we are inheriting so we mention the name of that class in the child class parameter
    def __init__(self, manufacturer, model, year): # Note => Here we are initializing the attributes which we are using in our parent class.
        super().__init__(manufacturer, model, year) # Note => Super() function is a special function that allows us to call the __init__() method and all other method(functions) from parent class
                                                     # Which gives child class instance(object) all the attributes and methods(functions) define in the parent class __init__() method.
                                                     # Note => Parent class is supper class and child class is subclass
# Another Definition of supper()
# => The super() function in Python which is used to call methods(functions) from a parent class
#It is commonly used to invoke the __init__() method of a parent class, allowing the child class to inherit and initialize attributes from the parent.
#super() can also be used to call any method from the parent class, not just __init__().



electric_car1 = Electric_car("Nishan", "NIH44", 2020)

print(electric_car1.get_details())

electric_car1.update_odometer(250000)
print(electric_car1.get_details())

electric_car1.increment_miles(1100)
print(electric_car1.get_details())

#Another example

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


# Topic => Defining Attributes and Methods for the child class

#Note =>  In child class we can add any new attributes and methods(functions) which is necessary to differentiate the child class from parent class


class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model.upper()} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"

        return car_info.title()

    def update_odometer_reading(self, odometer_reading):
        if odometer_reading >= self.odometer_reading:
            self.odometer_reading = odometer_reading
        else:
            print("\n Odometer_reading cannot changed")

    # 1km => 1 unit of odometer
    def increment_km(self, kilometer_traveled):
        self.odometer_reading = kilometer_traveled




class Electric_Car(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)

        self.battery = "400maH"

    def battery_info(self):
        battery_details = f"\n  Battery Capacity = {self.battery}"
        return battery_details.title()





electric_car_1 = Electric_Car("Nishan", "NIH4450", "2020")

print(electric_car_1.get_details())

print(electric_car_1.battery_info())




# Topic => Overriding methods from parent class

#=> We can override any method from the parent class
#=> To do this we define a method in child class with the same name as the method you want to override in the parent class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer = {self.make} | Model = {self.model} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"
        return car_info

    def fill_gas_tank(self):
        info = f"\n This Car {self.model} model have to fill gas"
        return info



class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = "40mah"


    def battery_info(self):
        battery_details = f"\n  Battery Capacity = {self.battery}"
        return battery_details

    def fill_gas_tank(self):   #Here we override the method of parent class
        info = f"\n This Car {self.model} model have no need of fuel tank"
        return info



car_1 = Car("Audi", "AUDI4450", 2020)
electric_car1 = Electric_car("Nishan", "NISH4500", 2020)

print(car_1.get_details())
print(electric_car1.get_details())

print(car_1.fill_gas_tank())
print(electric_car1.fill_gas_tank())



# Instances(object or class) as Attribute

#=> Imp Note => We can break large class into smaller classes that work together and this called Composition

class Car:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info = f"\n Manufacturer = {self.manufacturer} | Model = {self.model} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"

        return car_info.title()

    def fuel_tank(self):
        return f"\n This {self.model} car model have 45L gas tank"


class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def get_battery_details(self):
        return f"\n  This car has {self.battery_size}kwh Battery"



class Electric_Car(Car):
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)

        self.battery = Battery() #Imp Note => self.battery = Battery() creates a composition relationship between Electric_car and Battery classes
                                 # Battery() creates a new instance(object) of the Battery class
                                 # self.battery stores this Battery instance(object) as an attribute of the Electric_car instance(object)

    def fuel_tank(self):
        return f"\n This {self.model} car model have no need of fuel tank"



car_1 = Car("Audi", "AU24", 2020)

electric_car1 = Electric_Car("Tesla", "MODEL4", 2024)


print(car_1.get_details())

print(electric_car1.get_details())

# Override example
print(car_1.fuel_tank())
print(electric_car1.fuel_tank())




#instance(object or class) as attributes
# Here we => Call battery methods via =>  electric_car_1.battery.describe_battery()
print(electric_car1.battery.get_battery_details())






# Another example

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_details(self):
        car_info =  f"\n Manufacturer = {self.make} | Model = {self.model} | Year = {self.year} | Odometer_reading = {self.odometer_reading}"
        return car_info.title()


    def fuel_tank(self):
        return  f"\n This {self.model} car model have 45L gas tank"



class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def battery_details(self):
        return f"\n  This car has {self.battery_size} kwh battery"

    def battery_range(self):
        if self.battery_size == 40:
            return f"\n This car range is 150 km on full charge battery"
        elif self.battery_size == 65:
            return f"\n This car range is 200 km on full charge battery"


class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery() #Here we simply create a object attribute and assign a class from which we want cant to use that class methods



    def fuel_tank(self):
        return f"\n This {self.model} car model have no need of gas tank"


electric_car1 = Electric_car("Tesla", "MODEL4", 2024)

print(electric_car1.get_details())
print(electric_car1.battery.battery_range())
print(electric_car1.battery.battery_details())


#Another Example for instance(object) as attribute or class as attribute

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

        self.privilege = Privileges(*privileges)



admin1 = Admin("Willie", "van","can ban users", "can delete users", "can add user", "can update user info")


print(admin1.user_details())
print(admin1.greet_user())
admin1.privilege.show_privileges()




#Another Example for instance(object) as attribute or class as attribute

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
        self.get_battery_range()  #Imp Note => for using a function into another function we write syntax => self.name_of_function



class Electric_car(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()


electric_car1 = Electric_car("Audi", "AU", 2020)

electric_car1.battery.upgrade_battery()
