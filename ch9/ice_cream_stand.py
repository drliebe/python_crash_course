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


class IceCreamStand(Restaurant):
    """A class modeling a simple ice cream stand."""
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name, 'ice cream')
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print('-' + flavor)


bonnie_doon = IceCreamStand('Bonnie Doon', ['chocolate', 'vanilla', 
                            'strawberry'])
bonnie_doon.display_flavors()