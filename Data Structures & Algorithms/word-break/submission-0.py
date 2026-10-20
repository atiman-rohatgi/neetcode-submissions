class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        - so at each index we check the starting char with the words
            - recurse according to the words, so multiple branches of each letter
            - the repeat for the next word
        - base is if end reached we return T or else F
        - in memo for each index we store T/F, if the end can be reached from there
        - we check word wise and match if w[0] and s[i] same then sheck them with each other
        - complexity
            - time = o(n) 
            - space = o(n)
        """

        memo = {}
        def dp(i):
            #exit/base
            if i == len(s):
                return True

            #check in memo
            if i in memo:
                return memo[i]

            #recurse
            for word in wordDict:
                if word[0] == s[i] and s[i:i+len(word)] == word:
                    if dp(i+len(word)) is True:
                        memo[i] = True
                        return True


            #store and return
            memo[i] = False
            return False

        return dp(0)

        