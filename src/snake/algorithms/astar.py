import numpy
import pygame

from collections import deque
from config import cfg_dict as cfg


class AStar(object):
     
    def find_path(self, start, end, graph):
     
        G = {} #Actual movement cost to each position from the start position
        F = {} #Estimated movement cost of start to end going via this position
    
        #Initialize starting values
        G[start] = 0 
        F[start] = graph.heuristic(start, end)
    
        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}
    
        while len(openVertices) > 0:
            #Get the vertex in the open list with the lowest F score
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos
    
            #Check if we have reached the goal
            if current == end:
                #Retrace our route backward
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()
                return path#, F[end] #Done!
    
            #Mark the current vertex as closed
            openVertices.remove(current)
            closedVertices.add(current)
    
            #Update scores for vertices near the current position
            # for neighbour in graph.get_vertex_neighbours(current):
            x, y = current
            for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                neighbour = (x2, y2)
                if neighbour in closedVertices: 
                    continue #We have already processed this node exhaustively
                candidateG = G[current] + graph.move_cost(current, neighbour)
    
                try:
                    if neighbour not in openVertices and graph.graph[y2][x2] != (cfg['snake_body'] or cfg['snake_head']):
                        openVertices.add(neighbour) #Discovered a new vertex
                    elif candidateG >= G[neighbour]:
                        continue #This G score is worse than previously found
                except:
                    pass
                
                #Adopt this G score
                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                H = graph.heuristic(neighbour, end)
                F[neighbour] = G[neighbour] + H
    
        # raise RuntimeError("A* failed to find a solution")