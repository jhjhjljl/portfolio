from typing import List


def remove_element(nums: List[int], val: int) -> List[int]:
    k = 0
    for x in nums:
        if x != val:
            nums[k] = x
            k += 1
    return nums[:k]


if __name__ == "__main__":
    nums1 = [1, 1, 2, 3, 4]
    val1 = 1
    assert remove_element(nums1, val1) == [2, 3, 4]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    assert remove_element(nums2, val2) == [0, 1, 3, 0, 4]
