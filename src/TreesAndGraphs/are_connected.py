from Node import Node, State
from Queue import Queue 
from Graph import Graph

def are_conected(graph : Graph, start : Node, end : Node) -> bool:
    if start == end:
        return True
    
    nodes = graph.get_nodes()
    for node in nodes:
        node.state = State.Unvisited

    queue = Queue()
    start.state = State.Visiting
    queue.add(start)

    while queue.is_not_empty():
        current = queue.remove()
        current.state = State.Visiting

        for node in current.get_neighbours():
            if node.state == State.Unvisited:
                if node == end:
                    return True
                else:
                    node.state = State.Visiting
                    queue.add(node)
        
        current.visited()

    return False

 