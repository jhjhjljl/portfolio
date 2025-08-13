from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    return nums * 2


if __name__ == "__main__":
    nums = [1, 4, 1, 2]
    assert get_concatenation(nums) == [1, 4, 1, 2, 1, 4, 1, 2]
