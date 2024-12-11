from anagram import is_anagram
from tech_io_utils import send_msg, success, fail


def test_is_anagram():
    try:
        assert not is_anagram("a", "b")
        assert is_anagram("ab", "ba")
        assert is_anagram("cab", "bac")
        assert not is_anagram("abba", "bab")
        assert is_anagram("abba", "Baba")
        success()
        send_msg("Kudos 🌟", "Great job! 🎉")
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == '__main__':
    test_is_anagram()
