from ..src.graphs.binary_tree_from_array import binary_tree

import unittest

class Test(unittest.TestCase):
    
    def test_binary_tree_from_array(self):        
        test_array = [1,2,3,4,5,6,7]
        head = binary_tree(test_array)
        assert head.val == 4
        assert head.left.val == 2
        assert head.left.left.val == 1
        assert head.left.right.val == 3
        assert head.right.val == 6
        assert head.right.left.val == 5
        assert head.right.right.val == 7

        
