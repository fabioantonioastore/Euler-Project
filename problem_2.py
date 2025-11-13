fibonacci_cache = {0: 1, 1: 1}


def fibonacci(n: int) -> int:
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = result
    return result


even_fibonacci_sum = 0
term = 1


while (number := fibonacci(term)) < 4_000_000:
    if number % 2 == 0:
        even_fibonacci_sum += number
    term += 1


print(even_fibonacci_sum)
