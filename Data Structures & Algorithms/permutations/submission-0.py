class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        - whenever we are generating all possible paths, we backtrack
        - every num can appear once, so use a visited set
        - k == len(nums), for the exit condition
        - edge:
            - if len(nums) is 1, return that
        - Complexity
            - time = O(permutation) -> (n!) / (n-k)!, in this case n!
            - space =  O(n)
        """
        #edge
        if len(nums) == 1:
            return[nums]

        res, curr = [], []
        k = len(nums)
        visited = set()

        def backtrack(curr):
            #base exit
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            #for choice in choices
            for num in nums:
                if num in visited:
                    continue
                # add and move
                visited.add(num)
                curr.append(num)
                backtrack(curr)
                #undo
                curr.pop()
                visited.remove(num)
        
        backtrack([])
        return res

        