import pygal

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]


# Analyze the results.
frequencies = []
x_labels = []
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]
x_labels = [str(value) for value in range(1, max_result+1)]


# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling and multiplying two D6 dice 1000 times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6*D6', frequencies)
hist.render_to_file('dice_visual.svg')
