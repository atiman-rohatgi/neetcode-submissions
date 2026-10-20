class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        - exit case is going all the way to end
        - recursion is include then +1 or exclude and track the prev index to know if increasing
        - complexity
            - time - o(n^2)
            - space - o()

        """
        memo = {}

        def dp(i, prev_idx):
            #base/exit
            if i == len(nums):
                return 0

            #memo check
            if (i, prev_idx) in memo:
                return memo[(i, prev_idx)] 

            #recurse
            exclude = dp(i+1, prev_idx)

            include = 0
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                include = 1 + dp(i+1, i)

            res = max(exclude, include)

            #store and return
            memo[(i, prev_idx)] = res
            return memo[(i, prev_idx)]

        return dp(0, -1)