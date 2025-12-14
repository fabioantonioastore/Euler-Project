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


def digit_sum(n: int) -> int:
    length = number_length(n)
    total = 0
    for i in range(length):
        total += number_digit(n, length, i)
    return total


print(digit_sum(2**1_000))
