from collections import defaultdict
from typing import List


def group_anagrams_unoptimal(strs: List[str]) -> List[List[str]]:
    sorted_strs = defaultdict(list)
    for s in strs:
        sorted_str = tuple(sorted(s))  # Tuple is hashable. You can also join as str.
        sorted_strs[sorted_str].append(s)
    return [val for val in sorted_strs.values()]


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        ord_map = [0] * 26
        for c in s:
            diff = ord(c) - ord("a")
            ord_map[diff] += 1
        groups[tuple(ord_map)].append(s)  # Tuple is hashable. You can also join as str.
    return [val for val in groups.values()]


if __name__ == "__main__":
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    assert group_anagrams(strs) == [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
