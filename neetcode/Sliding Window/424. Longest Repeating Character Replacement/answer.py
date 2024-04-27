class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        count = {}

        for right in range(len(s)):
            # `right`で指される文字のカウントを増やす
            count[s[right]] = count.get(s[right], 0) + 1

            # ウィンドウ内の最も頻度の高い文字のカウントが、ウィンドウのサイズからkを引いたものより小さければ、
            # `left`をインクリメントしてウィンドウを縮小する
            print(count.values())
            while max(count.values()) < (right - left + 1) - k:
                count[s[left]] -= 1
                left += 1

            # 現在のウィンドウのサイズが最大長を更新するか確認
            max_length = max(max_length, right - left + 1)

        return max_length
