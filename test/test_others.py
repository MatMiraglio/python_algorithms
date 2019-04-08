from ..src.others.inplace_swap import swap
import unittest


class Test(unittest.TestCase):

    def test_swap(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 1, 4, [1, 5, 3, 4, 2]),
            ([1, 2, 3, 4, 5], 0, 1, [2, 1, 3, 4, 5]),
            ([1, 2, 3, 4, 5], 3, 4, [1, 2, 3, 5, 4])
        ]
        for case in test_cases:
            array, index1, index2, expected = case
            swap(array, index1, index2)
            assert array == expected
