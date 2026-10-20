class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        - we will be using backtracking as we are trying to make all possible combinations
        - so we start by having a nums list of 1 to n, but our curr length can be only k
        - so base case would be len of curr == k, then append
        - and run till the end index
        - edge case
            - if n == k, then return 1 to n
        - prune
            - if len > k, we will break the cycle
        - complexity
            - time =  
            - space = 
        """
        #egde case
        if n == k:
            nums = []
            for num in range(1, n+1):
                nums.append(num)
            return [nums]

        res, curr = [], []

        def backtrack(i, curr):
            #base exit condition
            if len(curr) == k:
                res.append(curr.copy())
                return

            #explore
            #stop early if nums left in the range is less than k
            for j in range(i, n+1):
                curr.append(j)
                backtrack(j+1, curr)
                curr.pop() #undo

        backtrack(1, [])
        return res
