from collections import deque
from constants import *


class Bfs(object):

    def find_path(self, start, end, graph):
        grid = graph.graph
        queue = deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if grid[y][x] == APPLE:
                return path
            for x2, y2 in graph.adjacent_edges(x, y):
                if graph.in_bounds(x2, y2) \
                        and (x2, y2) not in seen \
                        and graph.in_bounds(y2, x2) \
                        and grid[y2][x2] != (SNAKEHEAD or SNAKEBODY):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
