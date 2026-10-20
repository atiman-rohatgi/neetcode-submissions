class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        - subsets is 2^n
        - we will backtrack to generate all possible paths
        -  cases would be two option - include or dont
            - once the end is rea ched all the paths would be added to res
        - complexity
            - time = O(2^n)
            - space = O(n)
        """
        res, curr = [], []

        def backtrack(i, curr):
            #base case
            if i == len(nums):
                res.append(curr.copy())
                return

            #exploring the choices
            #include
            curr.append(nums[i])
            backtrack(i+1, curr)

            #undo
            curr.pop()

            #dont include
            backtrack(i+1, curr)

        backtrack(0, []) #calling the function
        return res #the final list
        