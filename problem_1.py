MAX_RANGE = 1000
multiple_sum = 0


for number in range(1, MAX_RANGE):
    if number % 3 == 0 or number % 5 == 0:
        multiple_sum += number


print(multiple_sum)
