class User():
    """A simple User class"""
    def __init__(self, first_name, last_name, username, admin=False):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.admin = admin
        self.login_attempts = 0

    def describe_user(self):
        output = "\nusername: " + self.username 
        output += "\n\tfirst_name: " + self.first_name
        output += "\n\tlast_name: " + self.last_name
        output += "\n\tadmin: " + str(self.admin) 
        print(output)

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

josh = User("joshua", "love", "jlove", True)
josh.increment_login_attempts()
josh.increment_login_attempts()
print(josh.login_attempts)
josh.increment_login_attempts()
print(josh.login_attempts)
josh.reset_login_attempts()
print(josh.login_attempts)
