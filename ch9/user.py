"""A Module that defines a simple User class """

class User():
    """A simple User class"""
    def __init__(self, first_name, last_name, username, employee=False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.employee = employee

    def describe_user(self):
        output = "\nusername: " + self.username 
        output += "\n\tfirst_name: " + self.first_name
        output += "\n\tlast_name: " + self.last_name
        output += "\n\temployee: " + str(self.employee) 
        print(output)

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!")

