from typing import List, NewType

IndexNum = NewType("IndexNum", int)


def binary_search(numbers: List[int], value: int) -> IndexNum:
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (right + left) // 2
        print(left, mid, right)
        if numbers[mid] == value:
            return mid
        elif value > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(numbers: List[int], value: int) -> IndexNum:
    def _binary_search(numbers: List[int], left, right) -> IndexNum:
        if left > right:
            return -1
        mid = (right + left) // 2
        if numbers[mid] == value:
            return mid
        elif value > numbers[mid]:
            left = mid + 1
            return _binary_search(numbers, left, right)
        else:
            right = mid - 1
            return _binary_search(numbers, left, right)

    return _binary_search(numbers, 0, len(numbers) - 1)


if __name__ == "__main__":
    import random

    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]
    value = 15
    # print(binary_search(nums, value))
    for v in [1, 6, 11, 20, 99]:
        print(binary_search_recursive(nums, v))
