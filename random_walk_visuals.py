import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points
while True:
    walk = RandomWalk(50000)
    walk.fill_walk()

    plt.figure(dpi=128, figsize=(12, 8))

    point_numbers = list(range(walk.num_points))
    plt.scatter(walk.x_values, walk.y_values, c=point_numbers, cmap=plt.cm.Reds,
                edgecolors='none', s=1)

    # Emphasize first and last points
    plt.scatter(0, 0, c='gray', edgecolors='none', s=100)
    plt.scatter(walk.x_values[-1], walk.y_values[-1], c='black', edgecolors='none', s=100)

    # Remove the axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
