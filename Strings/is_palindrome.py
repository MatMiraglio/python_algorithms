def is_palindrome(string) -> bool:
        
        start = 0
        end = len(string) - 1

        while start < end:
            left = string[start]
            right = string[end]
            if left != right:
                return False
            start += 1
            end -= 1
            
        return True

assert is_palindrome("asdsa")
assert not is_palindrome("asdfddsa")
assert is_palindrome("a")