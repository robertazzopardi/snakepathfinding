from constants import *
from collections import deque


class AStar:
    NAME = "Astar"

    @staticmethod
    def find_path(start, end, graph):
        G = {}
        F = {}

        G[start] = 0
        F[start] = graph.heuristic(start, end)

        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}

        while len(openVertices) > 0:
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos

            if current == end:
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()

                # return path[1:]
                return path[1:]

            openVertices.remove(current)
            closedVertices.add(current)

            x, y = current
            for x2, y2 in graph.adjacent_edges(x, y):
                neighbour = (x2, y2)
                if neighbour in closedVertices:
                    continue
                candidateG = G[current] + graph.move_cost(neighbour)

                try:
                    if neighbour not in openVertices and graph.graph[y2][x2] != (SNAKE_BODY or SNAKE_HEAD):
                        openVertices.add(neighbour)
                    elif candidateG >= G[neighbour]:
                        continue
                except:
                    pass

                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                H = graph.heuristic(neighbour, end)
                F[neighbour] = G[neighbour] + H
