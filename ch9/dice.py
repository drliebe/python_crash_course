from random import randint

class Die():
    """Simulates a simple dice."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))

my_6 = Die(6)
my_10 = Die(10)
my_20 = Die(20)

print('Rolling the 6 sided die.')
for roll_number in range(1,11):
    my_6.roll_die()

print('Rolling the 10 sided die.')
for roll_number in range(1,11):
    my_10.roll_die()

print('Rolling the 20 sided die.')
for roll_number in range(1,11):
    my_20.roll_die()