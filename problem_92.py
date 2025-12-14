RANGE = 10_000_000
END_NUMBER = 89
chain_cache = {1: 1, 89: 89}


def number_length(n: int) -> int:
    if n == 0:
        return 0
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


def square_digits(n: int, length: int) -> int:
    new_n = 0
    for i in range(length):
        new_n += number_digit(n, length, i) ** 2
    return new_n


def evaluate_chain(n: int) -> int:
    if n in chain_cache:
        return chain_cache[n]
    n_length = number_length(n)
    new_n = square_digits(n, n_length)
    chain_cache[n] = evaluate_chain(new_n)
    return chain_cache[n]


total = 0
for n in range(1, RANGE):
    if evaluate_chain(n) == END_NUMBER:
        total += 1


print(total)


# Make fast
