class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        - in this we will expand around the centres of each word
        - if odd then i,i would be the starting point
        - if even the i, i+1 starting point
            - expansion would be l-1, r+1
        - store the count of all palindromes and return
        - complexity
            - time = O(n^2)
            - space = O(1)
        """

        res = 0

        #odd case
        for i in range(0, len(s)):
            l, r = i, i
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        #even case   
        for i in range(0, len(s)):
            l, r = i, i+1
            while (l >= 0) and (r < len(s)) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res

        