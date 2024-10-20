from typing import List, Iterator


# Example answer1
def all_perms(elements: List[int]) -> List[List[int]]:
    results = []
    if len(elements) <= 1:
        return [elements]

    [1, 2, 3]
    [2, 3]
    for perm in all_perms(elements[1:]):
        for i in range(len(elements)):
            results.append(perm[:i] + elements[:1] + perm[i:])

    return results


# Example answer2
def all_perms_iterator(elements: List[int]) -> Iterator[List[int]]:
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[:1] + perm[i:]


if __name__ == "__main__":
    elements = [1, 2, 3]
    # print(all_perms(elements))
    for perm in all_perms_iterator(elements):
        print(perm)
# for i in all_perms(elements):
# print(i)
