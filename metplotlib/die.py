from random import randint
import pygal

class Die():
    
    def __init__(self, num = 6):
        self.num = num
    
    def roll(self):
        return randint(1, self.num)
    

die = Die()

res = []
for num in range(100):
    res1 = die.roll()
    res.append(res1)

frequencies = []

for value in range(1, die.num + 1):
    frequency = res.count(value)
    frequencies.append(frequency)
    
print(frequencies)

bar = pygal.Bar()
bar.title = 'yes'
bar.x_labels = [str(value) for value in range(1, 7)]
bar.x_title = 'die_num'
bar.add('d6', frequencies)
bar.render_to_file('dies_bar.svg')