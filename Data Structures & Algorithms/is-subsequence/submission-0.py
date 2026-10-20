class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            # If the characters match, move the pointer for s
            if s[i] == t[j]:
                i += 1
                j += 1
            # Always move the pointer for t to keep searching
            else:
                j += 1
            
        # If we successfully moved through all characters in s, it's a subsequence
        return i == len(s)