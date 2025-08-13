from collections import Counter


def valid_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    assert valid_anagram(s, t) == True
