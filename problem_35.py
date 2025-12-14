RANGE = 1_000_000
prime_cache = {2}


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None
        self.prev = None


class RotationList:
    def __init__(self, items: list[int]) -> None:
        self.first = None
        self.last = None
        for item in items:
            self.append(item)

    def append(self, item: int) -> None:
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
            return
        node = Node(item)
        if self.first is self.last:
            self.first.next = node
            node.prev = self.first
            self.last = node
            return
        self.last.next = node
        node.prev = self.last
        self.last = node

    def to_list(self) -> list[int]:
        items_list = []
        pointer = self.first
        while not pointer is None:
            items_list.append(pointer.data)
            pointer = pointer.next
        return items_list

    def rotate(self) -> None:
        temp_first = self.first
        temp_last = self.last
        self.last.prev.next = None
        self.last = self.last.prev
        self.first = temp_last
        self.first.next = temp_first
        self.first.prev = None
        temp_first.prev = self.first


def is_prime(n: int) -> bool:
    if n in prime_cache:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt = int(n ** (1 / 2))
    for i in range(3, sqrt + 1, 2):
        if n % i == 0:
            return False
    prime_cache.add(n)
    return True


def number_length(n: int) -> int:
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length


def number_digit(n: int, length: int, index: int) -> int:
    power = 10 ** (length - 1)
    for _ in range(index):
        ten_multiple = n // power
        n -= ten_multiple * power
        power //= 10
    n //= power
    return n


def number_to_list(n: int) -> list[int]:
    length = number_length(n)
    number_list = []
    for i in range(length):
        number_list.append(number_digit(n, length, i))
    return number_list


def list_to_number(n_list: list[int]) -> int:
    n = 0
    index = len(n_list) - 1
    for digit in n_list:
        n += digit * (10 ** index)
        index -= 1
    return n


def is_circular_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    n_list = number_to_list(n)
    rotation_list = RotationList(n_list)
    for _ in range(number_length(n) - 1):
        rotation_list.rotate()
        n_list = rotation_list.to_list()
        n = list_to_number(n_list)
        if not is_prime(n):
            return False
    return True


total = 1
for n in range(3, RANGE, 2):
    if is_circular_prime(n):
        total += 1


print(total)
