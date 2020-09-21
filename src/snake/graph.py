import numpy as np
import platform
import os
from constants import WIDTH, HEIGHT, APPLE, SNAKE_HEAD, BOARD_LENGTH, SNAKE_BODY


class Graph(object):
    def __init__(self, snake, apple):
        self.width = WIDTH
        self.height = HEIGHT
        self.board = np.zeros(
            (self.width, self.height), dtype=np.int)
        self.board[apple.relative_pos[1], apple.relative_pos[0]] = APPLE
        self.board[snake[0].relative_pos[1],
                   snake[0].relative_pos[0]] = SNAKE_HEAD

    def update(self, snake, apple):
        self.board = np.zeros(
            (BOARD_LENGTH, BOARD_LENGTH), dtype=np.int)

        self.board[apple.relative_pos[1], apple.relative_pos[0]] = APPLE
        try:
            self.board[snake[0].relative_pos[1],
                       snake[0].relative_pos[0]] = SNAKE_HEAD
            for s_body in snake[1:]:
                self.board[s_body.relative_pos[1],
                           s_body.relative_pos[0]] = SNAKE_BODY
        except Exception as e:
            print(e)

    def adjacent_edges(self, x, y):
        return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

    def in_bounds(self, x, y):
        if 0 <= x < len(self.board[0]) and 0 <= y < len(self.board):
            return True
        return False

    def print_board(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        print(self.board)

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
