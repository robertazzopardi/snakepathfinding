import pathfinder

from window import Window
from game import Game

if __name__ == "__main__":
    Game(Window(), pathfinder.AStar.NAME)
    # Game(Window(), pathfinder.Bfs.NAME)
