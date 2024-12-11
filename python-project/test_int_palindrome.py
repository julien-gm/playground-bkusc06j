from int_palindrome import is_int_palindrome
from int_palindrome_v0 import is_int_palindrome_julien
from tech_io_utils import send_msg, success, fail
import builtins

str_builtin_used = False


def new_str(x):
    global str_builtin_used
    str_builtin_used = True
    return orig_str(x)


orig_str = builtins.str
builtins.str = new_str


def get_nb_palindromes(min_value: int, max_value: int, palindrome_fct: callable) -> int:
    return len([num for num in range(min_value, max_value) if palindrome_fct(num)])


def test_is_int_palindrome():
    try:
        assert is_int_palindrome(0), "0 is a palindrome"
        assert is_int_palindrome(5), "5 is a palindrome"
        assert is_int_palindrome(101), "101 is a palindrome"
        assert not is_int_palindrome(1011), "1011 is not a palindrome"
        assert is_int_palindrome(10101), "10101 is a palindrome"
        assert is_int_palindrome(82328), "82328 is a palindrome"
        assert not is_int_palindrome(823028), "823028 is not a palindrome"
        assert is_int_palindrome(97823032879), "97823032879 is not a palindrome"
        number_10001 = get_nb_palindromes(0, 990, is_int_palindrome)
        assert number_10001 == get_nb_palindromes(0, 990, is_int_palindrome_julien), f"{number_10001} != {get_nb_palindromes(0, 990, is_int_palindrome_julien)}"
        success()
        send_msg("Kudos 🌟", "Great job! 🎉")

        if str_builtin_used:
            send_msg("Warning ⚠️", "You used the str builtin. Try to solve the exercise without using it")
        else:
            send_msg("Congratulation 🎉", "You solved the exercise without using the str builtin")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == '__main__':
    test_is_int_palindrome()
