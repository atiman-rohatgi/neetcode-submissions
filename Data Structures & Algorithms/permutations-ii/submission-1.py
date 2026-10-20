class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        - backtrack to discover all the paths
            - in permutation no index as a parameter
        - base
            - len of curr = len of nums
        - prune
            - sort the nums
            - to make sure same num dont get used as a sibling
                - havin an index wise visited list
        - complexity
            - time = O(permutation) -> (n!) / (n-k)!, in this case n!
            - space =  O(n)
        """

        res, curr = [], []
        nums.sort()
        visited = [False] * len(nums)

        def backtrack(curr):
            #base
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            #explore the options
            for i in range(0, len(nums)):
                #prune
                if visited[i] == True:
                    continue
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:
                    continue
                visited[i] = True
                curr.append(nums[i])
                #move
                backtrack(curr)
                #undo
                curr.pop()
                visited[i] = False

        backtrack([])
        return res
        