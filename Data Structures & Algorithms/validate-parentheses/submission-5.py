class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {"(":")", "{":"}", "[":"]"}

        for i in range (0, len(s)):
            if s[i] in brac.keys():
                stack.append(s[i])
            elif s[i] in brac.values():
                if stack: #stack needs atleast 1
                    popped = stack.pop()
                    if brac[popped] == s[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        
        if not stack: #stack empty
            return True
        else:
            return False

        