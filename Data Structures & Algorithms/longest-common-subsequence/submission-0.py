class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        - this is going to be a dp + memo problem
        - and also a two pointer
        - basically at each comparision we have 2 options
            - if the chars match then move both i, j and +1 the lcs
            - if they dont match then check both option, i+1, or j+1
        - in memo we store the len of LCS till those indexes
        - complexity
            - time = O(m*n)
            - space = O(m*n)
        """

        memo = {}
        def dp(i, j):
            #base/exit
            if i == len(text1) or j == len(text2):
                return 0

            #check memo
            if (i, j) in memo:
                return memo[(i, j)]

            #recurse
            #if match
            if text1[i] == text2[j]:
                res = 1+ dp(i+1, j+1)
            else: #if dont
                res = max(dp(i, j+1), dp(i+1, j))

            #store + return
            memo[(i,j)] = res
            return res

        #main loop
        return dp(0, 0)

        