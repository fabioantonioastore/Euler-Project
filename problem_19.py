START_YEAR = 1900
YEAR = 365
WEEK = 7
THIRTY = [3, 5, 10, 8]
THIRTY_ONE = [0, 2, 4, 6, 7, 9, 11]
LEAP = [1]


def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0):
        return True
    return False


def distance_day(year: int) -> int:
    distance = 1
    for i in range(1900, year):
        days = 365
        if is_leap_year(i):
            days += 1
        distance += days % WEEK
    return distance % WEEK


def year_sundays(year: int) -> int:
    distance = distance_day(year)
    total = 0
    if distance == 0:
        total += 1
    days = 31
    for i in range(0, 11):
        if i in THIRTY:
            days += 30
        if i in THIRTY_ONE:
            days += 31
        if i in LEAP:
            if is_leap_year(year):
                days += 29
            else:
                days += 28
        distance += days % 7
        if distance % 7 == 0:
            total += 1
    return total


total = 0
for i in range(1901, 2000):
    total += year_sundays(i)


print(total)
