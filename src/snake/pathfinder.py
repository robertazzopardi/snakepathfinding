from algorithms.astar import AStar
from algorithms.bfs import Bfs


class Pathfinder(AStar, Bfs):
    def __init__(self, start, end, graph, algorithm):
        self.name = algorithm

        self.d = {
            AStar.NAME: AStar.find_path(start, end, graph),
            Bfs.NAME: Bfs.find_path(start, end, graph)
        }

        self.path = self.d.get(self.name)

    def get_path(self, start, end, graph, algorithm):
        # self.path = self.d.get(self.name)

        if algorithm == AStar.NAME:
            self.path = AStar.find_path(start, end, graph)
        elif algorithm == Bfs.NAME:
            self.path = Bfs.find_path(start, end, graph)

        print(self.path, start)
