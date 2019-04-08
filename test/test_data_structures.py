from ..src.data_structures.nodes import LinkNode
from ..src.linked_lists.swap_pairs import swap_pairs

import unittest


class Test(unittest.TestCase):

    def test_create_linked_list(self):
        expected_size = 8
        actual_size = 0
        head = LinkNode.create_linked_list(expected_size)
        while head:
            actual_size += 1
            head = head.next

        assert expected_size == actual_size

    def test_linked_list_len(self):
        size = 8
        head = LinkNode.create_linked_list(size)
        assert len(head) == size

    def test_linked_list_iter(self):
        size = 3
        head = LinkNode.create_linked_list(size)
        for i, node in enumerate(head):
            assert node.val == i

    def test_swap_pairs(self):
        linked_list = LinkNode.create_linked_list(6)
        head = swap_pairs(linked_list)
        expected_order = [1, 0, 3, 2, 5, 4]
        for node, value in zip(head, expected_order):
            assert node.val == value


if __name__ == '__main__':
    unittest.main()
