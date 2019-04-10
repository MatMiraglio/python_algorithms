
def longest_palindrome(s: str) -> str:

    max_sub = ''

    for i in range(len(s)):
        # center is a letter "aba"
        odd = _expand(s, i, i)

        # center is between 2 letters "abba"
        even = _expand(s, i, i + 1)

        if len(odd) > len(max_sub):
            max_sub = odd

        if len(even) > len(max_sub):
            max_sub = even

    return max_sub


def _expand(string, L, R) -> int:

    end, start = L, R

    while L >= 0 and R < len(string):
        if string[L] == string[R]:
            start = L
            end = R
            R += 1
            L -= 1
        else:
            break

    return string[start:end + 1]


assert _expand('aba', 1, 1) == 'aba'
assert _expand('aabaa', 2, 2) == 'aabaa'
assert _expand('aba', 0, 1) == ''
assert longest_palindrome("aba") == "aba"
assert longest_palindrome("ababa") == "ababa"
assert longest_palindrome("asdfdg") == "dfd"
assert longest_palindrome("qwertyuy") == "yuy"
assert longest_palindrome("qwerrtyp") == "rr"
assert longest_palindrome("qwerrewq") == "qwerrewq"
