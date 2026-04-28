#15-1. Cubes: A mumber raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.
import matplotlib.pyplot as plt
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)
ax.set_title("Cubic Numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)
ax.tick_params(labelsize = 14)
ax.axis([0,5100,0, 125_000_000_000])
ax.ticklabel_format(style = 'plain')
plt.show()
#15-2 Colored Cubes
import matplotlib.pyplot as plt
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues)
ax.set_title("Cubic Numbers", fontsize = 14)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)
ax.tick_params(labelsize = 14)
ax.axis([0,5100,0, 125_000_000_000])
ax.ticklabel_format(style = 'plain')
plt.show()
#15-3. Molecular Motion
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c = 'blue', linewidth = 1)
    ax.set_aspect('equal')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
#15-4. Modified Random Walk
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c = 'blue', linewidth = 1)
    ax.set_aspect('equal')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
#15-5. Refactoring
from random import choice
class RandomWalk:
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step, y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
    def get_step(self):
        x_direction = choice([1,-1])
        x_distance = choice([0,1,2,3,4])
        x_step = x_direction * x_distance
        y_direction = choice([1,-1])
        y_distance = choice([0,1,2,3,4])
        y_step = y_direction * y_distance
        return x_step, y_step
#15-6. Two D8s
from die import Die
import plotly.express as px
die_1 = Die(8)
die_2 = Die(8)
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of rolling two D8 1000 times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick =1)
fig.show()
print(results)
print(frequencies)
#15-7. Three Dice
from die import Die
import plotly.express as px
die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of rolling three D6 1000 times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick =1)
fig.show()
print(results)
print(frequencies)
#15-8. Multiplication
from die import Die
import plotly.express as px
die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of multiplying two D6 1000 times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick =1)
fig.show()
print(results)
print(frequencies)
#15-9. Die Comprehension
from die import Die
import plotly.express as px
die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results of rolling two D6 1000 times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick =1)
fig.show()
print(results)
print(frequencies)
#15-10. Practicing with Both Libraries
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, c = 'blue', linewidth = 1)
    ax.set_aspect('equal')
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break