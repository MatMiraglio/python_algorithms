from collections import Counter

def has_unique_chars(string) -> bool:
        counter = Counter("")
        for char in string:
            if counter[char] > 0:
                return False

            counter[char] += 1
        
        return True

assert has_unique_chars("asd")
assert has_unique_chars("")
assert not has_unique_chars("asdfa")