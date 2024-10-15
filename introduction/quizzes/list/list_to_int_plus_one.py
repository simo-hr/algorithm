from typing import Tuple, List
from collections import Counter
import operator


# My answer
def sum_with_list(nums: List[int]) -> int:
    nums = [n for n in nums if n != 0]
    nums_len = len(nums)
    return sum([n * 10 ** (nums_len - i - 1) for i, n in enumerate(nums)]) + 1


# Example answer1
def remove_zero(numbers: List[int]) -> None:
    if numbers and numbers[0] == 0:
        numbers.pop(0)
        remove_zero(numbers)


def list_to_int(numbers: List[int]) -> int:
    # return int("".join([str(i) for i in numbers]))
    sum_numbers = 0
    for i, num in enumerate(reversed(numbers)):
        sum_numbers += num * (10**i)
    return sum_numbers


def list_to_int_plus_one(numbers: List[int]) -> int:
    i = len(numbers) - 1
    numbers[i] += 1
    while 0 < i:
        if numbers[i] != 10:
            remove_zero(numbers)
            break
        numbers[i] = 0
        numbers[i - 1] += 1
        i -= 1
    else:
        if numbers[0] == 10:
            numbers[0] = 1
            numbers.append(0)

    return list_to_int(numbers)


if __name__ == "__main__":
    input = [0, 0, 0, 9, 9, 9, 9]
    # input = [1, 2, 3]
    # input = [1]
    # print((sum_with_list(input)))
    print((list_to_int_plus_one(input)))
