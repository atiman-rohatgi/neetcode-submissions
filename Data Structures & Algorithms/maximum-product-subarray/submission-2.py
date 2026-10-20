class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If the current number is negative, swap max and min
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            # Decide whether to extend the current product or start a new subarray
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # Track global peak
            res = max(res, curr_max)

        return res