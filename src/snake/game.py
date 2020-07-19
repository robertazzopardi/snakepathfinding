# Core imports
import os
import sys
import pygame
import numpy as np
import platform
import time

from constants import *
from snake import Snake
from apple import Apple
from graph import Graph

from algorithms.bfs import Bfs
from algorithms.astar import AStar


class Game():

    def __init__(self, window):

        self.window = window

        self.score = 0

        self.snake = [Snake(window.display, (WIDTH/2, HEIGHT/2))]
        self.apple = Apple(window.display, self.snake)

        # make graph
        self.graph = Graph(self.snake, self.apple)

        # init search algorithm
        # self.bfs = BFS()
        self.astar = AStar(
            self.snake[0].relative_pos, self.apple.relative_pos, self.graph)

        # Run loop
        self.loop()

        self.window.quit()

    def loop(self):

        self.exit = False

        while not self.exit:
            self.check_events()

            self.check_game_state()

            self.snake_pathfinding()

            self.window.update_window(self)

    def snake_pathfinding(self):
        if self.astar.path is not None:
            next_pos, snake_head_pos = self.astar.path[0], self.snake[0].relative_pos

            if snake_head_pos[0] < next_pos[0] and snake_head_pos[1] == next_pos[1]:
                self.snake[0].update((1, 0))
            elif snake_head_pos[0] > next_pos[0] and snake_head_pos[1] == next_pos[1]:
                self.snake[0].update((-1, 0))

            elif snake_head_pos[0] == next_pos[0] and snake_head_pos[1] < next_pos[1]:
                self.snake[0].update((0, 1))
            elif snake_head_pos[0] == next_pos[0] and snake_head_pos[1] > next_pos[1]:
                self.snake[0].update((0, -1))

            self.astar.path = self.astar.path[1:]

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

        # self.player_movement(pygame.key.get_pressed(), self.snake[0])

    def restart(self):
        # time.sleep(3)
        self.score = 0
        self.exit = False
        Game(self.window)

    def check_game_state(self):
        if self.snake[0].check_state(self.apple, self.snake, self):
            self.score += 1
            self.apple = Apple(self.window.display, self.snake)
            self.snake.append(Snake(self.window.display, self.snake[0].prev))
            self.graph.update(self.snake, self.apple)
            # self.path = self.bfs.find_path(self.graph, self.snake[0].relative_pos, self.apple.relative_pos, self.snake)
            self.astar.path = self.astar.find_path(
                self.snake[0].relative_pos, self.apple.relative_pos, self.graph)
