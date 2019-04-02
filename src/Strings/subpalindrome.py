from is_palindrome import is_palindrome


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


assert longestPalindrome("aba") == "aba"
assert longestPalindrome("ababa") == "ababa"
assert longestPalindrome("asdfdg") == "dfd"
assert longestPalindrome("qwertyuy") == "yuy"
assert longestPalindrome("qwerrtyp") == "rr"
assert longestPalindrome("qwerrewq") == "qwerrewq"