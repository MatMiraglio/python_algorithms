from enum import Enum
from typing import List

class LinkNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        self._iterator = self
    
    def __str__(self): 
       return 'Node: %s' % (self.val)

    def __len__(self):
        length = 1
        next = self.next

        while next:
            length += 1
            next = next.next 
            
        return length

    def __iter__(self):
        return self

    def __next__(self):
        if self._iterator:
            current_node = self._iterator
            self._iterator = self._iterator.next
            return current_node
        else:
            raise StopIteration

    @staticmethod
    def create_linked_list(length : int):
        head = LinkNode(0)
        node = head
        for _ in range(1, length):
            node.next = LinkNode(_)
            node = node.next

        return head

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

    def get_neighbours(self):
        return self.adjacency_list

    def add_adjacent(self, node):
        self.adjacency_list += [node]

    def visited(self):
        self.state = State.Visited


class State(Enum):
    Unvisited = 0
    Visiting = 1
    Visited = 2