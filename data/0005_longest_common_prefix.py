from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    base = strs[0]
    for i, c in enumerate(base):
        for s in strs:
            if i == len(s) or c != s[i]:
                return base[:i]
    return base


if __name__ == "__main__":
    strs1 = ["bat", "bag", "bank", "band"]
    strs2 = ["dance", "dag", "danger", "damage"]
    assert longest_common_prefix(strs1) == "ba"
    assert longest_common_prefix(strs2) == "da"
