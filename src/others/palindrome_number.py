def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    original = x
    count = 0

    array = []

    while x >= 10:
        x /= 10
        count += 1

    while original:
        digit = 0
        while original >= 10**count:
            digit += 1
            original -= 10**count

        array.append(digit)
        count -= 1

    left = 0
    right = len(array) - 1

    while left < right:
        if not array[left] == array[right]:
            return False
        left += 1
        right -= 1
    return True


assert isPalindrome(1001)
assert isPalindrome(2332)
assert not isPalindrome(1023)
assert not isPalindrome(123421)
assert isPalindrome(0)
assert isPalindrome(1)
assert isPalindrome(2)
assert not isPalindrome(-2)
assert not isPalindrome(-1001)
assert not isPalindrome(100)
assert not isPalindrome(10)
