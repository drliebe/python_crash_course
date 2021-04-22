class Restaurant():
    """A class modeling a simple restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name: ' + self.restaurant_name + 
              ' Cuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        print('We are now open!')

#my_restaurant = Restaurant("Josh's Curry House", "Thai")
#print(my_restaurant.restaurant_name)
#print(my_restaurant.cuisine_type)

#my_restaurant.describe_restaurant()
#my_restaurant.open_restaurant()