class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return 0
        
        stack = []

        brac = {}
        brac["("] = ")"
        brac["{"] = "}"
        brac["["] = "]"

        for i in range (0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                if stack:
                    popped = stack.pop()
                    if brac[popped] == s[i]:
                        continue
                    else:
                        return False
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

        