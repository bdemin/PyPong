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
    def __init__(self, display, p_area, pos, color):
        
        self.COLOR = color
        self.DISPLAY = display
        self.P_AREA = p_area
        self.TMAX = 2 * (self.P_AREA['h'] + self.P_AREA['w'])
        self.pos = pos

    def draw(self):
        pass

    def move(self):
        pass
    def get_pos_of_param_rect(self, t):
        if t >= self.TMAX:
            t -= self.TMAX
        elif t < 0:
            t += self.t_max

        if 0 <= t <= self.P_AREA['w']:
            return np.array((self.P_AREA['x'] + t, self.P_AREA['y']))
        elif self.P_AREA['w'] <= t <= self.P_AREA['w'] + self.P_AREA['h']:
            return np.array((self.P_AREA['x'] + self.P_AREA['w'], self.P_AREA['y'] + t - self.P_AREA['w']))
        elif self.P_AREA['w'] + self.P_AREA['h'] <= t <= 2*self.P_AREA['w'] + self.P_AREA['h']:
            return np.array((self.P_AREA['x'] + 2*self.P_AREA['w'] - t + self.P_AREA['h'] , self.P_AREA['y'] + self.P_AREA['h']))
        # elif 2*self.P_AREA['w'] + self.P_AREA['h'] <= t <= 2*self.P_AREA['w'] + 2*self.P_AREA['h']:
        elif 2*self.P_AREA['w'] + self.P_AREA['h'] <= t:
            return np.array((self.P_AREA['x'] , self.P_AREA['y'] - t + 2*self.P_AREA['w'] + 2*self.P_AREA['h']))


class Player(object):
    def __init__(self, display, p_area, pos, color):

        self.score = 0
        self.has_ball = False
        self.pos = pos
        

        self.paddle = Paddle(display, p_area, self.pos, color)

