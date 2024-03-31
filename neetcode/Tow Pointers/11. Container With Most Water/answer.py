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


inputs = input()
n = int(inputs[0])
nums = list(map(int, inputs[1:]))
print(n, nums)

min = -100000000000
max = 0

for i in range(n):
    for j in range(n - i - 1):
        index = i + j + 1
        area = (j + 1) * min(nums[i], nums[index])
        max = max(max, area)
print(max)