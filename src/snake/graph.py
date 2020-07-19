import numpy as np
import platform
import os
from constants import *


class Graph(object):
    def __init__(self, snake, apple):
        self.width = WIDTH
        self.height = HEIGHT
        self.graph = np.zeros(
            (self.width, self.height), dtype=np.int)
        self.graph[apple.relative_pos[1], apple.relative_pos[0]] = APPLE
        self.graph[snake[0].relative_pos[1],
                   snake[0].relative_pos[0]] = SNAKEHEAD

    def update(self, snake, apple):
        self.graph = np.zeros(
            (BOARDLENGTH, BOARDLENGTH), dtype=np.int)

        self.graph[apple.relative_pos[1], apple.relative_pos[0]] = APPLE
        try:
            self.graph[snake[0].relative_pos[1],
                       snake[0].relative_pos[0]] = SNAKEHEAD
            for s_body in snake[1:]:
                self.graph[s_body.relative_pos[1],
                           s_body.relative_pos[0]] = SNAKEBODY
        except:
            pass

    def adjacent_edges(self, x, y):
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

    def in_bounds(self, x, y):
        if 0 <= x < len(self.graph[0]) and 0 <= y < len(self.graph):
            return True
        return False

    def print_graph(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        print(self.graph)

    def heuristic(self, start, goal):
        # Use Chebyshev distance heuristic if we can move one square either
        # adjacent or diagonal
        D, D2 = 1, 1
        dx, dy = abs(start[0] - goal[0]), abs(start[1] - goal[1])
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

    def move_cost(self, b):
        if not self.in_bounds(b[0], b[1]):
            return 100
        return 1
