class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        - we are trying to get all the subsets, hence backtracking
        - base
            - when all nums have been processed
        - prune
            - to find duplicate combinations, we can store the made subsets in a seen set, like store in tuples
            - 
        - complexity
            - time = O(2^n)
            - space = O(n) - auxilary space
        """
        res, curr = [], []
        seen = set()

        def backtrack(i, curr):
            #base
            if i == len(nums):
                res.append(curr.copy)
                return

            #include or dont

            #undo



        backtrack()
        return res