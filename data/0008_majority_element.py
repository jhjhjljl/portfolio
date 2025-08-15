from collections import defaultdict
from typing import List


def majority_element(nums: List[int]) -> int:
    half_len = len(nums) // 2
    cnt = defaultdict(int)
    for x in nums:
        cnt[x] += 1
        if cnt[x] > half_len:
            return x
    return None


if __name__ == "__main__":
    nums = [5, 5, 1, 1, 1, 5, 5]
    assert majority_element(nums) == 5
