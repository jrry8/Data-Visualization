from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_vals = [0]
        self.y_vals = [0]

    def get_step(self, step_dist=5):
        dir = choice([-1, 1])
        dist = choice(range(step_dist))
        return dir * dist

    def fill_walk(self):
        while (len(self.x_vals) < self.num_points):
            x_step = self.get_step(17)
            y_step = self.get_step(17)

            if x_step == y_step == 0:
                continue
                
            next_x = self.x_vals[-1] + x_step
            next_y = self.y_vals[-1] + y_step
            self.x_vals.append(next_x)
            self.y_vals.append(next_y)