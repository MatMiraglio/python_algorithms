from ..data_structures.nodes import UndirectedNode, State
from ..data_structures.queue import Queue

def connected_nodes(graph, start : UndirectedNode, end : UndirectedNode) -> bool:
    if start == end:
        return True
    
    nodes = graph.get_nodes()
    for node in nodes:
        node.state = State.Unvisited

    queue = Queue()
    start.state = State.Visiting
    queue.enqueue(start)

    while queue.is_not_empty():
        current = queue.dequeue()
        current.state = State.Visiting
        neightbourgs = current.get_neighbours()
        for node in neightbourgs:
            if node.state == State.Unvisited:
                if node == end:
                    return True
                else:
                    node.state = State.Visiting
                    queue.enqueue(node)
        
        current.visited()

    return False
 