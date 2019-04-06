from ..src.arrays_and_strings.is_palindrome import is_palindrome

import unittest

class Test(unittest.TestCase):
    
    def test_is_palindrome(self):   
        assert is_palindrome("asdsa")
        assert not is_palindrome("asdfddsa")
        assert is_palindrome("a")
        assert is_palindrome("")
