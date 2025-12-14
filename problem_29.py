START_RANGE = 2
END_RANGE = 100
sequence = set()
for a in range(START_RANGE, END_RANGE + 1):
    for b in range(START_RANGE, END_RANGE + 1):
        sequence.add(a**b)


print(len(sequence))
