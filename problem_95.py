LIMIT = 1_000_000
amicable_cache = {}


def proper_divisors(n: int) -> list[int]:
    divisors = [1]
    sqrt = int(n ** (1 / 2))
    if n % 2 == 0:
        for i in range(2, sqrt + 1):
            if n % i == 0:
                divisors.extend([i, n // i])
        return divisors
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            divisors.extend([i, n // i])
    return divisors


def next_amicable(n: int) -> int:
    if n in amicable_cache:
        return amicable_cache[n]
    divisors = proper_divisors(n)
    amicable_cache[n] = sum(divisors)
    return amicable_cache[n]


def evaluate_chain(start_n: int, n: int = None, chain: list[int] = None) -> list[int]:
    if not n:
        n = start_n
    if not chain:
        chain = []
    if n > LIMIT:
        return []
    if n == start_n and len(chain) != 0:
        return chain
    if n in chain:
        return []
    chain.append(n)
    new_n = next_amicable(n)
    return evaluate_chain(start_n, new_n, chain)


longest_chain = []
for n in range(1, LIMIT + 1):
    chain = evaluate_chain(n)
    if len(chain) > len(longest_chain):
        longest_chain = chain


print(min(longest_chain))
