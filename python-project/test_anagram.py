from anagram import is_anagram
from tech_io_utils import send_msg, success, fail
import builtins

sorted_builtin_used = 0


def new_sorted(x):
    global sorted_builtin_used
    sorted_builtin_used += 1
    return orig_sorted(x)


orig_sorted = builtins.sorted
builtins.sorted = new_sorted


def test_is_anagram():
    try:
        assert not is_anagram("a", "b")
        assert is_anagram("ab", "ba")
        assert is_anagram("cab", "bac")
        assert not is_anagram("abba", "bab")
        assert is_anagram("abba", "Baba")
        success()
        send_msg("Kudos 🌟", "Great job! 🎉")
        if sorted_builtin_used == 2:
            send_msg("Warning ⚠️", "You used the sorted builtin. Try to solve the exercise without using it")
        elif sorted_builtin_used == 1:
            send_msg(
                "Hint 💡",
                "You used the sorted builtin once. Maybe it would be easier to solve this exercise using it twice"
            )
        else:
            send_msg("Congratulation 🎉", "You solved the exercise without using the sorted builtin")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "If it's too difficult for you, maybe you can try to sort the strings and compare them")


if __name__ == '__main__':
    test_is_anagram()
