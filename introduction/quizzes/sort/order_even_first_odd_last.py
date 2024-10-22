from typing import List


# My answer
def order_even_first_odd_last(numbers: List[int]) -> None:
    def is_even(num: int):
        return num % 2 == 0

    i = 0
    while i <= len(numbers) - 1:
        if is_even(numbers[i]) and i != len(numbers) - 1:
            i += 1
            continue

        tmp = i
        while not is_even(numbers[tmp]) and tmp < len(numbers) - 1:
            tmp += 1
        if tmp == len(numbers) - 1 and not is_even(numbers[tmp]):
            break
        while tmp > i:
            numbers[tmp], numbers[tmp - 1] = numbers[tmp - 1], numbers[tmp]
            tmp -= 1
        i += 1


if __name__ == "__main__":
    import random

    # numbers = [random.randint(0, 1000) for _ in range(8)]
    numbers = [252, 576, 852, 737, 15, 315, 79, 252]
    order_even_first_odd_last(numbers)
    print(numbers)
