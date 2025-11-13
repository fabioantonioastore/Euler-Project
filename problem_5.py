DIVISORS_RANGE = 20
divisors = [i * (DIVISORS_RANGE // i) for i in range(2, DIVISORS_RANGE)]


def is_evenly_divisible(n: int) -> bool:
    for divisor in divisors:
        if n % divisor != 0:
            return False
    return True


number = DIVISORS_RANGE


while True:
    if is_evenly_divisible(number):
        print(number)
        break
    number += DIVISORS_RANGE
