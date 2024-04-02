class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = math.floor((l + r) / 2)
            print(l, r, mid)
            if sum((pile - 1) // mid + 1 for pile in piles) > h:
                l = mid + 1
            else:
                r = mid
        return l
