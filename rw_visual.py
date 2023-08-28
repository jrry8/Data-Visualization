import matplotlib.pyplot as plt

from random_walk import RandomWalk

while (True):
    rw = RandomWalk()
    rw.fill_walk()
    point_num = list(range(rw.num_points))
    plt.scatter(rw.x_vals, rw.y_vals, s=1, edgecolors='none', c=point_num, cmap=plt.cm.Blues)
    #plt.plot(rw.x_vals, rw.y_vals, linewidth=1)
    # emphasize start and end point
    plt.scatter(rw.x_vals[0], rw.y_vals[0], s=25, c='green', edgecolors='none')
    plt.scatter(rw.x_vals[-1], rw.y_vals[-1], s=25, c='red', edgecolors='none')
    # remove axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? [y/n]: ")
    if keep_running == 'n':
        break