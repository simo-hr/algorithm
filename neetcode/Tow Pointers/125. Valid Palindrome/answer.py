class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = re.sub(r'[^a-z0-9]', '', s.lower())
        l = 0
        r = len(formatted) - 1
        while l < r:
            if formatted[l] != formatted[r]:
                return False
            l += 1
            r -= 1

        return True
