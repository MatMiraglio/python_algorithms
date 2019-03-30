from collections import Counter

def is_permutation(first, second) -> bool:

        if len(first) != len(second):
            return False

        firstCounter = Counter(first)
        secondCounter = Counter(second)

        return firstCounter == secondCounter


assert is_permutation("abc", "cba")
assert not is_permutation('abcd', 'abc')