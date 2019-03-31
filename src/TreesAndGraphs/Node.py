from enum import Enum 
from typing import List

class Node():
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list : List[Node] = adjacency_list or []
        self.shortest_path = None
        self.state = State.Unvisited
    
    def add_edge_to(self, node):
        self.adjacency_list += [node]

    def get_neighbours(self) -> List[Node]:
        return self.adjacency_list

    def __str__(self):
        return self.data

    def visited(self):
        self.state = Visited

class State(Enum):
    Unvisited = 0
    Visiting = 1
    Visited = 2