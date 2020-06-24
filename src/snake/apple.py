import pygame

from config import cfg_dict as cfg
from random import randrange


class Apple(object):
    def __init__(self, display, snake):
        self.display = display
        self.colour = cfg['apple_colour']
        self.r = cfg['square_size']

        self.x = randrange(0, cfg['disp_width'], self.r)
        self.y = randrange(0, cfg['disp_height'], self.r)
        self.pos = (self.x, self.y)

        self.body = pygame.Rect(self.pos, (self.r, self.r))
        self.rect = pygame.draw.rect(display, self.colour, self.body)

    def draw(self):
        pygame.draw.rect(self.display, self.colour, self.rect)
