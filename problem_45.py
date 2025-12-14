def reverse_pentagonal(n: int) -> int:
    sqrt = ((24 * n) + 1) ** (1 / 2)
    return (sqrt + 1) / 6


def hexagonal(n: int) -> int:
    return n * ((2 * n) - 1)


n = 143
while True:
    n += 1
    hexagonal_number = hexagonal(n)
    pentagonal_index = reverse_pentagonal(hexagonal_number)
    if pentagonal_index == int(pentagonal_index):
        print(hexagonal_number)
        break
