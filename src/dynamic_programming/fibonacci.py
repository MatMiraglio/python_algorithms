def fibonacci_iterative(n):
    memo = {}
    for i in range(1, n + 1):
        if i <= 2:
            result = 1
        else:
            result = memo[i - 1] + memo[i - 2]
        memo[i] = result

    return memo[n]


def fibonacci(n: int):
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memoization(n: int):
    memo = {}
    return _fibonacci(n, memo)


def _fibonacci(n, memo):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    else:
        result = _fibonacci(n - 1, memo) + _fibonacci(n - 2, memo)
        memo[n] = result

    return result
