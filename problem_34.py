factorial_cache = {0: 1, 1: 1}


def factorial(n: int) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]


def number_length(n: int) -> int:
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


def number_digit(n: int, length: int, index: int) -> int:
    power = 10 ** (length - 1)
    for _ in range(index):
        ten_multiple = n // power
        n -= ten_multiple * power
        power //= 10
    n //= power
    return n


def number_equal_factorial_digits(n: int) -> bool:
    length = number_length(n)
    factorial_digit_sum = 0
    for i in range(length):
        factorial_digit_sum += factorial(number_digit(n, length, i))
    return n == factorial_digit_sum


n = 3
number_sum = 0
while n < 100_000:
    if number_equal_factorial_digits(n):
        number_sum += n
    n += 1


print(number_sum)
