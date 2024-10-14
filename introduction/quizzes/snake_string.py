from typing import List
import operator


# My answer
def snake_string(row_count: int, word: str) -> None:
    lists = [[] for _ in range(row_count)]
    list_number = row_count // 2
    isUpper = False
    for char in word:
        for index, list in enumerate(lists):
            if list_number == index:
                list.append(char)
            else:
                list.append(" ")
        if isUpper:
            if list_number != row_count - 1:
                list_number += 1
            else:
                isUpper = False
                list_number -= 1
        else:
            if list_number != 0:
                list_number -= 1
            else:
                isUpper = True
                list_number += 1

    for list in lists:
        print("".join(list))


# Example answer1
def snake_string_v1(chars: str) -> List[List[str]]:
    result = [[], [], []]
    result_indexes = {0, 1, 2}
    insert_index = 1
    for i, s in enumerate(chars):
        if i % 4 == 1:
            insert_index = 0
        elif i % 2 == 0:
            insert_index = 1
        elif i % 4 == 3:
            insert_index = 2
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
    return result


# Example answer2
def snake_string_v2(chars: str, depth: int) -> List[List[str]]:
    result = [[] for _ in range(depth)]
    result_indexes = {i for i in range(depth)}
    insert_index = int(depth / 2)

    # def pos(i):
    #     return i + 1
    # def neg(i):
    #     return i - 1
    # pos = lambda i: i + 1
    # neg = lambda i: i - 1

    op = operator.neg
    for s in chars:
        result[insert_index].append(s)
        for rest_index in result_indexes - {insert_index}:
            result[rest_index].append(" ")
        if insert_index <= 0:
            op = operator.pos
        if insert_index >= depth - 1:
            op = operator.neg
        insert_index += op(1)

    return result


if __name__ == "__main__":
    # row_count = 10
    # word = "012345678901234567890123456789"
    # x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    # snake_string(row_count, word)
    # print(snake_string_v1("01234"))
    # numbers = [str(i) for _ in range(5) for i in range(10)]
    # strings = "".join(numbers)
    # for line in snake_string_v1(strings):
    #     print("".join(line))

    import string

    alphabet = [s for _ in range(2) for s in string.ascii_lowercase]
    strings = "".join(alphabet)
    for line in snake_string_v2(strings, 6):
        print("".join(line))
