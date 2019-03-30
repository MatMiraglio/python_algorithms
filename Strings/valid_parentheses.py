def valid_parentheses(s: str) -> bool:
    openChars = ['(', '[', '{']
    stack = []

    for char in s:
        if char in openChars:
            stack.append(char)
        elif len(stack) > 0  and stack[-1] == close_to_open(char):
            stack.pop()
        else: return False

    if len(stack) == 0:
        return True

    return False

def close_to_open(char) -> str:
    if char == ')':
        return '('

    if char == ']':
        return '['

    if char == '}':
        return '{'
    
    return ""



assert valid_parentheses("()(){[]}")
assert not valid_parentheses('()[')
assert not valid_parentheses("(])")
assert not valid_parentheses('()]')

