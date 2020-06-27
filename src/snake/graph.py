import numpy as np
import platform
import os

from config import cfg_dict as cfg


class Graph(object):
    def __init__(self, snake, apple):
        self.width = cfg['board_size']
        self.height = cfg['board_size']
        self.graph = np.zeros(
            (self.width, self.height), dtype=np.int)
        self.graph[apple.relative_pos[1], apple.relative_pos[0]] = cfg['apple']
        self.graph[snake[0].relative_pos[1],
                   snake[0].relative_pos[0]] = cfg['snake_head']

    def update(self, snake, apple):
        self.graph = np.zeros(
            (cfg['board_size'], cfg['board_size']), dtype=np.int)

        self.graph[apple.relative_pos[1], apple.relative_pos[0]] = cfg['apple']
        try:
            self.graph[snake[0].relative_pos[1],
                       snake[0].relative_pos[0]] = cfg['snake_head']
            for s_body in snake[1:]:
                self.graph[s_body.relative_pos[1],
                           s_body.relative_pos[0]] = cfg['snake_body']
        except:
            pass
        
    def adjacent_edges(self):
        pass

    def in_bounds(self, x, y):
        if x < self.width and x > 0:
            return True
        elif y < self.height and y > 0:
            return True

    def print_graph(self):
        if platform.system() == ("Darwin" or "Linux"):
            os.system('clear')
        else:
            os.system('cls')

        print(self.graph)
