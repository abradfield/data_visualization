from random import choice


class RandomWalk():
    """
    A class to generate random walks
    """

    def __init__(self, num_points=5000):
        """
        initialize attributes of a walk
        :param num_points: # of points to be generated
        """
        self.num_points = num_points

        # All walks start at [0, 0]
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """
        calculate all points in the walk
        :return:
        """
        # Take steps until walk length reached

        while len(self.x_values) < self.num_points:
            next_step = self.get_step()

            # Reject moves that go nowhere
            if next_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + next_step[0]
            next_y = self.y_values[-1] + next_step[1]

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4])
        y_step = y_direction * y_distance

        step = (x_step, y_step)

        return step
