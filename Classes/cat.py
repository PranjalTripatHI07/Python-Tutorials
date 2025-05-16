class Cat:
    '''
    self => self is a parameter represent  object created for the class
    name and age are parameter for __init__()method or function
    self.name and self.age are object attributes
    self.name = name and self.age = age => name and age parameter is assign to self.name and self.age attribute
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"\n {self.name.title()} is meowing his age is {self.age}")
    def rolling(self):
        print(f"\n {self.name.title()} is rolling his age is {self.age}")




# Parameter are variable used in function or method
# attributes are variable belongs to the class or object of that class