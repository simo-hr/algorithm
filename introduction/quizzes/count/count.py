from typing import Tuple
from collections import Counter
import operator


# My answer
def count_max_char(sentence: str) -> Tuple[str, int]:
    formatted = sentence.replace(" ", "").lower()
    cache = {}
    maxChar = ("", 0)
    for char in formatted:
        if char in cache:
            cache[char] += 1
            if cache[char] > maxChar[1]:
                maxChar = (char, cache[char])
        else:
            cache[char] = 1
    return maxChar


# Example answer1
def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    l = []
    # for char in strings:
    #     if not char.isspace():
    #         strings.count(char)
    #         l.append((char, strings.count(char)))
    l = [(c, strings.count(c)) for c in strings if not c.isspace()]
    return max(l, key=operator.itemgetter(1))


# Example answer2
def count_chars_v2(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


# Example answer3
def count_chars_v3(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = Counter()
    for char in strings:
        if not char.isspace():
            d[char] += 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == "__main__":
    input = "This is a pen. This is an apple. Applepen."
    # print((count_max_char(input)))
    # print((count_chars_v1(input)))
    # print((count_chars_v2(input)))
    print((count_chars_v3(input)))
