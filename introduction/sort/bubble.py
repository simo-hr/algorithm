from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_nums = len(numbers)
    for i in range(len_nums - 1):
        swapped = False
        limit = len_nums - i
        for j in range(0, limit - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers


if __name__ == "__main__":
    import random

    nums = [1, 7, 3, 2, 8, 5]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bubble_sort(nums))
