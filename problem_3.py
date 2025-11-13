NUMBER = 600_851_475_143
NUMBER_PRIME_RANGE = int(NUMBER / 100_000) + 1


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    n_sqrt = n ** (1 / 2)
    for i in range(3, int(n_sqrt) + 1, 2):
        if n % i == 0:
            return False
    return True


for i in range(NUMBER_PRIME_RANGE, 1, -2):
    if NUMBER % i == 0 and is_prime(i):
        print(i)
        break
