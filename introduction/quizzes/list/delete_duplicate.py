from typing import List


# My answer
def delete_duplicate(numbers: List[int]) -> None:
    d = {}
    i = 0
    while i <= len(numbers) - 1:
        if d.get(numbers[i]):
            del numbers[i]
        else:
            d[numbers[i]] = True
            i += 1


# Example answer
def delete_duplicate_v1(numbers: List[int]) -> None:
    tmp = []
    for num in numbers:
        if num not in tmp:
            tmp.append(num)
    numbers[:] = tmp


def delete_duplicate_v2(numbers: List[int]) -> None:
    tmp = [numbers[0]]
    i, len_num = 0, len(numbers) - 1
    while i < len_num:
        if numbers[i] != numbers[i + 1]:
            tmp.append(numbers[i + 1])
        i += 1
    numbers[:] = tmp


def delete_duplicate_v3(numbers: List[int]) -> None:
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] == numbers[i + 1]:
            numbers.remove(numbers[i])
            i -= 1
        i += 1


def delete_duplicate_v4(numbers: List[int]) -> None:
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i -= 1


if __name__ == "__main__":
    numbers = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]

    # print(list(set(numbers)))
    # print(list(dict.fromkeys(numbers)))
    # print([n for i, n in enumerate(numbers) if n not in numbers[:i]])

    delete_duplicate(numbers)
    delete_duplicate_v1(numbers)
    delete_duplicate_v2(numbers)
    delete_duplicate_v3(numbers)
    delete_duplicate_v4(numbers)
    print(numbers)
