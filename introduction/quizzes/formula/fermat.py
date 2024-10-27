from typing import List, Generator, Tuple
import sys
import time

"""
# Fermat's Last Theorem x**2 + y**2 = z**2
# 3**2 + 4**2 == 5**2 OR 6**2 + 8**2 == 10**2
# Input 10, 2 => [(3, 4, 5), (6, 8, 10)]
# (x or y <= 10)
# Input 10, 3 => []
# Input 10, 4 => []
# Input 10, 5 => []
"""


# My answer
def fermat(max_num: int, power: int) -> List[Tuple[int, int, int]]:
    max_z = int(pow((max_num - 1) ** 2 + max_num**2, 1.0 / power))
    cache = {i**power: i for i in range(1, max_z + 1)}
    result = []
    for x in range(1, max_num - 1):
        for y in range(x + 1, max_num + 1):
            v = x**power + y**power
            if cache.get(v):
                result.append((x, y, cache[v]))
    return result


# Example answer1
def fermat_last_theorem_v1(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []
    if squire_num < 2:
        return result
    max_z = int(pow((max_num - 1) ** 2 + max_num**2, 1.0 / squire_num))
    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            for z in range(y + 1, max_z):
                if pow(x, squire_num) + pow(y, squire_num) == pow(z, squire_num):
                    result.append((x, y, z))
    return result


# Example answer2
def fermat_last_theorem_v2(max_num: int, squire_num: int) -> List[Tuple[int, int, int]]:
    result = []
    if squire_num < 2:
        return result

    for x in range(1, max_num + 1):
        for y in range(x + 1, max_num + 1):
            pow_sum = pow(x, squire_num) + pow(y, squire_num)
            if pow_sum > sys.maxsize:
                raise ValueError(x, y, z, squire_num, pow_sum)
            z = pow(pow_sum, 1.0 / squire_num)
            if not z.is_integer():
                continue
            z_pow = pow(z, squire_num)
            if z_pow == pow_sum:
                result.append((x, y, z))
    return result


if __name__ == "__main__":
    # print(fermat(10, 2))
    # print(fermat(10, 3))
    # print(fermat(10, 4))
    # print(fermat(10, 5))
    # print(fermat(100, 2))

    start = time.time()
    print(fermat(20, 2))
    print("my answer", time.time() - start)
    start = time.time()
    print(fermat_last_theorem_v1(20, 2))
    print("v1", time.time() - start)
    start = time.time()
    print(fermat_last_theorem_v2(20, 2))
    print("v2", time.time() - start)
