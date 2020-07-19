from collections import deque
from constants import *


class Bfs:
    NAME = "Bfs"

    @staticmethod
    def find_path(start, end, graph):
        grid = graph.graph
        queue = deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if grid[y][x] == APPLE:
                return path[1:]
            for x2, y2 in graph.adjacent_edges(x, y):
                if graph.in_bounds(x2, y2) \
                        and (x2, y2) not in seen \
                        and graph.in_bounds(y2, x2) \
                        and grid[y2][x2] != (SNAKE_BODY or SNAKE_HEAD):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
