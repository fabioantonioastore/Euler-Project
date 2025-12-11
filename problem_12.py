def triangle_number(n: int) -> int:
    return (n * (1 + n)) // 2


def get_total_divisors(n: int) -> int:
    total = 0
    sqrt = n ** (1 / 2)
    if sqrt == int(sqrt):
        total -= 1
    if n % 2 == 0:
        for i in range(1, int(sqrt) + 1):
            if n % i == 0:
                total += 2
        return total
    for i in range(1, int(sqrt) + 1, 2):
        if n % i == 0:
            total += 2
    return total


term = 1
while True:
    number = triangle_number(term)
    if get_total_divisors(number) > 500:
        print(number)
        break
    term += 1
