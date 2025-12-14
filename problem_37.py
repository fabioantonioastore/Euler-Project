prime_cache = {2}


def is_prime(n: int) -> bool:
    if n in prime_cache:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt = int(n ** (1 / 2))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    prime_cache.add(n)
    return True


def number_length(n: int) -> int:
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


def is_right_truncatable(n: int, length: int) -> bool:
    power = 10
    for _ in range(length - 1):
        ten_multiple = n % power
        n -= ten_multiple
        n //= 10
        if not is_prime(n):
            return False
    return True


def is_left_truncatable(n: int, lenght: int) -> bool:
    power = 10 ** (lenght - 1)
    for i in range(lenght - 1):
        ten_multiple = n // power
        n -= ten_multiple * power
        if not is_prime(n):
            return False
        power //= 10
    return True


def is_both_truncatable(n: int) -> bool:
    if not is_prime(n):
        return False
    lenght = number_length(n)
    return is_left_truncatable(n, lenght) and is_right_truncatable(n, lenght)


total_primes = 0
total_sum = 0
n = 11
while total_primes != 11:
    if is_both_truncatable(n):
        total_primes += 1
        total_sum += n
    n += 2


print(total_sum)
