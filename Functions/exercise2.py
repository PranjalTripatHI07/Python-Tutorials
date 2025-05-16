# T-Shirt function
from Dictionary.Exercise15 import country


def make_shirt(size, printed_message):
    print(f"\n  The Size of the T-shirt is {size} and the message printed in T-shirt is {printed_message}")

make_shirt(size = "S", printed_message="I am not okay, I am in a Pain")

make_shirt("M", "I am not okay, its feel void inside")


# Make T-shirt function 2

def make_shirt(size = "large", printed_message = "I am not ok"):
    print(f"\n The size of the T-shirt is {size} and the message printed in T-shirt is {printed_message}")


make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "any_size", printed_message= "I am not ok I am in pain")
make_shirt(printed_message= "I am in pain")



# Cities function

def cities(name, country="USA"):
    print(f"\n {name} is in {country}")

cities(name="New York")
cities(name = "Tokyo", country = "Japan" )

