class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        - since we need to generate all the posible paths, we use backtrack
        - pruning
            - sort the nums, and option include the current index onwards, to prevent duplicates
            - dont select any num bigger than target
            - when exploring, dont select options bigger than the diff of target and currsum
        - complexity
            - time = O(n!)
            - space = O(n)
        """
        #backtrack algo
        res, curr = [], []

        #sort the nums
        nums.sort()

        def backtrack(i, total, curr):
            #exit condition
            if total == target:
                res.append(curr.copy())
                return

            #go over all choices
            for j in range(i, len(nums)):
                choice = nums[j]
                if choice > (target - total):
                    break

                curr.append(choice)
                backtrack(j, total + choice, curr)
                curr.pop()

        #call the function
        backtrack(0, 0, [])
        return res
