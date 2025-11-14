def is_prime(n: int) -> int:
    n_sqrt = n ** (1 / 2)
    for i in range(3, int(n_sqrt) + 1, 2):
        if n % i == 0:
            return False
    return True


prime_sum = 2


for i in range(3, 2_000_000, 2):
    if is_prime(i):
        prime_sum += i


print(prime_sum)
