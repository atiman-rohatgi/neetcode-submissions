class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        - so we will be using recursion + dp + memo
        - at each indes we track max and min prod, so we can have big multiplication
            - as negative nums are allowed
        - memo wuld store the min and max at each index
        - exit would be when i is in the beginneing as we start in the end
        - recursion would be i+1 next state and storing max_p, min_p
        """
        
        memo = {}
        max_g = 0
        
        def dp(i):
            nonlocal max_g
            #base
            if i == 0:
                return(nums[0], nums[0])
            
            #check in memo
            if i in memo:
                return memo[i]

            #recurse backwards
            prev_min, prev_max = dp(i-1)

            curr_min = min(nums[i], nums[i]*prev_min, nums[i]*prev_max)
            curr_max = max(nums[i], nums[i]*prev_min, nums[i]*prev_max)

            max_g = max(max_g, curr_max)

            #storage
            memo[i] = (curr_min, curr_max)
            
            #return
            return memo[i]

        dp(len(nums)-1) #start from last index
        return max_g

        