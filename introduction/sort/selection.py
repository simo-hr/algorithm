from typing import List


def selection_sort(numbers: List[int]) -> List[int]:
    len_nums = len(numbers)
    for i in range(len_nums):
        min_index = i
        for j in range(i + 1, len_nums - 1):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


if __name__ == "__main__":
    import random

    nums = [1, 7, 3, 2, 8, 5]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(selection_sort(nums))
