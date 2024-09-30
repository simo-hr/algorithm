from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(1, len_nums):
        temp = nums[i]
        j = i - 1
        while j >= 0 and temp < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp

    return nums


# def insertion_sort(nums: List[int]) -> List[int]:
#     len_nums = len(nums)
#     for i in range(1, len_nums):
#         j = i - 1
#         while j >= 0:
#             if nums[j + 1] < nums[j]:
#                 nums[j + 1], nums[j] = nums[j], nums[j + 1]
#             j -= 1
#     return nums


if __name__ == "__main__":
    nums = [7, 3, 1, 2, 8, 5]
    # nums = [3, 7, 1, 2, 8, 5]
    print(insertion_sort(nums))
