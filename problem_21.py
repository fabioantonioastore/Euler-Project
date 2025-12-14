RANGE = 10_000
amicable_cache = set()


def proper_divisors(n: int) -> list[int]:
    divisors = [1]
    sqrt = int(n ** (1 / 2))
    if n % 2 == 0:
        for i in range(2, sqrt + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        return divisors
    for i in range(3, sqrt, 2):
        if n % i == 0:
            divisors.extend([i, n // i])
    return divisors


def is_amicable(n: int) -> bool:
    if n in amicable_cache:
        return True
    b = sum(proper_divisors(n))
    a = sum(proper_divisors(b))
    if a != b and a == n:
        amicable_cache.add(n)
        return True
    return False


total = 0
for n in range(2, RANGE):
    if is_amicable(n):
        total += n


print(total)
