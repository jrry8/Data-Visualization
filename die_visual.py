import pygal

from die import Die

die = Die()

res = []
for _ in range(1000):
    res.append(die.roll())

freq = []
for val in range(1, die.num_sides+1):
    freq.append(res.count(val))

hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = [str(i+1) for i in range(6)]
hist.x_title = 'Result'
hist.y_title = 'Frequency'
hist.add('D6', freq)
hist.render_to_file('die_visual.svg')