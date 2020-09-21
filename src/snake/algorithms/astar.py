from constants import SNAKE_BODY, SNAKE_HEAD
from collections import deque


class AStar:
    NAME = "Astar"

    @staticmethod
    def find_path(start, end, graph):
        G = {}
        F = {}

        G[start] = 0
        F[start] = graph.heuristic(start, end)

        closed_vertices = set()
        open_vertices = set([start])
        came_from = {}

        while len(open_vertices) > 0:
            current = None
            current_fscore = None
            for pos in open_vertices:
                if current is None or F[pos] < current_fscore:
                    current_fscore = F[pos]
                    current = pos

            if current == end:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()

                return path[1:]

            open_vertices.remove(current)
            closed_vertices.add(current)

            x, y = current

            for x2, y2 in graph.adjacent_edges(x, y):
                neighbour = (x2, y2)
                if neighbour in closed_vertices:
                    continue
                candidate_g = G[current] + graph.move_cost(neighbour)

                try:
                    if neighbour not in open_vertices and graph.board[y2][x2] != (SNAKE_BODY or SNAKE_HEAD):
                        open_vertices.add(neighbour)
                    elif candidate_g >= G[neighbour]:
                        continue
                except Exception:
                    pass

                came_from[neighbour] = current
                G[neighbour] = candidate_g
                H = graph.heuristic(neighbour, end)
                F[neighbour] = G[neighbour] + H
