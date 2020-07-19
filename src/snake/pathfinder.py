from algorithms.astar import AStar
from algorithms.bfs import Bfs

print(AStar.name)


class Pathfinder(Astar, Bfs):
    def __init__(self, start, end, graph, algorithm):
        AStar.__init__(start, end, graph)
        Bfs.__init__(start, end, graph)
