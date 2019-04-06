from is_palindrome import is_palindrome

def longest_palindrome(s: str) -> str:

    L, R = 0, 0
    max_len = 0

    for i in range(len(s)):
        left1, right1 = _expand(s, i, i)
        left2, right2 =_expand(s, i, i + 1)
        len1 = right1 - left1
        len2 = right2 - left2

        if len1 > len2 and len1 > max_len:
            L, R = left1, right1
        elif len2 > len1 and len2 > max_len:
            L, R = left2, right2



    return s[L:R]


def _expand(string, left, right):
    L = left
    R = right

    while left >= 0 and right < len(string) - 1:
        if string[left] == string[right]:
            right += 1
            left -= 1
        else:
            break
    
    return left - right - 1 



def longestPalindrome(s: str) -> str:
    start = end = 0
    sub_palindrome = ""
    length = len(s)

    while start < length:
        end = 0
        while end <= length:
            sub = s[start:end]
            if is_palindrome(sub):
                if len(sub_palindrome) < len(sub):
                    sub_palindrome = sub
            
            end += 1
        start += 1

    return sub_palindrome

assert longest_palindrome("aba") == "aba"
assert longest_palindrome("ababa") == "ababa"
assert longest_palindrome("asdfdg") == "dfd"
assert longest_palindrome("qwertyuy") == "yuy"
assert longest_palindrome("qwerrtyp") == "rr"
assert longest_palindrome("qwerrewq") == "qwerrewq"


assert longestPalindrome("aba") == "aba"
assert longestPalindrome("ababa") == "ababa"
assert longestPalindrome("asdfdg") == "dfd"
assert longestPalindrome("qwertyuy") == "yuy"
assert longestPalindrome("qwerrtyp") == "rr"
assert longestPalindrome("qwerrewq") == "qwerrewq"