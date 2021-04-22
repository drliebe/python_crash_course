class User():
    """A simple User class"""
    def __init__(self, first_name, last_name, username, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.admin = admin

    def describe_user(self):
        output = "\nusername: " + self.username 
        output += "\n\tfirst_name: " + self.first_name
        output += "\n\tlast_name: " + self.last_name
        output += "\n\tadmin: " + str(self.admin) 
        print(output)

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!")


josh = User("joshua", "love", "jlove", True)
bill = User("bill", "excellent", "bille", False)
ted = User("ted", "adventure", "teda", False)

josh.describe_user()
josh.greet_user()

bill.describe_user()
bill.greet_user()

ted.describe_user()
ted.greet_user()
