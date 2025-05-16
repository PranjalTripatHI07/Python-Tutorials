def make_pizza(size, *toppings):
    print(f"\n Make a {size} pizza with the following toppings:- ")

    for topping in toppings:
        print(f"\n -{topping}")