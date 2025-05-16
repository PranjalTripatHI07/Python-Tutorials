from Resturant_module import Restaurant

test1 = Restaurant("Atomix", "American Cuisine")
print(test1.restaurant_details())


# Admin

from Users_module import Privileges, Admin

test2 = Admin("willie", "van", "Can Update user", "can delete user", "can ban user", "can modify user details")
print(test2.user_details())
test2.privilege.show_privileges()