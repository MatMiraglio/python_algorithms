from Node import Node

class Graph:
    
    def __init__(self, nodes = Node):
        self.nodes = nodes or []

    def get_nodes(self):
        return self.nodes
    