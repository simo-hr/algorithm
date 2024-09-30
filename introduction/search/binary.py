from typing import List, NewType

IndexNum = NewType("IndexNum", int)


def binary_search(nums: List[int], value: int) -> IndexNum:
    left, right = 0, len(nums) - 1
    while left <= right:
        center = (left + right) // 2
        if value == nums[center]:
            return center
        elif value <= nums[center]:
            right = center - 1
        else:
            left = center + 1
    return -1


def binary_search_recursive(nums: List[int], value: int) -> IndexNum:
    def _binary_search(left: int, right: int) -> IndexNum:
        if left > right:
            return -1
        center = (left + right) // 2
        if value == nums[center]:
            return center
        elif value <= nums[center]:
            return _binary_search(left, center - 1)
        else:
            return _binary_search(center + 1, right)

    return _binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    import random

    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    value = 15
    # print(binary_search(nums, value))
    for v in [1, 6, 11, 20, 99]:
        print(binary_search_recursive(nums, v))
