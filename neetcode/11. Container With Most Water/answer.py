# https://leetcode.com/problems/container-with-most-water/
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(len(height) - i - 1):
#                 index = i + j + 1
#                 area = (j + 1) * min(height[i], height[index])
#                 max_area = max(max_area, area)
#         return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            print(area)
            res = max(res, area)
            if(height[l] <= height[r]):
                l += 1
            elif(height[r] < height[l]):
                r -= 1

        return res
