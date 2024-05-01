class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        target_count = {}
        for char in s1:
            target_count[char] = target_count.get(char, 0) + 1

        window_count = {}
        for char in s2[: len1 - 1]:
            window_count[char] = window_count.get(char, 0) + 1
        print(window_count)

        for i in range(len1 - 1, len2):
            window_count[s2[i]] = window_count.get(s2[i], 0) + 1

            if window_count == target_count:
                return True

            left_char = s2[i - len1 + 1]
            if window_count[left_char] == 1:
                del window_count[left_char]
            else:
                window_count[left_char] -= 1

        return False
