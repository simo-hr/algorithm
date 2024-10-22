from typing import List


# My answer
def order_change_by_indexes(strings: List[str], indexes: List[int]) -> None:
    end = len(strings) - 1
    while end > 0:
        tmp = 0
        while tmp < end:
            if indexes[tmp] > indexes[tmp + 1]:
                strings[tmp], strings[tmp + 1] = strings[tmp + 1], strings[tmp]
                indexes[tmp], indexes[tmp + 1] = indexes[tmp + 1], indexes[tmp]
            tmp += 1
        end -= 1
    return "".join(strings)


if __name__ == "__main__":
    strings, indexes = ["h", "y", "n", "p", "t", "o"], [3, 1, 5, 0, 2, 4]
    print(order_change_by_indexes(strings, indexes))
