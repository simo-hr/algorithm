from typing import List


# My answer1
def is_palindrome(strings: str) -> bool:
    # return strings == strings[::-1]
    def reverse(strings: str) -> str:
        reversed = ""
        strings_len = len(strings)
        for i in range(strings_len):
            reversed = reversed + strings[strings_len - 1 - i]
        return reversed

    return strings == reverse(strings)


# My answer2
def find_palindromes(strings: str) -> List[str]:
    len_strings = len(strings)
    results = []
    start = 0
    while start < len_strings:
        targets = strings[start:]
        end = len(targets)
        while end > 1:
            if is_palindrome(targets[:end]):
                results.append(targets[:end])
            end -= 1
        start += 1

    print(results)


# Example answer1
def is_palindrome(strings: str) -> bool:
    len_strings = len(strings)
    if not len_strings:
        return False
    if len_strings == 1:
        return True

    start, end = 0, len_strings - 1
    while start < end:
        if strings[start] != strings[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


# Example answer2
def find_palindrome(strings: str, left: int, right: int):
    result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        result.append(strings[left : right + 1])
        left -= 1
        right += 1
    return result


def find_all_palindrome(strings: str):
    result = []
    len_strings = len(strings)
    if not len_strings:
        return result
    if len_strings == 1:
        result.append(strings)

    for i in range(1, len_strings - 1):
        [result.append(s) for s in find_palindrome(strings, i - 1, i + 1)]
        [result.append(s) for s in find_palindrome(strings, i - 1, i)]
    return result


if __name__ == "__main__":
    strings = "aaddaa"
    # print(is_palindrome(strings))
    # (find_palindromes(strings))
    print(find_all_palindrome("cabbac"))
