from enum import Enum
from typing import List

class LinkNode:

    def __init__(self, val, next: LinkNode = None):
        self.val = val
        self.next = next

class TreeNode:

    def __init__(self, val, children = None, parent = None):
        self.val = val
        self.parent = parent
        self.children = children or []

class BinaryNode:

    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class UndirectedNode:

    def __init__(self, val, adjacency_list = None):
        self.val = val
        self.adjacency_list = adjacency_list or []
        self.state = State.Unvisited

    def add_adjacent(self, node):
        self.add_adjacent += [node]
    
class State(Enum):
    Unvisited = 0
    Visiting = 1
    Visited = 2