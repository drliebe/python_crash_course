class Restaurant():
    """A class modeling a simple restaurant."""
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print('Restaurant name: ' + self.restaurant_name + 
              ' Cuisine type: ' + self.cuisine_type)

    def open_restaurant(self):
        print('We are now open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_number_served):
        self.number_served += additional_number_served

restaurant = Restaurant("Josh's Curry House", "Thai")
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(15)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)
