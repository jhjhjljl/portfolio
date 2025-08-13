from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2, 3, 3]
    assert contains_duplicate(nums1) == False
    assert contains_duplicate(nums2) == True
