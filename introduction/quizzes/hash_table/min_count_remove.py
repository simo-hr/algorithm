from typing import List
from collections import Counter
import operator


# My answer
def count_max_char(numsX: List[int], numsY: List[int]):
    xCounter, yCounter = Counter(), Counter()
    for x in numsX:
        xCounter[x] += 1
    for y in numsY:
        yCounter[y] += 1

    for x in xCounter:
        if xCounter[x] < yCounter[x]:
            numsX = [n for n in numsX if n != x]

    for y in yCounter:
        if yCounter[y] < xCounter[y]:
            numsY = [n for n in numsY if n != y]

    return numsX, numsY


# Example answer1
def min_count_remove(x: List[int], y: List[int]):
    counter_x, counter_y = Counter(x), Counter(y)

    for key_x, value_x in counter_x.items():
        value_y = counter_y.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_y < value_x:
                y[:] = [i for i in y if i != key_x]


if __name__ == "__main__":
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    # print((count_max_char(x, y)))
    print((min_count_remove(x, y)))
    print(x, y)
