class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_count = 0

        for right in range(len(s)):
            print(right, char_map, left)
            if s[right] in char_map and char_map[s[right]] >= left:
                left = char_map[s[right]] + 1
            char_map[s[right]] = right
            max_count = max(max_count, right - left + 1)
        return max_count
