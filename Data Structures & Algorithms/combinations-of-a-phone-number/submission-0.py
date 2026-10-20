class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        - since we are exploring all the paths, we use backtracking
        - we keep a map of digits and letters
        - string joining
        - exit condition is len(curr) = len(digits)
        - edge
            - if empty
        - complexity
            - time = O()
            - space = O(n)
        """
        
        if not digits:
            return []

        res = []
        phone_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(i, curr):
            #base, exit
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            #explore
            for choice in phone_map[digits[i]]:
                curr.append(choice)
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])
        return res