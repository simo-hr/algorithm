from typing import List


def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot_num = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot_num:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[high], nums[i + 1] = nums[i + 1], nums[high]
    return i + 1


def quick_sort(nums: List[int]) -> List[int]:
    def _quick_sort(nums: List[int], low: int, high: int) -> None:
        if low < high:
            pivot_index = partition(nums, low, high)
            _quick_sort(nums, low, pivot_index - 1)
            _quick_sort(nums, pivot_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums


if __name__ == "__main__":
    import random

    # nums = [1, 8, 3, 9, 4, 5, 7]
    nums = [1, 8, 3, 9, 4, 5, 7]
    # nums = [random.randint(0, 1000) for _ in range(10)]
    print(quick_sort(nums))
