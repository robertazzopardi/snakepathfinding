import pygame
from random import randrange
from constants import APPLE_COLOUR, OBJECT_SIZE, WIDTH, HEIGHT


class Apple(object):
    def __init__(self, display, snake):
        self.display = display
        self.colour = APPLE_COLOUR
        self.r = OBJECT_SIZE

        self.snake = snake
        self.set_pos()

        self.body = pygame.Rect(self.pos, (self.r, self.r))
        self.rect = pygame.draw.rect(display, self.colour, self.body)

        self.relative_pos = (
            int(self.rect.topleft[0]/self.r), int(self.rect.topleft[1]/self.r))
        # print(self.relative_pos)

    def set_pos(self):
        self.x = randrange(0, WIDTH, self.r)
        self.y = randrange(0, HEIGHT, self.r)
        self.pos = (self.x, self.y)
        if any(self.pos == x.rect.topleft for x in self.snake):
            self.set_pos()

    def draw(self):
        self.relative_pos = (
            int(self.rect.topleft[0]/self.r), int(self.rect.topleft[1]/self.r))
        pygame.draw.rect(self.display, self.colour, self.rect)
