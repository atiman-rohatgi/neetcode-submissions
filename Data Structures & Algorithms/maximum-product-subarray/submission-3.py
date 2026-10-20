class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            #check the min max
            curr_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_max * num, curr_min * num)

            # Track global peak
            res = max(res, curr_max)

        return res