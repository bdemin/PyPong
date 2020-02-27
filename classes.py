import numpy as np


class Ball(object):
    def __init__(self):

        self.radius = 1
        self.position = np.zeros(2)
        self.velocity = np.zeros(2)


    def move(self):
        pass

    def bounce(self):
        pass

    def is_out(self):
        pass

    def change_color(self):
        pass


class Paddle(object):
    def __init__(self):

        self.width = 1
        self.position = np.zeros(2)

    def draw(self):
        pass

    def move(self):
        pass


class Player(object):
    def __init__(self):

        self.score = 0
        self.has_ball = False
