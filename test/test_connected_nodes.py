from ..src.data_structures.nodes import UndirectedNode
from ..src.data_structures.graph import Graph
from ..src.TreesAndGraphs.connected_nodes import connected_nodes
import unittest


class Test(unittest.TestCase):

    def test_connected_nodes(self):
        node_j = UndirectedNode('J')
        node_i = UndirectedNode('I')
        node_h = UndirectedNode('H')
        node_d = UndirectedNode('D')
        node_f = UndirectedNode('F', [node_i])
        node_b = UndirectedNode('B', [node_j])
        node_g = UndirectedNode('G', [node_d, node_h])
        node_c = UndirectedNode('C', [node_g])
        node_a = UndirectedNode('A', [node_b, node_c, node_d])
        node_e = UndirectedNode('E', [node_f, node_a])
        node_x = UndirectedNode('Disconnected')
        node_d.add_adjacent(node_a)
        node_h.add_adjacent(node_i)
        graph = Graph([node_j, node_i, node_h, node_d, node_f, node_b, node_g, node_c, node_a, node_e, node_x])

        self.assertTrue(connected_nodes(graph, node_a, node_j))
        self.assertTrue(connected_nodes(graph, node_a, node_i))
        self.assertFalse(connected_nodes(graph, node_a, node_x))


if __name__ == "__main__":
    unittest.main()
