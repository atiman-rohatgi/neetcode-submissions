class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        - since we are exploring all paths, we will use backtracking
        - pruning
            - if any num bigger than target, dont use
            - if any num is bigger than the diff, dont use
            - sort and only move l->r, to make sure no duplicates
        Complexity
            - time = O()
            - space = O(n)
        """
        
        res, curr = [], []
        candidates.sort()

        def backtrack(i, total, curr):
            #if solution, or exit case
            if total == target:
                res.append(curr.copy())
                return

            #go over the choices, check if any pruning
            #if solution then add to curr
            for j in range(i, len(candidates)):
                #if duplicate on the same level
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                #if the choice is bigger than the diff
                if candidates[j] > (target - total):
                    break

                curr.append(candidates[j])
                backtrack(j + 1, total + candidates[j], curr)
                curr.pop()
    
        #call the funct and return final
        backtrack(0, 0, [])
        return res
        