def strStr(haystack: str, needle: str) -> int:
    n = len(needle)

    for i in range(len(haystack)):
        if haystack[i:i+n] == needle:
            return i

    return -1
    

assert strStr('hello', 'll') == 2
assert strStr('hello', 'q') == -1
assert strStr('asdfqwer', 'dfq') == 2
assert strStr('my house', 'use') == 5