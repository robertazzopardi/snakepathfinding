import numpy

from collections import deque
from config import cfg_dict as cfg


class BFS(object):

    def find_path(self, graph, start, goal, snake):
        grid = graph.graph
        queue = deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if grid[y][x] == cfg['apple']:
                # print(path)
                return path
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):

                # if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] != wall and (x2, y2) not in seen:
                if 0 <= x2 < len(grid[0]) \
                        and 0 <= y2 < len(grid) \
                        and (x2, y2) not in seen \
                        and graph.in_bounds(y2, x2) \
                        and grid[y2][x2] != (cfg['snake_body'] or cfg['snake_head']):
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
