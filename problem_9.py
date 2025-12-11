def find_solution() -> int:
    for c in range(999, 1, -1):
        for b in range(999 - c, 1, -1):
            for a in range(b, 1, -1):
                if a + b + c == 1000 and (a**2) + (b**2) == (c**2):
                    return a * b * c


print(find_solution())
