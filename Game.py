import pygame


class Game():
    def __init__(self):

        pygame.init()
        self.HEIGHT = 800
        self.WIDTH = 600
        self.DISPLAY = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.DISPLAY.fill((255,255,255))

        self.define_play_area()

        pygame.display.set_caption("PyPong") #!

        self.run_graphics_loop()

    def run_graphics_loop(self):
        run = True
        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                self.draw_black_rect()
                self.draw_play_area()
                pygame.display.update()
        pygame.quit()

    def define_play_area(self):
        delta = int(((self.HEIGHT+self.WIDTH) / 2 ) / 4)
        self.P_AREA = {}
        self.P_AREA['x'] = delta
        self.P_AREA['y'] = delta
        self.P_AREA['w'] = self.HEIGHT-2*delta
        self.P_AREA['h'] = self.WIDTH-2*delta

    def draw_black_rect(self):
        delta = 10
        pos = (delta, delta)
        dim = (self.HEIGHT-2*delta, self.WIDTH-2*delta)
        pygame.draw.rect(self.DISPLAY,(0,0,255), pygame.Rect(*pos, *dim))

    def draw_play_area(self):
        delta = ((self.HEIGHT+self.WIDTH) / 2 ) / 4
        pos = (delta, delta)
        dim = (self.HEIGHT-2*delta, self.WIDTH-2*delta)
        pygame.draw.rect(self.DISPLAY,(0,0,0), pygame.Rect(*pos, *dim))
