class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        - we are trying to get all the subsets, hence backtracking
        - base
            - when all nums have been processed
        - prune
            - to find duplicate combinations, sort the array
            - skip the same nums on same level
        - complexity
            - time = O(2^n)
            - space = O(n) - auxilary space
        """
        res, curr = [], []
        nums.sort()

        def backtrack(i, curr):
            #base
            res.append(curr.copy())

            #explore all
            for j in range(i, len(nums)):
                #pruning
                if j > i and nums[j] == nums[j-1]:
                    continue
                
                curr.append(nums[j])
                backtrack(j+1, curr)
                curr.pop()
            
        backtrack(0, [])
        return res