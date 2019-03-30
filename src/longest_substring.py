def lengthOfLongestSubstring( s: str):

    right = 0 
    left = 0
    sub_string = {}
    max_substring = 0
    i = 0
    while right < len(s):
        if s[right] not in sub_string:
            sub_string[s[right]] = i
            right += 1
        else:
            max_substring = max(len(sub_string), max_substring)
            sub_string.clear()
            index = s.index(s[i], left, right)
            sub_string[s[index + 1]] = i
            left = s.index(s[i], left, right) + 1
            right = left + 1

        i += 1
    return right - left

assert lengthOfLongestSubstring('abca') == 3
assert lengthOfLongestSubstring('a') == 1
assert lengthOfLongestSubstring('ababc') == 3
assert lengthOfLongestSubstring('asdsqwse') == 5
assert lengthOfLongestSubstring('aabbcc') == 2