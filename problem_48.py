RANGE = 1_000


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


def serie_sum() -> int:
    total = 0
    for n in range(1, RANGE + 1):
        total += n**n
    return total


def last_digits(n: int, range_index: int) -> int:
    length = number_length(n)
    index = length - 1
    number = 0
    for i in range(range_index):
        number += number_digit(n, length, index) * (10**i)
        index -= 1
    return number


n = serie_sum()
print(last_digits(n, 10))
