# Core imports
import os
import sys
import pygame
import numpy as np

# sys.path.insert(1, '../../snakepathfinding/src')

# Local imports
from config import cfg_dict as cfg
from snake import Snake
from apple import Apple
from algorithms import bfs


class Main():

    def __init__(self):
        """
        Initilisation
        """
        
        # Initialise pygame
        pygame.init()
        self.score = 0
        self.background_color = cfg['background_color']
        self.window_w = cfg['disp_width']
        self.window_h = cfg['disp_height']
        self.title = cfg['caption']
        self.start_pos = (self.window_w/2, self.window_h/2)
        
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(
            (self.window_w, self.window_h))
        pygame.display.set_caption(self.title)

        self.snake = [Snake(self.display, self.start_pos)]
        self.apple = Apple(self.display, self.snake)
        
        
        
        
        # make board
        self.board = np.zeros((50, 50), dtype=np.int)
        # print(self.board[self.snake[0].relative_pos[0], self.snake[0].relative_pos[1]])
        self.board[self.snake[0].relative_pos[0], self.snake[0].relative_pos[1]] = 1
        
        print(self.board.tolist())



        
        # Run loop
        self.loop()

        # Exit at end of loop
        pygame.quit()
        sys.exit(0)

    def loop(self):

        self.exit = False

        while not self.exit:
            self.check_events()
            self.update_window()
            self.check_game_state()
            self.clock.tick(10)

    def player_movement(self, keys, snake_head):
        if keys[pygame.K_RIGHT] and snake_head.v[0] != -1:
            snake_head.update((1, 0))
        elif keys[pygame.K_LEFT] and snake_head.v[0] != 1:
            snake_head.update((-1, 0))
        elif keys[pygame.K_UP] and snake_head.v[1] != 1:
            snake_head.update((0, -1))
        elif keys[pygame.K_DOWN] and snake_head.v[1] != -1:
            snake_head.update((0, 1))

    def check_events(self):
        """
        Check the events list one by one for input / exitting.
        """

        self.player_movement(pygame.key.get_pressed(), self.snake[0])

        # Check over incoming events
        for event in pygame.event.get():

            # Check for quit event
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit = True
                elif event.key == pygame.K_r:
                    self.restart()

    def restart(self):
        self.score = 0
        self.exit = False
        Main()

    def check_game_state(self):
        if self.snake[0].check_state(self.apple, self.snake, self):
            self.score += 1
            self.apple = Apple(self.display, self.snake)
            self.snake.append(Snake(self.display, self.snake[0].prev))

    def update_window(self):
        self.display.fill(self.background_color)

        for i, snake in enumerate(self.snake):
            if i == 0:
                snake.draw()
            else:
                snake.draw(self.snake[i-1].prev)

        self.apple.draw()

        pygame.display.set_caption(f"{self.title} {self.score}")

        pygame.display.update()


if __name__ == '__main__':
    main = Main()
