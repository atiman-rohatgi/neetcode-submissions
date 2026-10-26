class Solution:
    def climbStairs(self, n: int) -> int:
        """
        - at each step ther are 2 options, +1 or +2
        - target is when sum is >= n
        - have memo, store whether T/F if end reachable
        - Complexity
            - time = O()
            - space = O()

        """
        #memo
        memo = {}

        #dp function
        def dp(i):
            #base case
            if i == n:
                return 1
            if i > n:
                return 0
            
            #check in memo
            if i in memo:
                return memo[i]

            #explore values
            res = dp(i+1) + dp(i+2)
            
            #store + return
            memo[i] = res
            return memo[i]

        #main
        return dp(0)

