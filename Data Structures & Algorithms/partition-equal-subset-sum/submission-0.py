class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        - we check every option, hence dp
        - early pruning, if sum of elements not even, then always false
        - make subsets to match the half, the remaining would make the half
        - base condition
            - if i to the end
            - if the currsum > target
        - each index we check if include or exclude, and track currsum, once == target, return True
        - use memo, store states so like i,currSum as T/F, so we know if the same state then stop further calculation
        - complexity
            - time = O(n)
            - space = O(n)
        """

        #early check
        totalSum = 0
        for num in nums:
            totalSum += num
        if totalSum % 2 != 0:
            return False


        #have memo and intialize things
        #target dont needs to be non local as only being read otherwise nonlocal inside the dp function or else dp creates is own.
        target = totalSum // 2 #floor division
        memo = {}

        def dp(i, currSum):
            #base condition
            if i == len(nums) or currSum > target:
                return False
            if currSum == target:
                return True

            #check memo
            if (i, currSum) in memo:
                return memo[(i,currSum)]

            #explore
            res = dp(i+1, currSum + nums[i]) or dp(i+1, currSum)

            #store
            memo[(i, currSum)] = res #will say True, if either path reaches
            return memo[(i, currSum)]


        return dp(0, 0)
        