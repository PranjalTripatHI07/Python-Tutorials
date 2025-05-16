#DATE - 12/2/2025

# Sandwiches

def sandwich_orders(*orders):
    print("\n list of sandwiches ordered:- ")

    if orders:
        for order in orders:
            print(f"\n -{order.title()}")
    else:
        print("\n -Plane Sandwich ")


order_sandwiches = sandwich_orders("veg-chilli", "cheese-sandwich")
order_sandwiches = sandwich_orders("veg-fried", "veg-cheese-fried", "veg-grill", "veg-cheese-grill")
order_sandwiches = sandwich_orders("veg-chilli-grill", "veg-cheese-grill")
order_sandwiches = sandwich_orders("cheese-grill", "cheese-grill-chilli")
order_sandwiches = sandwich_orders()


def sandwich_orders(customer, *orders):
    print(f"\n list of sandwiches ordered By :-  {customer.title()} ")

    if orders:
        for order in orders:
            print(f"\n -{order.title()}")
    else:
        print("\n -Plane Sandwich ")


order_sandwiches = sandwich_orders("Willi-van", "veg-chilli", "cheese-sandwich")
order_sandwiches = sandwich_orders("Iron-man", "veg-fried", "veg-cheese-fried", "veg-grill", "veg-cheese-grill")
order_sandwiches = sandwich_orders("bat-man", "veg-chilli-grill", "veg-cheese-grill")
order_sandwiches = sandwich_orders("super-man", "cheese-grill", "cheese-grill-chilli")
order_sandwiches = sandwich_orders("bruce-van")


#Userprofile

def build_user_profile(username, **userinfo):
    print(f"\n Display User info of username:- {username}")
    return userinfo


user_profile = build_user_profile(username="willie_van", first_name ="Willie", last_name = "van", Country ="USA", City = "new-york")
print(user_profile)
user_profile = build_user_profile(username="iron-man", first_name = "tony", last_name = "stark", Country = "USA", City = "new-york")
print(user_profile)


#Car
def car_info(**carinfo):

    print("\n Display the Car information")
    return carinfo

car_information = car_info(Manufacturer="BMW", Model="BMW iX M60", Price = "1.21 Cr", Color = "White", Top_Spped = "250.0 km/h")
print(car_information)
car_information = car_info(Manufacturer="Subaru", Model = "Outback", Color = "Blue", Price = "50 lakhs", Top_package = True)
print(car_information)

