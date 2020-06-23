import pygame
import sys
import numpy as np

from config import cfg_dict as cfg


class Snake(object):
    def __init__(self, display, pos):
        self.display = display
        self.colour = cfg['snake_colour']
        self.r = cfg['disp_width']/50
        self.pos = pos
        self.v = (0, -1)
        self.body = pygame.Rect(self.pos, (self.r, self.r))
        self.rect = pygame.draw.rect(display, self.colour, self.body)

    def update(self, vel):
        self.v = vel

    def check_state(self, apple, snake, game):
        if self.rect.topleft[0] >= cfg['disp_width']:
            game.restart()
        elif self.rect.topleft[0] <= 0:
            game.restart()
        elif self.rect.topleft[1] >= cfg['disp_height']:
            game.restart()
        elif self.rect.topleft[1] <= 0:
            game.restart()
        elif any(self.rect.topleft == x.rect.topleft for x in snake[1:]):
            game.restart()
        elif self.rect.topleft == apple.rect.topleft:
            return True

    def draw(self, newpos=None):
        self.prev = self.rect.topleft
        if newpos is None:
            self.vel = (self.v[0]*self.r, self.v[1]*self.r)
            self.rect.move_ip(self.vel)
        else:
            self.rect.topleft = newpos

        pygame.draw.rect(self.display, self.colour, self.rect)
