from algorithms.astar import AStar
from algorithms.bfs import Bfs


class Pathfinder(AStar, Bfs):
    def __init__(self, start, end, graph, algorithm):
        self.name = algorithm

        self.finder = {
            AStar.NAME: lambda x, y, z: AStar().find_path(x, y, z),
            Bfs.NAME: lambda x, y, z: Bfs().find_path(x, y, z)
        }

        self.path = self.finder[self.name](start, end, graph)

    def get_path(self, start, end, graph):
        self.path = self.finder[self.name](start, end, graph)
