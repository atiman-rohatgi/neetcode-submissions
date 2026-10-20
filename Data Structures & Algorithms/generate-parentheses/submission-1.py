class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        - len of string would be 2n to be added
        - open and close would be 0 to n
        - at each point we have two option either open or close
            - we open first and open += 1, then explore close and close += 1
        - prune is open != close
        - also stop exploring if open > n or close > n
        - complexity 
            - time = 
            - space = O(n)
        """
        res = []

        def backtrack(curr, open_count, close_count):
            #base, exit
            if len(curr) == (2*n):
                res.append("".join(curr))
                return

            #explore
            #open
            if open_count < n:
                curr.append("(")
                backtrack(curr, open_count+1, close_count)
                curr.pop()

            #close
            if close_count < open_count:
                curr.append(")")
                backtrack(curr, open_count, close_count+1)
                curr.pop()

        backtrack([], 0, 0)
        return res
        