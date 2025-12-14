fibonacci_cache = {1: 1, 2: 1}


def fibonacci(n: int) -> int:
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    fibonacci_cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fibonacci_cache[n]


def number_length(n: int) -> int:
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


term = 1
while True:
    length = number_length(fibonacci(term))
    if length == 1_000:
        print(term)
        break
    term += 1
