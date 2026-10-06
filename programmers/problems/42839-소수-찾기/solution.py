from itertools import permutations
from math import isqrt


def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False

    return True


def make_all_numbers(arr):
    numbers = set()

    for length in range(1, len(arr) + 1):
        for selected in permutations(arr, length):
            number = int("".join(map(str, selected)))
            if is_prime(number):
                numbers.add(number)

    return sorted(numbers)


def solution(numbers):
    return len(make_all_numbers(numbers))
