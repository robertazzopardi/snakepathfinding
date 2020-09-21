import pygame
from sys import exit
from constants import WIDTH, HEIGHT, BACKGROUND, FPS, TITLE


class Window(object):
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

    def update_window(self, game):
        self.display.fill(BACKGROUND)

        game.apple.draw()
        for i, snake in enumerate(game.snake):
            snake.draw() if i == 0 else snake.draw(game.snake[i-1].prev)

        ''''''
        game.graph.update(game.snake, game.apple)
        ''''''
        # self.graph.print_graph()

        pygame.display.set_caption(f"{TITLE} {game.score}")

        pygame.display.update()

        self.clock.tick(FPS)

    def quit(self):
        # Exit at end of loop
        pygame.quit()
        exit(0)
