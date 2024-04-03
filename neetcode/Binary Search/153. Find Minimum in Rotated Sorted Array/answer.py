# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             if r - l < 2:
#                 return min(nums[l], nums[r])
#             mid = math.floor((l + r) / 2)
#             l_min = min(nums[l], nums[mid - 1])
#             r_min = min(nums[mid + 1], nums[r])
#             mid_n = nums[mid]
#             print(l_min, r_min, mid_n)
#             if l_min < r_min and l_min < mid_n:
#                 r = mid - 1
#             elif r_min < l_min and r_min < mid_n:
#                 l = mid + 1
#             else:
#                 return nums[mid]
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = math.floor((l + r) / 2)
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]