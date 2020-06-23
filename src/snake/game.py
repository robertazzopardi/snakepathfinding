# Core imports
import os
import sys
import pygame

# Local imports
from config import cfg_dict as cfg
from snake import Snake


class Main():

    def __init__(self):
        self.score = 0
        self.background_color = cfg['background_color']

        # Initialise pygame
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((cfg['disp_width'], cfg['disp_height']))
        pygame.display.set_caption(cfg['caption'])
        
        self.snake = Snake(self.display)
        
        # Run loop
        self.loop()

        # Exit at end of loop
        pygame.quit()

    def loop(self):

        self.exit = False

        while not self.exit:
            self.check_events()
            self.update_window()
            self.check_game_state()
            self.clock.tick(10)

    def check_events(self):
        """
        Check the events list one by one for input / exitting.
        """
        
        keys = pygame.key.get_pressed()
        self.snake.move(keys)

        # Check over incoming events
        for event in pygame.event.get():

            # Check for quit event
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit = True
                elif event.key == pygame.K_r:
                    self.score = 0
                    self.exit = False
                    Main()
                    
    def check_game_state(self):
        self.snake.check_bounds()

    def update_window(self):

        self.display.fill(self.background_color)

        self.snake.draw()
        
        pygame.display.set_caption(f"{cfg['caption']} {self.score}")

        pygame.display.update()


if __name__ == '__main__':
    main = Main()
