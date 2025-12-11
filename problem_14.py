RANGE = 1_000_000
chains = {1: 1}


def generate_chain(n: int) -> int:
    if n in chains:
        return chains[n]
    if n % 2 == 0:
        new_n = n // 2
        chains[n] = 1 + generate_chain(new_n)
        return chains[n]
    new_n = (3 * n) + 1
    chains[n] = 1 + generate_chain(new_n)
    return chains[n]


longest_start = 0
longest_chain = 0
for i in range(1, RANGE):
    chain = generate_chain(i)
    if chain > longest_chain:
        longest_start = i
        longest_chain = chain


print(longest_start)
