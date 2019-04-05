def lengthOfLongestSubstring( s: str) -> int:
    start = end = 0
    length = len(s)
    max_len = 0
    substring = {}

    while start < length and end < length:
        if s[end] not in substring:
            substring[s[end]] = '#'
            end += 1
        else:
            max_len = max(max_len, end - start)
            substring.clear()
            start += 1
            end = start

    return max(max_len, len(substring))

#optimized solution
def longest_substring(s):
        start = maxLength = 0
        indexer = {}
        
        for index, char in enumerate(s):
            if char in indexer and start <= indexer[char]:
                start = indexer[char] + 1
            else:
                maxLength = max(maxLength, index - start + 1)

            indexer[char] = index

        return maxLength



assert lengthOfLongestSubstring('abca') == 3
assert lengthOfLongestSubstring('a') == 1
assert lengthOfLongestSubstring('ababc') == 3
assert lengthOfLongestSubstring('asdsqwse') == 4
assert lengthOfLongestSubstring('aabbcc') == 2
assert lengthOfLongestSubstring('aqwaert') == 6


assert longest_substring('abca') == 3
assert longest_substring('a') == 1
assert longest_substring('ababc') == 3
assert longest_substring('asdsqwse') == 4
assert longest_substring('aabbcc') == 2
assert longest_substring('aqwaert') == 6