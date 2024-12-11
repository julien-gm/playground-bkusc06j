import math


def len_number(number: int) -> int:
    return 1 if (number < 10) else int(math.log10(number)) + 1


def is_int_palindrome_julien(n: int) -> bool:
    nb_digits = len_number(n)
    for i in range(0, nb_digits//2):
        left = (n // (10 ** (nb_digits - i - 1))) % 10
        right = (n % (10 ** (i + 1))) // 10 ** i
        if left != right:
            return False
    return True
