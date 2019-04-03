def isPalindrome(x: int) -> bool:
    if x < 0: return False

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

assert isPalindrome(1001) == True
assert isPalindrome(2332) == True
assert isPalindrome(1023) == False
assert isPalindrome(123421) == False
assert isPalindrome(0) == True
assert isPalindrome(1) == True
assert isPalindrome(2) == True
assert isPalindrome(-2) == False
assert isPalindrome(-1001) == False
assert isPalindrome(100) == False
assert isPalindrome(10) == False
