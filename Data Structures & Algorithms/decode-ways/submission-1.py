class Solution:
    def numDecodings(self, s: str) -> int:
        """
        - dp to figure out all the ways
        - exit is if index reached to the end, return 1
        - if 0 is read is return 0
        - evey num has 2 options - single digit is allowed and we will recurse forward
                                 - two digits tg converted to int if b/w 10 and 26 then res += dp 
        - normal memo to save over index
        - complexity    
            - time = O(n)
            - space = o(n)
        """
        
        memo = {}
        def dp(i):
            #base and exit cases
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            #in memo
            if i in memo:
                return memo[i]

            #explore
            #single num, just move ahead
            res = dp(i+1)

            #double num
            if (i+1) < len(s) and 10 <= int(s[i:i+2]) <= 26:
                res += dp(i+2)

            #store
            memo[i] = res
            return res

        return dp(0)
