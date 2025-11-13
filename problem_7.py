PRIME_RANGE = 10_001


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    n_sqrt = n ** (1 / 2)
    for i in range(3, int(n_sqrt) + 1, 2):
        if n % i == 0:
            return False
    return True


prime_index = 1
number = 1


while prime_index != PRIME_RANGE:
    number += 1
    if is_prime(number):
        prime_index += 1


print(number)
