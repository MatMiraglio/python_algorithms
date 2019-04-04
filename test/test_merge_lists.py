from ..src.data_structures.nodes import LinkNode
from ..src.linked_lists.merge_two_lists import mergeTwoLists
import unittest

class Test(unittest.TestCase):
    
    def test_create_linked_list(self):
        first = LinkNode.create_linked_list(2)
        second = LinkNode.create_linked_list(3)
        result = mergeTwoLists(first, second)
        values = [0,0,1,1,2]
        assert len(result) == 5
        for expected, actual in zip(values, result):
            assert expected == actual.val



if __name__ == '__main__':
    unittest.main()