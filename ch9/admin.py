"""A Module that defines a simple User class and Admin child class"""

from user import User

class Admin(User):
    """A simple Admin class"""
    def __init__(self, first_name, last_name, username, employee, 
                 privileges=''):
        super().__init__(first_name, last_name, username, employee)
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print('-' + privilege)

        
#josh = Admin("joshua", "love", "jlove", True, 
#             ['can add post', 'can delete post'])
#josh.show_privileges()
