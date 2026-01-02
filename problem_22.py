def letter_alphabetical_position(letter: str) -> int:
    letter_value = ord(letter)
    return abs(ord("a") - letter_value) + 1


def name_value(name: str) -> int:
    value = 0
    for letter in name.lower():
        value += letter_alphabetical_position(letter)
    return value


items = []
with open("problem_22.txt") as file:
    for names in file:
        names = names.split(",")
        for name in names:
            items.append(name[1:-1:])
    items.sort()


total = 0
for i in range(len(items)):
    total += name_value(items[i]) * (i + 1)


print(total)
