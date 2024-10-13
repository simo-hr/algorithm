from typing import List, Iterator, Tuple


# My answer
def search_symmetric(input: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    d = {}
    output = []
    for nums in input:
        key = nums[0]
        value = nums[1]
        if value in d and d[value] == key:
            output.append(nums)
        else:
            d[key] = value
    return output


# Example answer
def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[Tuple[int, int]]:
    cache = {}
    for pair in pairs:
        first, second = pair[0], pair[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield pair


if __name__ == "__main__":
    input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
# print((search_symmetric(input)))
for r in find_pair(input):
    print(r)
