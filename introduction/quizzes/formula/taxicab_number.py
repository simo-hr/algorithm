from typing import List, Generator


# My answer
def taxicab_number(count: int, solve_num) -> List[int]:
    tmp_count = 0
    result = []
    answer = 1
    while tmp_count < count:
        max_param = int(pow(answer, 1.0 / 3)) + 1
        cache = {answer: []}
        for x in range(1, max_param):
            for y in range(x + 1, max_param):
                if x**3 + y**3 == answer:
                    cache[answer].append((x, y))
        if len(cache[answer]) == solve_num:
            result.append((answer, cache[answer]))
            tmp_count += 1
        answer += 1

    return result


from collections import defaultdict


# Example answer1
def taxi_cab_number(max_answer_num: int, match_answer_num: int = 2) -> List[int]:
    result = []
    got_answer_count = 0
    answer = 1
    while got_answer_count < max_answer_num:
        max_answer_count = 0
        memo = defaultdict(list)

        max_param = int(pow(answer, 1.0 / 3)) + 1
        for x in range(1, max_param):
            for y in range(x + 1, max_param):
                if x**3 + y**3 == answer:
                    max_answer_count += 1
                    memo[answer].append((x, y))
        if max_answer_count == match_answer_num:
            result.append((answer, memo[answer]))
            got_answer_count += 1
        answer += 1
    return result


if __name__ == "__main__":
    print(taxicab_number(2, 1))
    # print(taxi_cab_number(1, 3))
