from constants import SNAKE_BODY, SNAKE_HEAD
from collections import deque


class AStar:
    NAME = "Astar"

    def find_path(self, start, end, graph):
        self.G = {}
        self.F = {}

        self.G[start] = 0
        self.F[start] = graph.heuristic(start, end)

        self.closed_vertices = set()
        self.open_vertices = set([start])
        self.came_from = {}

        while len(self.open_vertices) > 0:
            current = None
            current_fscore = None
            for pos in self.open_vertices:
                if current is None or self.F[pos] < current_fscore:
                    current_fscore = self.F[pos]
                    current = pos

            if current == end:
                path = [current]
                while current in self.came_from:
                    current = self.came_from[current]
                    path.append(current)
                path.reverse()

                return path[1:]

            self.open_vertices.remove(current)
            self.closed_vertices.add(current)

            x, y = current
            self.check_state(end, graph, x, y, current)

    def check_state(self, end, graph, x, y, current):
        for x2, y2 in graph.adjacent_edges(x, y):
            neighbour = (x2, y2)
            if neighbour in self.closed_vertices:
                continue

            candidate_g = self.G[current] + graph.move_cost(neighbour)

            try:
                if neighbour not in self.open_vertices and graph.board[y2][x2] != (SNAKE_BODY or SNAKE_HEAD):
                    self.open_vertices.add(neighbour)
                elif candidate_g >= self.G[neighbour]:
                    continue
            except Exception:
                pass

            self.came_from[neighbour] = current
            self.G[neighbour] = candidate_g
            H = graph.heuristic(neighbour, end)
            self.F[neighbour] = self.G[neighbour] + H
