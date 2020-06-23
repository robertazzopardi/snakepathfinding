import pygame
import sys
import numpy as np

from config import cfg_dict as cfg


class Snake(object):
    def __init__(self, display):
        self.display = display
        self.colour = cfg['snake_colour']
        self.r = cfg['disp_width']/50
        self.pos = np.array([cfg['disp_width']/2, cfg['disp_height']/2])
        self.v = np.array([1, 0])
        self.body = pygame.Rect(self.pos, np.array([self.r, self.r]))
        self.rect = pygame.draw.rect(display, self.colour, self.body)

    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.v = np.array([1, 0])
        elif keys[pygame.K_LEFT]:
            self.v = np.array([-1, 0])
        elif keys[pygame.K_UP]:
            self.v = np.array([0, -1])
        elif keys[pygame.K_DOWN]:
            self.v = np.array([0, 1])
    
    def check_bounds(self):
        if self.rect.topleft[0] >= cfg['disp_width']:
            sys.exit()
        elif self.rect.topleft[0] <= 0:
            sys.exit()
        elif self.rect.topleft[1] >= cfg['disp_height']:
            sys.exit()
        elif self.rect.topleft[1] <= 0:
            sys.exit()

    def draw(self):
        self.rect.move_ip(self.v[0]*self.r, self.v[1]*self.r)
        pygame.draw.rect(self.display, self.colour, self.rect)
