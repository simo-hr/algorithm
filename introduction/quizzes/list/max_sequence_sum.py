from typing import List


# My answer
# Example answer1
def get_max_or_min_sequence_sum(numbers: List[int], operator=max) -> int:
    result_sequence, sum_sequence = 0, 0
    for num in numbers:
        sum_sequence = operator(num, sum_sequence + num)
        result_sequence = operator(result_sequence, sum_sequence)
    return result_sequence


# Example answer2
def find_max_circular_sequence_sum_v1(numbers: List[int]) -> int:
    max_sequence_sum = get_max_or_min_sequence_sum(numbers)
    invert_numbers = []
    all_sum = 0
    for num in numbers:
        all_sum += num
        invert_numbers.append(-num)
    max_wrap_sequence = all_sum - (-get_max_or_min_sequence_sum(invert_numbers))
    return max(max_sequence_sum, max_wrap_sequence)


# Example answer3
def find_max_circular_sequence_sum_v2(numbers: List[int]) -> int:
    max_sequence_sum = get_max_or_min_sequence_sum(numbers)
    max_wrap_sequence = sum(numbers) - get_max_or_min_sequence_sum(numbers, min)
    return max(max_sequence_sum, max_wrap_sequence)


if __name__ == "__main__":
    input = [1, -2, 3, 6, -1, 2, 4, -5, 2]
    # print((get_max_or_min_sequence_sum(input)))
    # print((find_max_circular_sequence_sum_v1(input)))
    print((find_max_circular_sequence_sum_v2(input)))
