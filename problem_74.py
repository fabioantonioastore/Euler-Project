RANGE = 1_000_000
CHAIN_LENGTH = 60
factorial_cache = {0: 1}
digit_factorial_sum_cache = {}


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


def digit_factorial_sum(n: int) -> int:
    if n in digit_factorial_sum_cache:
        return digit_factorial_sum_cache[n]
    length = number_length(n)
    new_n = 0
    for i in range(length):
        new_n += factorial(number_digit(n, length, i))
    digit_factorial_sum_cache[n] = new_n
    return new_n


def factorial_chain(n: int, chain: set = None) -> int:
    if not chain:
        chain = set()
    if n in chain:
        return 0
    chain.add(n)
    new_n = digit_factorial_sum(n)
    return 1 + factorial_chain(new_n, chain)


total = 0
for n in range(1, RANGE):
    if factorial_chain(n) == CHAIN_LENGTH:
        total += 1


print(total)
