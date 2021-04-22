import pygal

from die import Die

# Create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# Number of rolls
num_rolls = 1000000

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(num_rolls)]


# Analyze the results.
frequencies = []
x_labels = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
x_labels = [str(value) for value in range(2, max_result+1)]


# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling two D8 dice " + str(num_rolls) + " times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8+D8', frequencies)
hist.render_to_file('dice_visual.svg')
