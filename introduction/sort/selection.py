from typing import List


def selection_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        temp_index = i
        for j in range(i + 1, len_nums):
            if nums[j] < nums[temp_index]:
                temp_index = j
        nums[i], nums[temp_index] = nums[temp_index], nums[i]
    return nums


if __name__ == "__main__":
    import random

    nums = [2, 7, 3, 1, 8, 5]
    # nums = [random.randint(0, 1000) for _ in range(10)]
    print(selection_sort(nums))
