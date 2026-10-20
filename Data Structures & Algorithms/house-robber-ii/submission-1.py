class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        - this is basic house robber
            - but since a cycle first and last are connected
            - trick is to make two arrays (0, n-2) and (1, n-1)
        - edge case is if only one element
        - use normal dp with memo
        - exit case, when i is outside the array
        - recurse is max(i + dp(i+2), dp(i+1))
            - which is rob or skip
        - complexity
            - time = O(n)
            - space = O(n)
        """

        #edge
        if len(nums) == 1:
            return nums[0]
        
        memo1 = {}
        memo2 = {}
        arr1 = nums[:-1]
        arr2 = nums[1:]

        def dp(i, array, memo):
            #base/exit case
            if i >= len(array):
                return 0

            #check in memo
            if i in memo:
                return memo[i]
            
            #recurce
            res = max(array[i] + dp(i+2, array, memo), dp(i+1, array, memo))

            #store in memo
            memo[i] = res
            return res

        #return
        return max(dp(0, arr1, memo1), dp(0, arr2, memo2))
        