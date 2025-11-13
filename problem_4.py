def is_palindrome(n: int) -> bool:
    n = str(n)
    if n[0::] == n[::-1]:
        return True
    return False


largest_palindrome = 0

for i in range(100, 1_000):
    for j in range(100, 1_000):
        number = i * j
        if number > largest_palindrome and is_palindrome(number):
            largest_palindrome = number


print(largest_palindrome)
