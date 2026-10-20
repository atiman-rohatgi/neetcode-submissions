class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        - same as palindromic subtrings, odd even centre expansion
        - but instead iof counting numbers be count max len
            - and store the string that beats it

        - complexity:
            - time = O(n^2)
            - space = O(1)
        """

        res = ""
        res_len = 0

        for i in range(0, len(s)):
            #odd
            l, r = i, i
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1

            #even
            l, r = i, i+1
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1
        
        return res
        