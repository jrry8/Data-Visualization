import pygal

from die import Die

num_die = int(input("How many dice do you want to roll? "))
print("How many sides does each dice have?")
dies = []
for i in range(num_die):
    prompt = "Die #" + str(i+1) + ": "
    sides = int(input(prompt))
    dies.append(Die(sides))
num_rolls = int(input("How many times do you want to roll your dice? "))

roll_values = []
for _ in range(num_rolls):
    total = 0
    for d in dies:
        total += d.roll()
    roll_values.append(total)

freq = []
max_val = sum(d.num_sides for d in dies)
for val in range(num_die, max_val+1):
    freq.append(roll_values.count(val))

hist = pygal.Bar()
hist.title = 'Results of rolling selected dice ' + str(num_rolls) + ' times.'
hist.x_labels = [str(i) for i in range(num_die, max_val+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency'
hist.add('D6', freq)
hist.render_to_file('die_visual.svg')