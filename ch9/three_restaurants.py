class Restaurant():
    """A class modeling a simple restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name: ' + self.restaurant_name + 
              ', Cuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        print('We are now open!')

my_restaurant = Restaurant("Josh's Curry House", "Thai")
bills = Restaurant("Bill's Barbeque", "Sushi")
teds = Restaurant("Ted's Sushi Palace", "Barbeque")

my_restaurant.describe_restaurant()
bills.describe_restaurant()
teds.describe_restaurant()