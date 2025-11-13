RANGE = 100

square_sum = 1
square_of_sum = 1


for i in range(2, RANGE + 1):
    square_sum += i**2
    square_of_sum += i


print((square_of_sum**2) - square_sum)
