from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = dict()
    for i, x in enumerate(nums):
        diff = target - x
        if diff in seen:
            return [seen[diff], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    nums = [4, 5, 6]
    target = 10
    assert two_sum(nums, target) == [0, 2]
