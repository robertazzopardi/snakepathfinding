import pygame
import sys
import os

from config import cfg_dict as cfg

class Snake(object):
    def __init__(self, display):
        self.display = display
        self.x = cfg['disp_width']/2
        self.y = cfg['disp_height']/2
        self.r = 20
        self.body = pygame.Rect((self.x, self.y), (self.r, self.r))
        self.rect = pygame.draw.rect(display, cfg['snake_colour'], self.body)
        
    def move(self, keys):
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.r, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.r, 0)
        elif keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.r)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.r)

    def draw(self):
        # self.rect.move(self.w*x, self.h*y)
        pygame.draw.rect(self.display, (0, 0, 128), self.rect)
        