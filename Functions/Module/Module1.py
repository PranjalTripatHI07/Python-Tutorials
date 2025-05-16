# Here we are creating a module for making pizza and use that module file to our main pizza.py file

def make_pizza(size, *toppings):
    print(f"\n  Make a {size.title()} pizza with the following toppings:- ")
    for topping in toppings:
        print(f"\n -{topping.title()}")


