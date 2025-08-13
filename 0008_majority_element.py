from collections import defaultdict
from typing import List


def majority_element(nums: List[int]) -> int:
    half_len = len(nums) // 2
    counter = defaultdict(int)
    for x in nums:
        counter[x] += 1
        if counter[x] > half_len:
            return x
    return None


if __name__ == "__main__":
    nums = [5, 5, 1, 1, 1, 5, 5]
    assert majority_element(nums) == 5
