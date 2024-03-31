class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        map = {}
        s_nums = sorted(nums)
        print(s_nums)
        for i, n in enumerate(s_nums):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
            remain = 0 - n
            l, r = i + 1, len(s_nums) - 1
            while l < r:
                sum = s_nums[l] + s_nums[r]
                if remain > sum:
                    l += 1
                    continue
                elif remain < sum:
                    r -= 1
                    continue

                n_list = [n, s_nums[l], s_nums[r]]
                key = "".join([str(x) for x in n_list])
                if remain == sum and key not in map:
                    map[key] = [n, s_nums[l], s_nums[r]]
                l += 1
        return list(map.values())
