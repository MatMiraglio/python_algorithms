from ..src.dynamic_programming.fibonacci import *
import unittest

class Test(unittest.TestCase):
    
    def test_fibonacci_recursive(self):
        assert fibonacci(3) == 2
        assert fibonacci(4) == 3
        assert fibonacci(5) == 5
        assert fibonacci(6) == 8

    def test_fibonacci_memoization(self):      
        assert fibonacci_memoization(3) == 2
        assert fibonacci_memoization(4) == 3
        assert fibonacci_memoization(5) == 5
        assert fibonacci_memoization(6) == 8

    def test_fibonacci_iterative(self):              
        assert fibonacci_iterative(3) == 2
        assert fibonacci_iterative(4) == 3
        assert fibonacci_iterative(5) == 5
        assert fibonacci_iterative(6) == 8

if __name__ == '__main__':
    unittest.main()