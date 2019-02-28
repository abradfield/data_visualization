import pygal
from die import Die

# Create a D6
die1 = Die()
die2 = Die(10)

# Make some rolls and store results in a list
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_results = die1.num_sides + die2.num_sides
for value in range(2, max_results):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')
