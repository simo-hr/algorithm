"""
1. Input: [11,2,5,9,10,3], 12 => Output: (2,10) or None
2. Input: [11,2,5,9,10,3]  => Output: (11,9) or None ex) 11 + 9 = 2 + 5 + 10 + 3
"""

from typing import List, Tuple, Optional


def get_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums) - 1):
    #         if nums[i] + nums[j] == target:
    #             return nums[i], nums[j]
    cache = set()
    for num in nums:
        val = target - num
        if val in cache:
            return val, num
        cache.add(num)


def get_pair_half_sum(nums: List[int]) -> Optional[Tuple[int]]:
    # sum_numbers = sum(nums)
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums) - 1):
    #         if sum_numbers - nums[i] - nums[j] == nums[i] + nums[j]:
    #             return nums[i], nums[j]

    sum_numbers = sum(nums)
    # if sum_numbers & 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)

    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
    cache = set()
    for num in nums:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num


if __name__ == "__main__":
    inputList, value = [11, 2, 5, 9, 10, 3], 12

    [4, 3, 5]
    # sum= 40
    print(get_pair(inputList, value))
    print(get_pair_half_sum(inputList))
