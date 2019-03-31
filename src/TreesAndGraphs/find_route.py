from Queue import Queue
from Node import Node

def find_route(start, end):
    found_path = None
    queue = Queue()
    node = start
    node.shortest_path = [node]
    all_visited_nodes = [node]
    while node:
        for adjacent in node.adjacency_list:
        if not adjacent.shortest_path:
            adjacent.shortest_path = node.shortest_path + [adjacent]
            if adjacent == end:
            found_path = node.shortest_path + [adjacent]
            break
            queue.add(adjacent)
            all_visited_nodes.append(adjacent)
        node = queue.remove()
    for visited in all_visited_nodes:
        visited.shortest_path = None
    return found_path
    
