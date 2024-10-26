import math


# My answer
def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


# Example answer2
def is_prime_v2(num: int) -> bool:
    """
    36 = 1 * 36
    36 = 2 * 18
    36 = 3 * 12
    36 = 4 * 9
    36 = 6 * 6 <= √n
    36 = 9 * 4
    36 = 12 * 3
    36 = 18 * 2
    36 = 36 * 1
    """
    if num <= 1:
        return False

    # i = 2
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 1
    for x in range(2, math.floor(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True


def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    # i = 3
    # while i * i <= num:
    #     if num % i == 0:
    #         return False
    #     i += 2
    for x in range(3, math.floor(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


def is_prime_v4(num: int) -> bool:
    # 6k +- 1 <= √n
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, math.floor(math.sqrt(num) + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    # i = 5
    # while i * i <= num:
    #     if num % i == 0 or num % (i + 2) == 0:
    #         return False
    #     i += 6
    return True


if __name__ == "__main__":
    # print(is_prime(37))
    # print(is_prime_v2(37))
    import random
    import time

    numbers = [random.randint(0, 1000) for _ in range(1000000)]
    start = time.time()
    for num in numbers:
        is_prime(num)
    print("my answer", time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v2(num)
    print("v2", time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v3(num)
    print("v3", time.time() - start)

    start = time.time()
    for num in numbers:
        is_prime_v4(num)
    print("v4", time.time() - start)
