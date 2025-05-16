class Restaurant:
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type


    def restaurant_details(self):
        restaurant_info = f"\n  Restaurant Name = {self.restaurant_name} | Restaurant Type = {self.restaurant_type}"
        return restaurant_info.title()


