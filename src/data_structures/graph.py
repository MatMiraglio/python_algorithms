class Graph:

    def __init__(self, nodes=None):
        self.nodes = nodes or []

    def get_nodes(self):
        return self.nodes

    def add_node(self, node):
        if node:
            self.nodes.append(node)
