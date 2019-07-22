from random_walk import RandomWalk
import matplotlib.pyplot as plt


while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s = 15)
    plt.show()
    
    keep_running = input("make another walk? (Y/n): \n")
    if keep_running == 'n':
        break