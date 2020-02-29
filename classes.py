import numpy as np

import pygame


class Ball(object):
    def __init__(self, display, p_area, paddle_pos_lst):
        
        self.DISPLAY = display
        self.P_AREA = p_area
        self.paddle_pos_lst = paddle_pos_lst

        self.radius = 8
        pos = (self.P_AREA['x'] + self.P_AREA['w']/2, self.P_AREA['y'] + self.P_AREA['h']/2)
        self.pos = np.array(pos)
        self.velocity = 80 * np.random.rand(2)
        self.dt = 0.2


    def update(self):
        self.pos += self.velocity * self.dt
        pos = self.pos.astype(int)
        pygame.draw.circle(self.DISPLAY, (255, 255, 255), pos, self.radius)

    def is_on_edge(self):
        if self.P_AREA['x'] >= self.pos[0] \
            or self.pos[0] >= self.P_AREA['x'] + self.P_AREA['w'] \
                or self.P_AREA['y'] >= self.pos[1] \
                    or self.pos[1] >= self.P_AREA['y'] + self.P_AREA['h']:
            print('much edge, wow')
            return True
        return False

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
        self.WIDTH = 4
        self.N_CIRCLES = 40
        self.TMAX = 2 * (self.P_AREA['h'] + self.P_AREA['w'])
        self.pos = pos

    def draw(self):
        for center in self.get_all_centers:
            pygame.draw.circle(self.DISPLAY, self.COLOR, center, self.WIDTH)

    @property
    def get_all_centers(self):
        circ_centers = []
        for t in range(self.pos, self.pos + self.N_CIRCLES):
            circ_centers.append(self.get_pos_of_param_rect(t))
        return circ_centers

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
        elif 2*self.P_AREA['w'] + self.P_AREA['h'] <= t:
            return np.array((self.P_AREA['x'] , self.P_AREA['y'] - t + 2*self.P_AREA['w'] + 2*self.P_AREA['h']))


class Player(object):
    def __init__(self, display, p_area, pos, color):

        self.score = 0
        self.has_ball = False
        self.pos = pos
        self.paddle = Paddle(display, p_area, self.pos, color)

    def update(self):
        self.paddle.draw()
