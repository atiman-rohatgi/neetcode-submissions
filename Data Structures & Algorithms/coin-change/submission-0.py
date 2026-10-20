class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        - we are trying to count number of ways, so we would use dp
        - store the result into a dict, we store the min coins for each diff
            - like if 12, then if 10 selected, call dp(10)+dp(12-10)
        - base case would be if remaining amount == 0
        - pruning is if the coins is bigger than the dp being called for then skip them, like dp(2) wont use 5
        - recursion would be we 1+dp(amt-coin), and we store the min
        - complexity
            - time = 
            - space = 
        """
        
        #initialize memo
        memo = {}

        def dp(rem):
            #base case
            if rem == 0:
                return 0
            #check in memo
            if rem in memo:
                return memo[rem]
            
            #recurse
            min_coins = float("inf")
            for coin in coins:
                if coin <= rem:
                    min_coins = min(min_coins, 1 + dp(rem - coin))
            
            #store
            memo[rem] = min_coins
            return memo[rem]

        ans = dp(amount)

        if ans != float("inf"):
            return ans
        else:
            return(-1)