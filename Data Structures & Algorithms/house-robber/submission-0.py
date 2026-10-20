class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - we are moving in a striaght line, return max
        - each house we have 2 option rob/skip unless the house before has been robbed
        - if rob then we call i+2, if we skip then call i+1
        - have a memo dict to avoid re calculation
        - store the res in memo
        - complexity
            - time = O(n)
            - space = O(n)
        """
        
        memo = {}
        
        def dp(i):
            #exit case
            if i >= len(nums):
                return 0

            #check in memo
            if (i) in memo:
                return memo[i]

            #recurse
            #rob or dont, check max
            res = max(nums[i] + dp(i+2), dp(i+1))

            #store in memo and return
            memo[i] = res
            return memo[i]

        #call the start
        return dp(0)