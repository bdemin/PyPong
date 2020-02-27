import pygame


class Game():
    def __init__(self):

        pygame.init()
        self.HEIGHT = 800
        self.WIDTH = 600
        self.DISPLAY = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.DISPLAY.fill((255,255,255))

        pygame.display.set_caption("PyPong") #!

        self.run_graphics_loop()

    def run_graphics_loop(self):
        run = True
        while run:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pygame.display.update()
        pygame.quit()
