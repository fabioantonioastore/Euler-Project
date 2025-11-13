MAX_TOTAL_SQUARES = 716 * 1_000
total_squares = 0
squares_sum = 0
number = 1


while total_squares != MAX_TOTAL_SQUARES:
    squares_sum += number**2
    total_squares += 2
    number += 2


print(squares_sum)
