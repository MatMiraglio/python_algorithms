def fibonacci(n : int):
    if n <= 2:
        return 1

    return fibonacci( n - 1) + fibonacci( n - 2)

def fibonacci_memoized(n : int):
    memo = {}
    return _fibonacci(n, memo)

def _fibonacci(n, memo):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    else:
        result = _fibonacci( n - 1, memo) + _fibonacci( n - 2, memo)
        memo[n] = result

    return result

assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8

assert fibonacci_memoized(3) == 2
assert fibonacci_memoized(4) == 3
assert fibonacci_memoized(5) == 5
assert fibonacci_memoized(6) == 8